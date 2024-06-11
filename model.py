class Node:
    def __init__(self, idd, xx, yy, fam, dem=0):
        self.x = xx
        self.y = yy
        self.ID = idd
        self.isRouted = False
        self.family = fam
        self.demand = dem
        self.isTabuTillIterator = -1


class Route:
    def __init__(self, cap):
        self.sequenceOfNodes = []
        self.cost = 0
        self.capacity = cap

    def update_cost(self):
        cost = 0
        for node in self.sequenceOfNodes:
            cost += node.demand
        self.cost = cost


class Family:
    def __init__(self, idd, nodes, dem, required):
        self.id = idd
        self.nodes = nodes
        self.demand = dem
        self.required = required


class Solution:
    def __init__(self):
        self.cost = 0.0
        self.routes = []
        self.sequenceOfNodes = []