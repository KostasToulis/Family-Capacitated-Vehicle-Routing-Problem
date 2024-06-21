from model import Route
# from clark_wright import CnW_Solver

class Solution:
    def __init__(self):
        self.cost = 0.0
        self.routes = []





class Solver:
    def __init__(self, m):
        self.allNodes = m.nodes
        self.customers = m.customers
        self.depot = m.depot
        self.distanceMatrix = m.cost_matrix
        self.capacity = m.capacity
        self.sol = None
        self.bestSolution = None
        self.model = m

    def solve(self):
        self.select_candidates()
        self.SetRoutedFlagToFalseForAllCustomers()
        # self.Clarke_n_Wright()
        CnW_Solver()
        # self.ReportSolution(self.sol)
        return self.sol

    def select_candidates(self):
        customers = self.customers
        for customer in customers:
            customer.sumCost = sum(customer.costs)
        customers.sort(key=lambda x: x.sumCost)

        family_reqs = [0 for i in range(self.model.num_fam)]
        candidate_nodes = []
        for customer in customers:
            if family_reqs[customer.family] >= self.model.families[customer.family].required:
                continue
            candidate_nodes.append(customer)
            family_reqs[customer.family] += 1

        self.customers = candidate_nodes
        return candidate_nodes

    def SetRoutedFlagToFalseForAllCustomers(self):
        for i in range(0, len(self.customers)):
            self.customers[i].isRouted = False

        for c in self.customers:
            c.isRouted = False


