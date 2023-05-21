from main import UndirectedPath, compute_shortest_paths
from utils import create_example_data


def test_large_graph_no_tolerance() -> None:
    """
    Test function to check the shortest path computation on a large graph without tolerance. The function creates the example graph, computes the shortest paths using the compute_shortest_paths function and asserts that the result matches the expected path. The graph nodes can be visualized as
    1   2   3   4
    5   6   7   8
    9  10  11  12
    13 14  15  16
    , where each node my have an edge to lateral, horizontal or diagnoal neighbors. The defined connections and their respective length are arbitrary and the single shortest path is 1>5>9>13>14>15>16.
    """
    nodes = 16
    node_connections = [
        ((1, 6), 20),
        ((6, 11), 20),
        ((11, 16), 20),
        ((1, 5), 10),
        ((5, 9), 10),
        ((9, 13), 10),
        ((13, 14), 10),
        ((14, 15), 10),
        ((15, 16), 5),
        ((6, 2), 20),
        ((2, 3), 20),
        ((3, 4), 20),
        ((6, 7), 20),
        ((6, 10), 20),
        ((7, 10), 20),
        ((7, 3), 20),
        ((7, 8), 20),
        ((7, 11), 20),
        ((7, 12), 20),
        ((12, 16), 20),
    ]
    test_data = create_example_data(nodes, node_connections)
    computed_paths = compute_shortest_paths(
        test_data["graph_1"], test_data["node_1"], test_data["node_16"], 1.0
    )
    expected_paths = [
        UndirectedPath(
            [
                test_data["node_1"],
                test_data["node_5"],
                test_data["node_9"],
                test_data["node_13"],
                test_data["node_14"],
                test_data["node_15"],
                test_data["node_16"],
            ]
        )
    ]
    assert computed_paths == expected_paths
