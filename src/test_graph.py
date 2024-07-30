import unittest
import argparse
from graph import Node, Edge, Graph
from topological_sort import validate_topological_sort, find_topological_sort

# Define the test case
class TestGraphFunctions(unittest.TestCase):

    def test_topological_sort(self):
        # Initialize Graph from the file data
        if hasattr(self, 'test_file'):
            graph = Graph()
            with open(self.test_file, 'r') as file:
                data = file.read().strip()
                if data:
                    graph = Graph.from_string(data)
                else:
                    self.fail("No valid graph data to test")

            # Get the original graph representation
            graph_str = graph.to_string()
            topo_sort = find_topological_sort(graph)
            
            # Check and assert topological sort
            if topo_sort:
                topo_sort_str = [node.id for node in topo_sort]
                is_valid = validate_topological_sort(graph, topo_sort)
                self.assertTrue(is_valid, "Topological sort is invalid")
                # Include graph and sort information in the test message
                self.assertEqual(is_valid, True, f"Original Graph: {graph_str}\nTopological Sort: {topo_sort_str}")
            else:
                self.fail(f"No valid topological sort found. Original Graph: {graph_str}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run tests on Graph functionalities.")
    parser.add_argument('--file', required=True, help='Path to the file containing graph data')
    args = parser.parse_args()
    
    # Set the file argument for the test case
    TestGraphFunctions.test_file = args.file

    unittest.main(argv=['first-arg-is-ignored'], exit=False)
