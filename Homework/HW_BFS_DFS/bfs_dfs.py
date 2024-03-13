from homework.queue import Queue
from homework.read_from_file import get_graph, get_neighbors


def breadth_fist_search(graph, start):
    """Breadth First Search:
    """
    visited = [False] * len(graph)
    queue = Queue()
    queue.enqueue(start)
    order = []
    # print(f"Number of nodes in graph: {num_nodes}")

    while not queue.is_empty():
        current = queue.dequeue()
        if not visited[current]:
            visited[current] = True
            # Visit the vertex or do any operation you want
            order.append(current)

            for neighbor in graph[current]:
                if not visited[neighbor]:
                    queue.enqueue(neighbor)

    return order


def depth_first_search(graph, start):
    """Depth First Search:
    """
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
        print(order)
    return order


# Get graph from YAML file
graph_data = get_graph('graph.yaml')

# Get list of nodes and neighbors
graph_numbers = get_neighbors(graph_data)

# Print Graph
print("Node and its connections:")
for node, neighbors in graph_numbers.items():
    print(f"{node}: {neighbors}")

# Run BFS and DFS
bfs_order_numbers = breadth_fist_search(graph_numbers, 0)
dfs_order_numbers = depth_first_search(graph_numbers, 0)

# Print Results
print("BFS order: ", bfs_order_numbers)
print("DFS order: ", dfs_order_numbers)
