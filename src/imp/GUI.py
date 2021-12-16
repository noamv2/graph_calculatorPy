import string
import matplotlib.pyplot as plt
from DiGraph import DiGraph
from matplotlib.widgets import Cursor
import numpy as np


d = DiGraph("../../data/A0.json")


def draw_nodes():
    nodes = d.get_all_v()  # all the nodes in the graph
    x = []
    y = []

    for j in nodes.values():
        positions = j.get__pos()
        list_pos = list(positions.split(","))
        # x axis value list.
        x.append(list_pos[0])
        # y axis value list.
        y.append(list_pos[1])

    # Draw point based on above x, y axis values.
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, y, 'o')

    plt.show()


if __name__ == '__main__':
    draw_nodes()








