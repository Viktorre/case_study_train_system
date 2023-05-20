from typing import Dict, List
from main import (
    UndirectedEdge,
    UndirectedGraph,
    UndirectedPath,
    Node,
    compute_shortest_paths,
)


def create_example_data() -> Dict[Node, UndirectedGraph]:
    n1, n2 = Node(1), Node(2)
    return {
        "node_01": n1,
        "node_02": n2,
        "graph_01": UndirectedGraph(
            [
                UndirectedEdge((n1, n2), 10),
            ]
        ),
    }


def test_minimal_graph_no_tolerance() -> None:
    test_data = create_example_data()
    assert compute_shortest_paths(
        test_data["graph_01"], test_data["node_01"], test_data["node_02"], 1.0
    ) == [UndirectedPath([test_data["node_01"], test_data["node_02"]])]


def test_minimal_graph_with_tolerance() -> None:
    test_data = create_example_data()
    assert set(
        compute_shortest_paths(
            test_data["graph_01"], test_data["node_01"], test_data["node_02"], 2.0
        )
    ) == set([UndirectedPath([test_data["node_01"], test_data["node_02"]])])
