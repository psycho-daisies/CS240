"""
Troy Brunette
BFS / DFS

This program explores using Depth First Search and Breadth First Search to explore a graph of Nodes.
For the BFS algorithm it uses a Queue data structure to keep track of the nodes that need to be explored.
For the DFS algorithm it uses a Stack data structure to keep track of the nodes that need to be explored.
There is an included data file with an example graph to explore.


Algorithm:
    * Start at an initial node
    * Visit node
    * Explore neighbors
    * check for unvisited neighbors
    * visit neighbor node/s
    * if no more unvisited neighbors, go back to previous node
    * Repeat until all nodes are visited

Pseudocode:
def depth_first_search(graph, start):
    visited = [False] * len(graph)
    stack = [start]
    order = []

    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            order.append(current)

            # Push neighbors onto the stack in the order they appear in the adjacency list
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    stack.append(neighbor)
    return order

Time Complexity: O(V + E)

"""

from hashset import HashSet
from queue import Queue
from read_from_file import get_graph, get_neighbors



def breadth_fist_search(graph, start):
    """Breadth First Search:
    """
    visited = [False] * len(graph)  # Tracks whether a Node has been visited
    queue = Queue()  # BFS uses a Queue, first in first out
    queue.enqueue(start)
    order = []  # Keeps track of the order the Nodes are visited

    while not queue.is_empty():
        current = queue.dequeue()
        if not visited[current]:
            # Visit the Node
            visited[current] = True
            order.append(current)
            # Check for unvisited neighbors and add to the queue
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    queue.enqueue(neighbor)
    return order


def depth_first_search(graph, start):
    """Depth First Search:
    """
    visited = [False] * len(graph)  # Tracks whether a Node has been visited
    stack = [start]  # DFS uses a Stack
    order = []  # Keeps track of the order the Nodes are visited

    while stack:
        current = stack.pop()
        if not visited[current]:
            # Visit the Node
            visited[current] = True
            order.append(current)
            # Check for unvisited neighbors and add to the stack
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    stack.append(neighbor)
        print(order)
    return order


def main():
    # Import data from a YAML file
    graph_data = get_graph('graph.yaml')

    # Get list of nodes and neighbors
    # Build adjacency list graph
    graph = get_neighbors(graph_data)

    # Print the Node and its neighbors
    print("Node and its connections:")
    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")

    # Run BFS and DFS
    bfs_order_numbers = breadth_fist_search(graph, 0)
    dfs_order_numbers = depth_first_search(graph, 0)

    # Print Results
    print("BFS order: ", bfs_order_numbers)
    print("DFS order: ", dfs_order_numbers)


if __name__ == "__main__":
    main()

