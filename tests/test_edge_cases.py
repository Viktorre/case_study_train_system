from main import (
    UndirectedPath,
    compute_shortest_paths,
)
from utils import create_example_data


def test_minimal_graph() -> None:
    """ Test function to check that the shortest path computation works on the smallest graph possible. The graph consists of two nodes and a single edge between them. The function asserts that the compute_shortest_path function finds the wanted single-edged path.
    """
    nodes = 2
    node_connections = [((1, 2), 10)]
    test_data = create_example_data(nodes,node_connections)
    assert compute_shortest_paths(
        test_data["graph_1"], test_data["node_1"], test_data["node_2"], 1.0
    ) == [UndirectedPath([test_data["node_1"], test_data["node_2"]])]


