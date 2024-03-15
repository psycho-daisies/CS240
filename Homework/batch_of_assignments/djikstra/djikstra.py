"""
Troy Brunette
HW9 Djikstra's Algorithm

This program implements the Dijkstra's Algorithm  to find the shortest distance between a starting node
and the other nodes in a graph.

It uses the previous MinHeap assignment to ensure the shortest distance path is found.
There is a sample file included that is used to find the shortest path.

The algorithm loops while the minheap is not empty, pops from the minheap and adds to the visited,
and checks the distances for each of its neighbors


"""
from minheap import MinHeap
import yaml

# Reads an adjacency list from a file and returns a connections dictionary
def read_connections_from_file(filename):
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)
    return data.get('connections', {})

# Uses Dijkstra's Algorithm to find the shortest distance from a starting node to the other nodes in the Graph
def dijkstras(graph, start):
    # Initialize distances and visited set
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    visited = set()

    # MinHeap to store node, weight pairs (town, distance)
    minheap = MinHeap()
    minheap.push((start, 0))

    while minheap.heap:
        # Get the node with the smallest distance by popping from heap
        current, current_distance = minheap.pop()  # Get the smallest distance from the minheap

        # Skip visited nodes
        if current in visited:
            continue

        # Mark the current node as visited
        visited.add(current)

        # Update distances and check for each neighboring nodes
        for neighbor, weight in graph[current].items():
            distance = current_distance + weight

            # Update the distance if it's shorter than the current recorded distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                minheap.push((neighbor, distance))

    return distances


def main():
    # Example usage
    filename = 'towns.yaml'
    # Read data from the YAML file
    graph = read_connections_from_file(filename)
    start = input("Input Starting Town: ")

    # Run Dijkstra's algorithm
    shortest_distances = dijkstras(graph, start)

    # Print the result
    for node, distance in shortest_distances.items():
        print(f"Shortest distance from {start} to {node}: {distance}")


if __name__ == "__main__":
    main()
