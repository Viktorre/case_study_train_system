from main import (
    UndirectedPath,
    compute_shortest_paths,
)
from utils import create_example_data


def test_ascending_order_of_paths() -> None:
    """Test function to check that the shortest path computation returns the identified paths in the right order. Assert that computed list of paths and expected list of paths is exactly equal, ie no set comparison."""
    nodes = 5
    node_connections = [
        ((1, 5), 50),
        ((1, 2), 10),
        ((2, 3), 10),
        ((3, 4), 10),
        ((4, 5), 5),
    ]
    test_data = create_example_data(nodes, node_connections)
    assert compute_shortest_paths(
        test_data["graph_1"], test_data["node_1"], test_data["node_5"], 1.5
    ) == [
        UndirectedPath(
            [
                test_data["node_1"],
                test_data["node_2"],
                test_data["node_3"],
                test_data["node_4"],
                test_data["node_5"],
            ]
        ),
        UndirectedPath(
            [
                test_data["node_1"],
                test_data["node_2"],
                test_data["node_3"],
                test_data["node_4"],
                test_data["node_5"],
                test_data["node_4"],
                test_data["node_5"],
            ]
        ),
        UndirectedPath(
            [
                test_data["node_1"],
                test_data["node_5"],
            ]
        )
    ]
