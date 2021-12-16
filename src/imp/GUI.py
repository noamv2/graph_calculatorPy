import math
import string
import matplotlib.pyplot as plt
from DiGraph import DiGraph
import pandas as pd
import numpy as np


#d = DiGraph("../../data/A0.json")


def draw(di: DiGraph):
    nodes = di.get_all_v()  # all the nodes in the graph
    id_nums = []

    for _id in nodes:
        id_nums.append(str(_id))

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

        # ax.plot(x, y, c='red',  marker='o')
        dots = plt.scatter(x, y, c='red', marker='o', s=10, zorder=3)

        # Loop for annotation of all points
        for i in range(len(x)):
            plt.annotate(id_nums[i], (x[i], y[i] + 0.02))
        counter = 0

        x_s = []
        y_s = []
        x_d = []
        y_d = []

        # plot line between points
        for node in nodes.values():
            outE = di.all_out_edges_of_node(node.get__id())
            for edge_out in outE:

                # the x and y of src node
                src = node.get__pos()
                pos_src = list(src.split(","))
                # x axis value list.
                x_s.append((float(pos_src[0]) - min_x) * scalelog)
                # y axis value list.
                y_s.append((float(pos_src[1]) - min_y) * scalelat)

                # the x and y of dest node
                dest_id = int(edge_out)
                dest = di.get_node(dest_id).get__pos()
                pos_dest = list(dest.split(","))
                # x axis value list.
                x_d.append((float(pos_dest[0]) - min_x) * scalelog)
                # y axis value list.
                y_d.append((float(pos_dest[1]) - min_y) * scalelat)

                # add arrow to plot
                dx = x_d[counter] - x_s[counter]
                dy = y_d[counter] - y_s[counter]
                plt.arrow(x_s[counter], y_s[counter], dx, dy, head_width=0.02, width=.004, length_includes_head=True, facecolor='black')
                counter += 1


    plt.show()


if __name__ == '__main__':
    draw()
