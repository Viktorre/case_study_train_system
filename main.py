"""
This script computes and returns the N shortest paths between two given end nodes
in an undirected graph. The paths are determined based on a length tolerance factor,
which allows paths up to a certain length ratio compared to the shortest path. The
program uses a modified breadth-first search algorithm, which handles cyclic paths 
efficiently. The script provides an example usage with a demo graph.
"""
from typing import List

from utils import (
    UndirectedEdge,
    UndirectedGraph,
    UndirectedPath,
    Node,
)


def compute_shortest_paths(
    graph: UndirectedGraph, start: Node, end: Node, length_tolerance_factor: float
) -> List[UndirectedPath]:
    """Computes and returns the N shortest paths between the given end nodes. The
    discovered paths always contain the shortest path between the two nodes. In
    addition, the second shortest, third shortest and following paths are also
    added (in ascending order by path length) up to (excluding) the path whose
    length is larger than the length of the shortest path multiplied with the
    given tolerance factor. Paths may be cyclic, meaning paths can go back an
    forth between nodes as in a circle. This function uses an breadth-first search
    algorithm, which is modified to efficiently handle cyclic paths. Given a start
    node, the function gradually creates and extends paths in all possible
    directions including cyclic conncections. It saves all paths that successfully
    reach the end node. The modification is that the function stops extending paths
    that are too long given the tolerance to increase efficiency. The process of
    extending paths is repeated until all paths reach the length tolerance limit.
    When the process is finished, the result is the list of arrived paths ordered
    by length, which is returned.

    Args:
        graph (UndirectedGraph): The undirected graph in which the N shortest paths
            shall be found.
        start (Node): The start node of the paths
        end (Node): The end node of the paths
        length_tolerance_factor (float): The maximum length ratio which is allowed
            for the discovered paths (minimum: 1.0, maximum: infinite)

    Returns:
        (List[UndirectedPath]): The discovered paths. If no path from A to B exists,
            the result list is empty.
    """
    if length_tolerance_factor < 1.0:
        raise ValueError(
            "length_tolerance_factor must be greater than or equal to 1.0."
        )

    paths = [UndirectedPath([start])]
    arrived_paths = []
    while paths:
        paths = extend_each_path_in_each_direction(paths, graph)
        if arrived_paths := identify_and_append_arrived_paths(
            paths, arrived_paths, end
        ):
            length_tolerance = compute_length_tolerance(
                arrived_paths, length_tolerance_factor
            )
            paths = remove_too_long_paths(paths, length_tolerance)
            arrived_paths = remove_too_long_paths(arrived_paths, length_tolerance)

    return sorted(arrived_paths, key=lambda path: path.length, reverse=False)


def identify_and_append_arrived_paths(
    paths: List[UndirectedPath],
    arrived_paths: List[UndirectedPath],
    end: Node,
) -> List[UndirectedPath]:
    """
    checks for all possible paths if their current end point is the end point of
    the graph. If yes, then these paths are added to the list of arrived paths.
    Args:
        paths (List[UndirectedPath]): A list of UndirectedPath objects representing
            the current paths.
        arrived_paths (List[UndirectedPath]): A list of UndirectedPath objects
            representing the paths that have already arrived at the end node.
        end (node): The end node to compare against the end points of the paths.

    Returns:
        (List[UndirectedPath]): A list of UndirectedPath objects containing the
            former arrived paths as well as the added updated arrived paths.
    """
    new_arrived_paths = [path for path in paths if path.end == end]
    arrived_paths.extend(new_arrived_paths)
    return arrived_paths


def remove_too_long_paths(
    paths: List[UndirectedPath],
    length_tolerance: float,
) -> List[UndirectedPath]:
    """If at least one path arrived at the end point of the graph, the function
    removes all paths from the list of given paths that are longer than the
    shortest arrived path times the tolerance factor.

    Args:
        paths (List[UndirectedPath]): A list of UndirectedPath objects representing
            the paths to be evaluated and potentially removed.
        length_tolerance (float): A float value representing the maximum allowed
            length ratio compared to the shortest arrived path length.

    Returns:
        (List[UndirectedPath]): A list of UndirectedPath objects containing the
            updated paths with any paths longer than the length tolerance removed.
    """
    updated_paths = [path for path in paths if path.length <= length_tolerance]
    return updated_paths


def compute_length_tolerance(
    arrived_paths: List[UndirectedPath], length_tolerance_factor: float
) -> float:
    """If at least on path arrived at the end node, ie the list of arrived path
    is not empty, the length tolerance is computed by multiplying the shortest
    arrived path length with the tolerance factor.
    Args:
        arrived_paths (List[UndirectedPath]): A list of UndirectedPath objects
            representing the paths that have successfully arrived at the end node.
        length_tolerance_factor (float): A float value representing the tolerance
            factor to be applied to the shortest arrived path length.

    Returns:
        (float): A float value representing the computed length tolerance. It is
            determined by multiplying the length of the shortest arrived path by
            the length tolerance factor.
    """
    length_tolerance = (
        min(arrived_path.length for arrived_path in arrived_paths)
        * length_tolerance_factor
    )
    return length_tolerance


def extend_each_path_in_each_direction(
    paths: List[UndirectedPath], graph: UndirectedGraph
) -> List[UndirectedPath]:
    """For each path, the function finds all edges that are connected to its end node.
    Each path is extended by its adjacent nodes. If there are several adjacent nodes,
    one path is updated into several different graphs, one for each adjacent node.
    This function uses a complex list comprehension to generate the extended paths.
    Its logic can be described as:
    extended_paths = []
    for path in paths:
        for nodes in graph.nodes_by_id.values():
            if path.end.edge_to(nodes) is not None:
                extended_paths.append(UndirectedPath([*path.nodes, nodes]))
    Args:
        paths (List[UndirectedPath]): The list of paths to be extended.
        graph (UndirectedGraph): The undirected graph containing the paths.

    Returns:
        List[UndirectedPath]: The extended paths.
    """
    extended_paths = [
        UndirectedPath([*path.nodes, nodes])
        for path in paths
        for nodes in graph.nodes_by_id.values()
        if path.end.edge_to(nodes) is not None
    ]
    return extended_paths


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
    print(compute_shortest_paths(demo_graph, n1, n4, 2.0))
