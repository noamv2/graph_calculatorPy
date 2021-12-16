"""
This class represents a node in a graph
Node has the following info:
id : integer that represents which node it is, every node has it's own id number
pos : list with 3 parameters that represents a geographic point on the globe
tag : integer that represents the current state of node (used for algorithms i.e. BFS)
0 --> white, 1--> gray, 2--> black
"""
import string
from typing import List


class Node(object):
    # constructor
    def __init__(self, _id: int, _pos: List[float]):
        self._id = _id
        self._pos = _pos
        self._tag = 0

    # string of information
    def __str__(self):
        return f'Node({self._id},{self._pos},{self._tag})'

    # string for inside the list information
    def __repr__(self):
        return str(self)

    # getter method for id
    def get__id(self):
        return self._id

    # setter method for id
    def set__id(self, x):
        self._id = x

    # getter method for pos
    def get__pos(self):
        return self._pos

    # setter method for pos
    def set__pos(self, val):
        self._pos = val

    # getter method for tag
    def get__tag(self):
        return self._tag

    # setter method for tag
    def set__tag(self, t):
        if t < 0:
            raise ValueError("the tag is invalid")
        if t > 2:
            raise ValueError("the tag is invalid")
        self._tag = t
