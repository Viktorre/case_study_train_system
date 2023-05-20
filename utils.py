from typing import Tuple, Union, List, Dict
from main import (
    UndirectedEdge,
    UndirectedGraph,
    Node,
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
