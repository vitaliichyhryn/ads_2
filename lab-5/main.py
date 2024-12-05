import networkx as nx
import matplotlib.pyplot as plt
import pygraphviz


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def infix_to_postfix(expression):
    precedence = {'+': 0, '-': 0, '*': 1, '/': 1}
    operators = ['+', '-', '*', '^']
    stack = []
    postfix = []
    for char in expression:
        if char.isdigit():
            postfix.append(char)
        if char in operators:
            while stack and stack[-1] != '(' and precedence[char] < precedence[stack[-1]]:
                postfix.append(stack.pop())
            stack.append(char)
        if char == '(':
            stack.append(char)
        if char == ')':
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
    while stack:
        postfix.append(stack.pop())
    return postfix


def postfix_to_tree(postfix):
    nodes = []
    for char in postfix:
        if char.isdigit():
            nodes.append(Node(char, None, None))
        else:
            right = nodes.pop()
            left = nodes.pop()
            nodes.append(Node(char, left, right))
    return nodes[0]


def tree_to_prefix(node):
    if node is None:
        return []
    return [] + [node.value] + tree_to_prefix(node.left) + tree_to_prefix(node.right)


def tree_to_infix(node):
    operators = "+-*/"
    if node is None:
        return []
    if node.value in operators:
        return ['('] + tree_to_infix(node.left) + [node.value] + tree_to_infix(node.right) + [')']
    else:
        return tree_to_infix(node.left) + [node.value] + tree_to_infix(node.right)


def tree_to_postfix(node):
    if node is None:
        return []
    return tree_to_postfix(node.left) + tree_to_postfix(node.right) + [node.value]


def tree_to_graph(graph, node, parent=None):
    if node is not None:
        graph.add_node(node)
        if parent is not None:
            graph.add_edge(parent, node)
        tree_to_graph(graph, node.left, node)
        tree_to_graph(graph, node.right, node)


def show_graph(graph):
    labels = {node: node.value for node in graph.nodes()}
    pos = nx.nx_agraph.graphviz_layout(graph, prog='dot')
    nx.draw(graph, pos, with_labels=True, labels=labels)
    plt.show()


if __name__ == "__main__":
    expression = "9+8*(7+(6*(5+4)-(3-2))+1)"
    postfix = infix_to_postfix(expression)
    tree = postfix_to_tree(postfix)
    graph = nx.Graph()
    tree_to_graph(graph, tree)
    show_graph(graph)
    print("prefix: " + ' '.join(tree_to_prefix(tree)))
    print("infix: " + ' '.join(tree_to_infix(tree)))
    print("postfix: " + ' '.join(tree_to_postfix(tree)))
