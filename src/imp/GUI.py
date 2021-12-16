import math
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
    max_x = math.inf * (-1)
    min_x = math.inf
    max_y = math.inf * (-1)
    min_y = math.inf
    scalelog=0
    scalelat=0
    for node in nodes.values():
        positions = node.get__pos()
        list_pos = list(positions.split(","))
        posX = float(list_pos[0])
        posY = float(list_pos[1])
        if max_x < posX:
            max_x = posX
        if max_y < posY:
            max_y = posY
        if min_x > posX:
            min_x = posX
        if min_y > posY:
            min_y = posY

    scalelog = 1 / (max_x - min_x)
    scalelat = 1 / (max_y - min_y)

    for j in nodes.values():
        positions = j.get__pos()
        list_pos = list(positions.split(","))
        # x axis value list.
        x.append((float(list_pos[0])-min_x)*scalelog)
        # y axis value list.
        y.append((float(list_pos[1])-min_y)*scalelat)

    # Draw point based on above x, y axis values.
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, y, 'o')

    plt.show()


if __name__ == '__main__':
    draw_nodes()
