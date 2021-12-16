import math
import matplotlib.pyplot as plt
from DiGraph import DiGraph

"""
in this class we draw the graph we receive from a Json file using matplotlib
"""

# Function draw receives a graph a draw it


def draw(di: DiGraph):
    nodes = di.get_all_v()  # all the nodes in the graph
    id_nums = []

    # id_nums holds all the id numbers of the nodes in the graph
    # used to draw the numbers of each node
    for _id in nodes:
        id_nums.append(str(_id))

    x = []  # the x values of the position of every node
    y = []  # the y values of the position of every node

    # for scaling
    max_x = math.inf * (-1)
    min_x = math.inf
    max_y = math.inf * (-1)
    min_y = math.inf

    # going through all the nodes id values in the graph
    for node in nodes.values():
        positions = node.get__pos()  # this node's position (in string format)
        list_pos = list(positions.split(","))  # converting position into a list
        posX = float(list_pos[0])  # the value at place 0 is x
        posY = float(list_pos[1])  # the value at place 1 is y

        # scaling
        if max_x < posX:
            max_x = posX
        if max_y < posY:
            max_y = posY
        if min_x > posX:
            min_x = posX
        if min_y > posY:
            min_y = posY

    scalelog = 1 / (max_x - min_x)  # scaling the x
    scalelat = 1 / (max_y - min_y)  # scaling the y

    for j in nodes.values():
        positions = j.get__pos()
        list_pos = list(positions.split(","))
        # x axis value list.
        x.append((float(list_pos[0])-min_x)*scalelog)
        # y axis value list.
        y.append((float(list_pos[1])-min_y)*scalelat)

        # Draw points based on above x, y axis values.
        dots = plt.scatter(x, y, c='red', marker='o', s=10, zorder=3)

        # Loop for annotation of all points
        for i in range(len(x)):
            plt.annotate(id_nums[i], (x[i], y[i] + 0.02))

        counter = 0
        x_s = []  # x values of source node
        y_s = []  # y values of source node
        x_d = []  # x values of dest node
        y_d = []  # y values of dest node

        # plot line between points
        for node in nodes.values():
            outE = di.all_out_edges_of_node(node.get__id())  # the edges that goes out of this node
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
                dx = x_d[counter] - x_s[counter]  # distance between x values of dest node and src node
                dy = y_d[counter] - y_s[counter]  # distance between y values of dest node and src node
                plt.arrow(x_s[counter], y_s[counter], dx, dy, head_width=0.02, width=.004, length_includes_head=True, facecolor='black')
                counter += 1

    plt.show()


if __name__ == '__main__':
    draw()
