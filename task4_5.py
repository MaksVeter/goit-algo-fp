import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.animation import FuncAnimation
import colorsys
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r,
                          y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


def array_to_heap_tree(arr):
    if not arr:
        return None

    nodes = [Node(key) for key in arr]

    for i in range(len(arr)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < len(arr):
            nodes[i].left = nodes[left_index]
        if right_index < len(arr):
            nodes[i].right = nodes[right_index]

    return nodes[0]


def update_graph(tree_root, visited_nodes, colors):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    node_colors = []
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    for node in tree.nodes(data=True):
        node_colors.append(node[1]['color'] if node[0]
                           in visited_nodes else "lightgray")

    plt.clf()
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=node_colors)
    plt.draw()


def dfs_animation(tree_root):
    stack = [tree_root]
    order = 0
    visited = set()
    steps = []
    colors = list(mcolors.CSS4_COLORS.values())

    while stack:
        node = stack.pop()
        if node.id not in visited:
            visited.add(node.id)
            node.color = colors[order % len(colors)]
            order += 1
            steps.append((set(visited), colors[:order]))
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    fig, ax = plt.subplots(figsize=(8, 5))
    ani = FuncAnimation(fig, lambda i: update_graph(
        tree_root, steps[i][0], steps[i][1]), frames=len(steps), repeat=False)
    plt.show()


def bfs_animation(tree_root):
    queue = deque([tree_root])
    order = 0
    visited = set()
    steps = []
    colors = list(mcolors.CSS4_COLORS.values())

    while queue:
        node = queue.popleft()
        if node.id not in visited:
            visited.add(node.id)
            node.color = colors[order % len(colors)]
            order += 1
            steps.append((set(visited), colors[:order]))
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    fig, ax = plt.subplots(figsize=(8, 5))
    ani = FuncAnimation(fig, lambda i: update_graph(
        tree_root, steps[i][0], steps[i][1]), frames=len(steps), repeat=False)
    plt.show()


heap_array = [10, 7, 5, 3, 2, 1]
heap_tree_root = array_to_heap_tree(heap_array)

print("Обхід в глибину (DFS):")
dfs_animation(heap_tree_root)

print("Обхід в ширину (BFS):")
bfs_animation(heap_tree_root)
