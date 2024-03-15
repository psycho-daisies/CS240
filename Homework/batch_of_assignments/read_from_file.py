import yaml

def get_graph(file):
    with open(file, 'r') as file:
        graph_data = yaml.safe_load(file)
        return graph_data.get("graph", {})

def get_neighbors(graph_data):
    neighbors_list = {}
    for node, neighbors in graph_data.items():
        neighbors_list[node] = [neighbor for neighbor in neighbors]
    return neighbors_list
