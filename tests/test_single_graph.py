from typing import Dict, List
from main import (
    UndirectedEdge,
    UndirectedGraph,
    UndirectedPath,
    Node,
    compute_shortest_paths,
)


def create_example_data() -> Dict[Node, UndirectedGraph]:
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


def test_single_graph_no_tolerance() -> None:
    test_data = create_example_data()
    assert compute_shortest_paths(
        test_data["graph_01"], test_data["node_01"], test_data["node_04"], 1.0
    ) == [
        UndirectedPath(
            [test_data["node_01"], test_data["node_02"], test_data["node_04"]]
        )
    ]


def test_single_graph_with_tolerance() -> None:
    test_data = create_example_data()
    assert compute_shortest_paths(
        test_data["graph_01"], test_data["node_01"], test_data["node_04"], 2.0
    ) == [
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
    ]
