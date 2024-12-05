import queue
import random

# libs for drawing graph
import networkx as nx
import matplotlib.pyplot as plt


def get_neighbors(graph, source):
    nodes = range(len(graph))
    neighbors = [node for node in nodes if graph[source][node] == 1]
    return neighbors


def get_distance(graph, source, destination):
    node_queue = queue.Queue()
    node_queue.put(source)
    nodes = range(len(graph))
    distances = [None for node in nodes]
    distances[source] = 0
    while node_queue:
        node = node_queue.get()
        if node == destination:
            return distances[node]
        for neighbor in get_neighbors(graph, node):
            if distances[neighbor] is None:
                node_queue.put(neighbor)
                distances[neighbor] = distances[node] + 1


def get_random_graph(graph_order):
    nodes = range(graph_order)
    graph = [[0 for _ in nodes] for _ in nodes]
    for node in nodes[:-1]:
        random_node = random.randint(node + 1, graph_order - 1)
        graph[node][random_node] = graph[random_node][node] = 1
    return graph


def get_graph(graph_order):
    nodes = range(graph_order)
    graph = [[0 for _ in nodes] for _ in nodes]
    for node in nodes:
        neighbors = [
            int(node) for node in input(f"Enter neighbors of {node}: ").split()
        ]
        for neighbor in neighbors:
            graph[node][neighbor] = graph[neighbor][node] = 1
    return graph


if __name__ == "__main__":
    graph_order = int(input("Enter graph order: "))
    if input("Generate graph? [y/n]: ") == "y":
        graph = get_random_graph(graph_order)
    else:
        graph = get_graph(graph_order)

    # drawing graph
    nodes = range(graph_order)
    graph_dict = {node: get_neighbors(graph, node) for node in nodes}
    options = {
        "node_color": "white",
        "edgecolors": "black",
    }
    nx.draw_networkx(nx.from_dict_of_lists(graph_dict), **options)
    plt.axis("off")
    plt.show()

    source = int(input("Enter source node: "))
    destination = int(input("Enter destination node: "))
    distance = get_distance(graph, source, destination)
    print(f"Distance is {distance}")
