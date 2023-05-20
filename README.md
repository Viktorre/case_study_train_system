# Graph Path Discovery

This project is focused on implementing a function to discover shortest paths in an undirected weighted graph with strictly positive edge lengths. The main functionality is provided in the `main.py` file, along with some supporting classes and functions found in `utils.py`.

## Project Structure

The project has the following structure:

```
├── main.py
├── utils.py
├── requirements.txt
├── tests
│   ├── test_ascending_order_of_paths.py
│   ├── test_basic_graph.py
│   ├── test_large_graph.py
│   └── test_edge_cases.py
```

- `main.py`: Contains the main implementation code for discovering shortest paths in the graph.
- `utils.py`: Contains the supporting classes and functions needed for the main implentation and testing
- `requirements.txt`: Specifies the dependencies required for running the project.
- `tests`: A directory containing test files to verify the correctness of the implementation.

## Usage

To use the project, follow these steps:

1. Make sure you have the necessary dependencies installed. You can install them using the command `pip install -r requirements.txt`.
2. Run `main.py`.
3. Run the respective tests in the `tests/` directory.


Here's an usage example:

```python
from main import compute_shortest_paths
from utils import UndirectedGraph, Node

# Create the nodes and edges of the graph
n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
demo_graph = UndirectedGraph([
    UndirectedEdge((n1, n2), 10),
    UndirectedEdge((n1, n3), 30),
    UndirectedEdge((n2, n4), 10),
    UndirectedEdge((n3, n4), 10),
])

# Find the shortest paths from n1 to n4 with a length tolerance factor of 1.0
shortest_paths = compute_shortest_paths(demo_graph, n1, n4, 1.0)
print(shortest_paths)  # Should print the path [1, 2, 4]

# Find the shortest paths from n1 to n4 with a length tolerance factor of 2.0
shortest_paths = compute_shortest_paths(demo_graph, n1, n4, 2.0)
print(shortest_paths)  # Should print multiple paths
```

## Implementation Details

The `compute_shortest_paths` function is the main entry point for discovering shortest paths in the graph. It uses a modified breadth-first search algorithm to efficiently handle cyclic paths. The function gradually creates and extends paths in all possible directions, saving the paths that successfully reach the end node. The extension of paths is stopped for paths that exceed the length tolerance limit, increasing efficiency. For higher readability the crucial steps withing the function is split up into smaller sub-functions.

The other classes (`Node`, `UndirectedEdge`, `UndirectedGraph`, `UndirectedPath`) provide the necessary data structures and operations for representing and working with the graph.

For more details on the functionality and usage of each class and function, please refer to the docstrings in the code in `main.py` and `utils.py`.

## Testing

The project includes a `tests` directory containing test files to verify the correctness of the implementation. The tests cover a standard graph, a large graph, and edge cases.

To run the tests, execute the corresponding test files using the testing framework `pytest` via shell command.

```bash
pytest tests/
```

Make sure to have the necessary testing dependencies installed before running the tests.

## Dependencies

The project has dependencies specified in the `requirements.txt` file. You can install them using the following command:

```bash
pip install -r requirements.txt
```

Please note that the project was developed and tested using Python 3.9. It may not be compatible with older versions of Python.

This project was developed and is owned by Viktor Reif. If you have suggestions or inquiries, contact viktor.reif@gmail.com
