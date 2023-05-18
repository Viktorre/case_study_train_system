"""A graph path discovery coding task.

In this file, you are presented with the task to implement the function `compute_shortest_paths`
which discovers some shortest paths from a start node to an end node in an undirected weighted graph
with strictly positive edge lengths. The function is marked with "TODO: Write" below and carries a
more precise specification of the expected behavior in its docstring.

Please write the implementation with the highest quality standards in mind which you would also use
for production code. Functional correctness is the most important criterion. After that it will be
evaluated in terms of maintainability and wall clock runtime for large graphs (in decreasing order
of importance). Please submit everything you have written, including documentation and tests.

Your implementation of `compute_shortest_paths` should target Python 3.9 and not use any external
dependency except for the Python standard library. Outside of the implementation of
`compute_shortest_paths` itself, you are free to use supporting libraries as long as they are
available on PyPi.org. If you use additional packages, please add a requirements.txt file which
lists them with their precise versions ("packageA==1.2.3").
"""
from functools import total_ordering
from typing import Any, List, Optional, List, Tuple, cast


class Node:
    """A node in a graph."""

    def __init__(self, id: int):
        self.id: int = id
        self.adjacent_edges: List["UndirectedEdge"] = []

    def edge_to(self, other: "Node") -> Optional["UndirectedEdge"]:
        """Returns the edge between the current node and the given one (if existing)."""
        matches = [
            edge for edge in self.adjacent_edges if edge.other_end(self) == other
        ]
        return matches[0] if len(matches) > 0 else None

    def is_adjacent(self, other: "Node") -> bool:
        """Returns whether there is an edge between the current node and the given one."""
        return other in {edge.other_end(self) for edge in self.adjacent_edges}

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Node) and self.id == other.id

    def __le__(self, other: Any) -> bool:
        return isinstance(other, Node) and self.id <= other.id

    def __hash__(self) -> int:
        return self.id

    def __repr__(self) -> str:
        return f"Node({self.id})"


class UndirectedEdge:
    """An undirected edge in a graph."""

    def __init__(self, end_nodes: Tuple[Node, Node], length: float):
        self.end_nodes: Tuple[Node, Node] = end_nodes
        if 0 < length:
            self.length: float = length
        else:
            raise ValueError(
                f"Edge connecting {end_nodes[0].id} and {end_nodes[1].id}: "
                f"Non-positive length {length} not supported."
            )

        if any(
            e.other_end(end_nodes[0]) == end_nodes[1]
            for e in end_nodes[0].adjacent_edges
        ):
            raise ValueError("Duplicate edges are not supported")

        self.end_nodes[0].adjacent_edges.append(self)
        if self.end_nodes[0] != self.end_nodes[1]:
            self.end_nodes[1].adjacent_edges.append(self)
        self.end_node_set = set(self.end_nodes)

    def other_end(self, start: Node) -> Node:
        """Returns the other end of the edge, given one of the end nodes."""
        return self.end_nodes[0] if self.end_nodes[1] == start else self.end_nodes[1]

    def is_adjacent(self, other_edge: "UndirectedEdge") -> bool:
        """Returns whether the current edge shares an end node with the given edge."""
        return len(self.end_node_set.intersection(other_edge.end_node_set)) > 0

    def __repr__(self) -> str:
        return (
            f"UndirectonalEdge(({self.end_nodes[0].__repr__()}, "
            f"{self.end_nodes[1].__repr__()}), {self.length})"
        )


class UndirectedGraph:
    """A simple undirected graph with edges attributed with their length."""

    def __init__(self, edges: List[UndirectedEdge]):
        self.edges: List[UndirectedEdge] = edges
        self.nodes_by_id = {
            node.id: node for edge in self.edges for node in edge.end_nodes
        }


@total_ordering
class UndirectedPath:
    """An undirected path through a given graph."""

    def __init__(self, nodes: List[Node]):
        assert all(
            node_1.is_adjacent(node_2) for node_1, node_2 in zip(nodes[:-1], nodes[1:])
        ), "Path edges must be a chain of adjacent nodes"
        self.nodes: List[Node] = nodes
        self.length = sum(
            cast(UndirectedEdge, node_1.edge_to(node_2)).length
            for node_1, node_2 in zip(nodes[:-1], nodes[1:])
        )

    @property
    def start(self) -> Node:
        return self.nodes[0]

    @property
    def end(self) -> Node:
        return self.nodes[-1]

    def prepend(self, edge: UndirectedEdge) -> "UndirectedPath":
        if self.start not in edge.end_nodes:
            raise ValueError("Edge is not adjacent")
        return UndirectedPath([edge.other_end(self.start)] + self.nodes)

    def append(self, edge: UndirectedEdge) -> "UndirectedPath":
        if self.end not in edge.end_nodes:
            raise ValueError("Edge is not adjacent")
        return UndirectedPath(self.nodes + [edge.other_end(self.end)])

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, UndirectedPath) and self.nodes == other.nodes

    def __le__(self, other: Any) -> bool:
        return isinstance(other, UndirectedPath) and self.length <= other.length

    def __hash__(self) -> int:
        return hash(n.id for n in self.nodes)

    def __repr__(self) -> str:
        nodestr: str = ", ".join([node.__repr__() for node in self.nodes])
        return f"UndirectedPath([{nodestr}])"


