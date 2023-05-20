from main import (
    UndirectedPath,
    compute_shortest_paths,
)
from utils import create_example_data


def test_minimal_graph() -> None:
    """Test function to check that the shortest path computation works on the smallest graph possible. The graph consists of two nodes and a single edge between them. The function asserts that the compute_shortest_path function finds the wanted single-edged path."""
    nodes = 2
    node_connections = [((1, 2), 10)]
    test_data = create_example_data(nodes, node_connections)
    assert compute_shortest_paths(
        test_data["graph_1"], test_data["node_1"], test_data["node_2"], 1.0
    ) == [UndirectedPath([test_data["node_1"], test_data["node_2"]])]


def test_distorted_graph() -> None:
    """Test function to check that the shortest path computation works on a graph containg two different paths that lead to the end node. One path is the shortest by total length and the other is the shortest by total number of passed nodes. This test asserts that the compute_shortest_path function returns the path with the shortest total length and ignores the other path."""
    nodes = 5
    node_connections = [
        ((1, 5), 50),
        ((1, 2), 10),
        ((2, 3), 10),
        ((3, 4), 10),
        ((4, 5), 10),
    ]
    test_data = create_example_data(nodes, node_connections)
    assert compute_shortest_paths(
        test_data["graph_1"], test_data["node_1"], test_data["node_5"], 1.0
    ) == [
        UndirectedPath(
            [
                test_data["node_1"],
                test_data["node_2"],
                test_data["node_3"],
                test_data["node_4"],
                test_data["node_5"],
            ]
        )
    ]


def test_two_equally_long_paths_at_tolerance_one() -> None:
    """Test function to check the correct handling of two equally long arrived paths in a graph. Asserts that the compute_shortest_path function returns both paths given a tolerance of 1."""
    nodes = 4
    node_connections = [
        ((1, 3), 10),
        ((1, 2), 10),
        ((2, 4), 10),
        ((3, 4), 10),
    ]
    test_data = create_example_data(nodes, node_connections)
    assert set(compute_shortest_paths(
        test_data["graph_1"], test_data["node_1"], test_data["node_4"], 1.0
    )) == set([
        UndirectedPath(
            [
                test_data["node_1"],
                test_data["node_2"],
                test_data["node_4"],
            ]
        ),
        UndirectedPath(
            [
                test_data["node_1"],
                test_data["node_3"],
                test_data["node_4"],
            ]
        )
    ])
