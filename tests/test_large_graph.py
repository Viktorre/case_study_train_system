from typing import Dict, List, Tuple, Union
from main import (
    UndirectedEdge,
    UndirectedGraph,
    UndirectedPath,
    Node,
    compute_shortest_paths,
)


def create_example_data(nodes:int,node_connections:List[Union[Tuple[int],int]]) -> Dict[Node, UndirectedGraph]:
    """
    Create example data with nodes and their connections in an undirected graph.

    Args:
        nodes (int): The number of nodes to create.
        node_connections (List[Tuple[int],int]): List of tuples representing the connections between nodes. Each tuple contains two integers representing the indices of the connected nodes, and another single integer for the length of the edge connection the two nodes.

    Returns:
        Dict[Node, UndirectedGraph]: A dictionary containing the nodes and the undirected graph.

    """
    example_data = {}
    for i in range(1, nodes+1):
        example_data[f"node_{i}"] = Node(i)
    edges = []
    for node_connection in node_connections:
        edges.append(
            UndirectedEdge(
                (
                    example_data[f"node_{node_connection[0][0]}"],
                    example_data[f"node_{node_connection[0][1]}"],
                ),
                node_connection[1],
            )
        )
    example_data["graph_1"] = UndirectedGraph(edges)
    return example_data


def test_basic_graph_no_tolerance() -> None:
    """
    Test function to check the shortest path computation on a basic graph without tolerance. The function creates an example graph, computes the shortest paths using the compute_shortest_paths function and asserts that the result matches the expected path. Given this specific graph and a tolerance of 1, there exist a single shortest path.

    """
    nodes = 4
    node_connections = [((1, 2), 10),((1, 3), 30),((2, 4), 10),((3, 4), 10)]
    test_data = create_example_data(nodes, node_connections)
    assert compute_shortest_paths(
        test_data["graph_1"], test_data["node_1"], test_data["node_4"], 1.0
    ) == [
        UndirectedPath(
            [test_data["node_1"], test_data["node_2"], test_data["node_4"]]
        )
    ]

def test_basic_graph_with_tolerance() -> None:
    """
    Test function to check the shortest path computation on a basic graph without tolerance. The function creates an example graph and computes the shortest paths given a tolerance of 2.0. It asserts that the computed paths match the expected paths.
    """
    nodes = 4
    node_connections = [((1, 2), 10),((1, 3), 30),((2, 4), 10),((3, 4), 10)]
    test_data = create_example_data(nodes, node_connections)
    assert set(
        compute_shortest_paths(
            test_data["graph_1"], test_data["node_1"], test_data["node_4"], 2.0
        )
    ) == set(
        [
            UndirectedPath(
                [test_data["node_1"], test_data["node_2"], test_data["node_4"]]
            ),
            UndirectedPath(
                [test_data["node_1"], test_data["node_3"], test_data["node_4"]]
            ),
            UndirectedPath(
                [
                    test_data["node_1"],
                    test_data["node_2"],
                    test_data["node_4"],
                    test_data["node_2"],
                    test_data["node_4"],
                ]
            ),
            UndirectedPath(
                [
                    test_data["node_1"],
                    test_data["node_2"],
                    test_data["node_1"],
                    test_data["node_2"],
                    test_data["node_4"],
                ]
            ),
            UndirectedPath(
                [
                    test_data["node_1"],
                    test_data["node_2"],
                    test_data["node_4"],
                    test_data["node_3"],
                    test_data["node_4"],
                ]
            ),
        ]
    )
