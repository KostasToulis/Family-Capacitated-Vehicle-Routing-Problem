class Model:
    def __init__(self):
        self.num_nodes = 0
        self.num_fam = 0
        self.num_req = 0
        self.capacity = 0
        self.vehicles = 0
        self.depot = None
        self.fam_members = []
        self.fam_req = []
        self.fam_dem = []
        self.cost_matrix = []
        self.nodes = None
        self.customers = None
        self.families = None
        self.solution = None


class Node:
    def __init__(self, idd, fam, costs, dem=0):
        self.ID = idd
        self.isRouted = False
        self.isDepot = False
        self.family = fam
        self.costs = costs
        self.demand = dem
        self.isTabuTillIterator = -1
        self.route = None


class Route:
    def __init__(self, idd, cap):
        self.id = idd
        self.sequenceOfNodes = []
        self.demand = 0
        self.cost = 0
        self.capacity = cap

    def update_demand(self):
        demand = 0
        for node in self.sequenceOfNodes:
            demand += node.demand
        self.demand = demand

    def update_cost(self):
        cost = 0
        for i in range(1, len(self.sequenceOfNodes)):
            cost += self.sequenceOfNodes[i].costs[self.sequenceOfNodes[i-1].id]
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