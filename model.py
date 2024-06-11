class Model:
    def __init__(self):
        self.num_nodes = 0
        self.num_fam = 0
        self.num_req = 0
        self.capacity = 0
        self.vehicles = 0
        self.fam_members = []
        self.fam_req = []
        self.fam_dem = []
        self.cost_matrix = []


class Node:
    def __init__(self, idd, fam, costs, dem=0):
        self.ID = idd
        self.isRouted = False
        self.family = fam
        self.costs = costs
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