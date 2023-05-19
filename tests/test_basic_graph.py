from typing import Dict, List
from main import (
    UndirectedEdge,
    UndirectedGraph,
    UndirectedPath,
    Node,
    compute_shortest_paths,
)


def create_example_data() -> Dict[Node, UndirectedGraph]:
    """Creates a simple graph containing 4 nodes connected as a rectangular network.
    """
    n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
    return {
        "node_01": n1,
        "node_02": n2,
        "node_03": n3,
        "node_04": n4,
        "graph_01": UndirectedGraph(
            [
                UndirectedEdge((n1, n2), 10),
                UndirectedEdge((n1, n3), 30),
                UndirectedEdge((n2, n4), 10),
                UndirectedEdge((n3, n4), 10),
            ]
        ),
    }


def test_basic_graph_no_tolerance() -> None:
    """
    Test function to check the shortest path computation on a basic graph without tolerance. The function creates an example graph, computes the shortest paths using the compute_shortest_paths function and asserts that the result matches the expected path. Given this specific graph and a tolerance of 1, there exist a single shortest path.

    """
    test_data = create_example_data()
    assert compute_shortest_paths(
        test_data["graph_01"], test_data["node_01"], test_data["node_04"], 1.0
    ) == [
        UndirectedPath(
            [test_data["node_01"], test_data["node_02"], test_data["node_04"]]
        )
    ]

    test_data = create_example_data()
    assert compute_shortest_paths(
        test_data["graph_01"], test_data["node_01"], test_data["node_04"], 1.0
    ) == [
        UndirectedPath(
            [test_data["node_01"], test_data["node_02"], test_data["node_04"]]
        )
    ]


def test_basic_graph_with_tolerance() -> None:
    """
    Test function to check the shortest path computation on a basic graph without tolerance. The function creates an example graph and computes the shortest paths given a tolerance of 2.0. It asserts that the computed paths match the expected paths.
    """
    test_data = create_example_data()
    assert set(compute_shortest_paths(
        test_data["graph_01"], test_data["node_01"], test_data["node_04"], 2.0
    )) == set([
        UndirectedPath(
            [test_data["node_01"], test_data["node_02"], test_data["node_04"]]
        ),
        UndirectedPath(
            [test_data["node_01"], test_data["node_03"], test_data["node_04"]]
        ),
        UndirectedPath(
            [
                test_data["node_01"],
                test_data["node_02"],
                test_data["node_04"],
                test_data["node_02"],
                test_data["node_04"],
            ]
        ),
        UndirectedPath(
            [
                test_data["node_01"],
                test_data["node_02"],
                test_data["node_01"],
                test_data["node_02"],
                test_data["node_04"],
            ]
        ),
        UndirectedPath(
            [
                test_data["node_01"],
                test_data["node_02"],
                test_data["node_04"],
                test_data["node_03"],
                test_data["node_04"],
            ]
        ),
    ])