import math
import string
import matplotlib.pyplot as plt
from DiGraph import DiGraph
import pandas as pd
import numpy as np
from matplotlib.patches import ConnectionPatch

d = DiGraph("../../data/A0.json")
nodes = d.get_all_v()  # all the nodes in the graph

def draw():
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
    #ax.plot(x, y, c='red',  marker='o')
    dots = plt.scatter(x, y, c='red', marker='o', s=20, zorder=3)

    x_s = []
    y_s = []
    x_d = []
    y_d = []
    count = 0
    # plot line between points
    for node in nodes.values():
        for edge_out in d.all_out_edges_of_node(node.get__id()):
            # the x and y of src node
            src = node.get__pos()
            pos_src = list(src.split(","))
            # x axis value list.
            x_s.append((float(pos_src[0]) - min_x) * scalelog)
            # y axis value list.
            y_s.append((float(pos_src[1]) - min_y) * scalelat)

            # the x and y of dest node
            dest_id = edge_out.get_dest()
            dest = d.get_node(int(dest_id))
            pos_dest = list(dest.split(","))
            # x axis value list.
            x_d.append((float(pos_dest[0]) - min_x) * scalelog)
            # y axis value list.
            y_d.append((float(pos_dest[1]) - min_y) * scalelat)

            xyA = (x_s[count], y_s[count])
            xyB = (x_d[count], y_d[count])
            count+1
            coordsA = "data"
            coordsB = "data"
            con = ConnectionPatch(xyA, xyB, coordsA, coordsB,
                                  arrowstyle="-|>", shrinkA=5, shrinkB=5,
                                  mutation_scale=20, fc="w")

            dots.add_artist(con)


    plt.show()


if _name_ == '_main_':
    draw()