def compute_shortest_paths(
    graph: UndirectedGraph, start: Node, end: Node, length_tolerance_factor: float
) -> List[UndirectedPath]:
    """Computes and returns the N shortest paths between the given end nodes.

    The discovered paths always contain the shortest path between the two nodes. In addition, the
    second shortest, third shortest and following paths are also added (in ascending order by path
    length) up to (excluding) the path whose length is larger than the length of the shortest path
    multiplied with the given tolerance factor.

    We do not constrain this function to acyclic paths, i.e., cyclic paths should be found as well.

    For a given input of start node A, end node B and a tolerance factor of 2, the result has to
    contain all paths from A to B whose length is at most twice the length of the shortest path
    from A to B.

    Args:
        graph: The undirected graph in which the N shortest paths shall be found.
        start: The start node of the paths
        end: The end node of the paths
        length_tolerance_factor: The maximum length ratio which is allowed for the discovered paths
            (minimum: 1.0, maximum: infinite)

    Returns:
        The discovered paths. If no path from A to B exists, the result shall be empty.
    """

    # TODO: Write
    possible_paths = [UndirectedPath([start])]
    arrived_paths = []
    while possible_paths:
        possible_paths = extend_each_path_in_each_direction(possible_paths, graph)
        arrived_paths = identify_and_append_arrived_paths(
            possible_paths, arrived_paths, end
        )
        possible_paths, arrived_paths = remove_paths_that_are_too_long(
            possible_paths, arrived_paths, length_tolerance_factor
        )
    return arrived_paths


def identify_and_append_arrived_paths(
    possible_paths: List[UndirectedPath],
    arrived_paths: List[UndirectedPath],
    end: Node,
) -> List[UndirectedPath]:
    """
    checks for all possible paths if their current end point is the end point of the graph. If yes, then these paths are added to the list of arrived paths
    """
    for path in possible_paths:
        if path.end == end:
            arrived_paths.append(path)
    return arrived_paths


def remove_paths_that_are_too_long(
    possible_paths: List[UndirectedPath],
    arrived_paths: List[UndirectedPath],
    length_tolerance_factor: float,
) -> List[UndirectedPath]:
    """If at least one path arrived at the end point of the graph, the function removes all paths from the list of possible path that are longer than the shortest arrived path times the tolerance factor."""
    updated_possible_paths = []
    updated_arrived_paths = []
    if arrived_paths:
        # (maybe use @total_ordering to find fastest path)
        length_tolerance = (
            min(arrived_path.length for arrived_path in arrived_paths)
            * length_tolerance_factor
        )
        for path in possible_paths:
            if path.length <= length_tolerance:
                updated_possible_paths.append(path)
        possible_paths = updated_possible_paths
        for arrived_path in arrived_paths:
            if arrived_path.length <=length_tolerance:
                updated_arrived_paths.append(arrived_path)
        arrived_paths = updated_arrived_paths
    return possible_paths, arrived_paths


def extend_each_path_in_each_direction(
    possible_paths: List[UndirectedPath], graph: UndirectedGraph
) -> List[UndirectedPath]:
    """for each path it finds all edges that are connected to its end node. Each path is extended by its adjacent nodes. If there are several adjacent nodes, one path is updated into several different graphs, one for each adjacent node."""
    extended_possible_paths = []
    for path in possible_paths:
        for nodes in graph.nodes_by_id.values():
            if path.end.edge_to(nodes) is not None:
                extended_possible_paths.append(UndirectedPath([*path.nodes, nodes]))
    return extended_possible_paths


if __name__ == "__main__":
    # Usage example
    n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
    demo_graph = UndirectedGraph(
        [
            UndirectedEdge((n1, n2), 10),
            UndirectedEdge((n1, n3), 30),
            UndirectedEdge((n2, n4), 10),
            UndirectedEdge((n3, n4), 10),
        ]
    )
    # Should print the path [1, 2, 4]
    print(compute_shortest_paths(demo_graph, n1, n4, 1.0))

    # Should print the paths [1, 2, 4], [1, 3, 4], [1, 2, 4, 2, 4], [1, 2, 1, 2, 4], [1, 2, 4, 3, 4]
    print(len(compute_shortest_paths(demo_graph, n1, n4, 8.0)))
    

# refactor function, especially too long paths in arrived_paths (als erstes mal trennen)
# to do: write test where shortest path is found in later step, ie one direct long connection and several shorter. interesting edge case

#test large graph
#test edge cases#
# test performance