from model import Route


class Solution:
    def __init__(self):
        self.cost = 0.0
        self.routes = []


class Saving:
    def __init__(self, n1, n2, sav):
        self.n1 = n1
        self.n2 = n2
        self.score = sav


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
        self.Clarke_n_Wright()
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

    def CalculateTotalCost(self, sol):
        c = 0
        for i in range(0, len(sol.routes)):
            rt = sol.routes[i]
            for j in range(0, len(rt.sequenceOfNodes) - 1):
                a = rt.sequenceOfNodes[j]
                b = rt.sequenceOfNodes[j + 1]
                c += self.distanceMatrix[a.ID][b.ID]
        return c

    def UpdateRouteCostAndLoad(self, rt: Route):
        tc = 0
        tl = 0
        for i in range(0, len(rt.sequenceOfNodes) - 1):
            A = rt.sequenceOfNodes[i]
            B = rt.sequenceOfNodes[i + 1]
            tc += self.distanceMatrix[A.ID][B.ID]
            tl += A.demand
        rt.demand = tl
        rt.cost = tc

    def Clarke_n_Wright(self):
        self.sol = self.create_initial_routes()
        savings: list = self.calculate_savings()
        savings.sort(key=lambda s: s.score, reverse=True)
        for i in range(0, len(savings)):
            sav = savings[i]
            n1 = sav.n1
            n2 = sav.n2
            rt1 = n1.route
            rt2 = n2.route

            if n1.route == n2.route:
                continue
            if self.not_first_or_last(rt1, n1) or self.not_first_or_last(rt2, n2):
                continue
            if rt1.demand + rt2.demand > self.capacity:
                continue

            self.merge_routes(n1, n2)

            self.sol.cost -= sav.score
            cst = self.CalculateTotalCost(self.sol)

            # print(cst, self.sol.cost)
            a = 0
        a = 0

    def calculate_savings(self):
        savings = []
        for i in range(0, len(self.customers)):
            n1 = self.customers[i]
            for j in range(i + 1, len(self.customers)):
                n2 = self.customers[j]

                score = self.distanceMatrix[n1.ID][self.depot.ID] + self.distanceMatrix[self.depot.ID][n2.ID]
                score -= self.distanceMatrix[n1.ID][n2.ID]

                sav = Saving(n1, n2, score)
                savings.append(sav)

        return savings

    def create_initial_routes(self):
        s = Solution()
        for i in range(0, len(self.customers)):
            n = self.customers[i]
            rt = Route(i, self.capacity)
            n.route = rt
            n.position_in_route = 1
            rt.sequenceOfNodes = [self.depot, self.depot]
            rt.sequenceOfNodes.insert(1, n)
            rt.demand = n.demand
            rt.cost = self.distanceMatrix[self.depot.ID][n.ID] + self.distanceMatrix[n.ID][self.depot.ID]
            s.routes.append(rt)
            s.cost += rt.cost
        return s

    def not_first_or_last(self, rt, n):
        if n.position_in_route != 1 and n.position_in_route != len(rt.sequenceOfNodes) - 2:
            return True
        return False

    def merge_routes(self, n1, n2):
        rt1 = n1.route
        rt2 = n2.route

        if n1.position_in_route == 1 and n2.position_in_route == len(rt2.sequenceOfNodes) - 2:
            for i in range(len(rt2.sequenceOfNodes) - 2, 0, -1):
                n = rt2.sequenceOfNodes[i]
                rt1.sequenceOfNodes.insert(1, n)
        elif n1.position_in_route == 1 and n2.position_in_route == 1:
            for i in range(1, len(rt2.sequenceOfNodes) - 1, 1):
                n = rt2.sequenceOfNodes[i]
                rt1.sequenceOfNodes.insert(1, n)
        elif n1.position_in_route == len(rt1.sequenceOfNodes) - 2 and n2.position_in_route == 1:
            for i in range(1, len(rt2.sequenceOfNodes) - 1, 1):
                n = rt2.sequenceOfNodes[i]
                rt1.sequenceOfNodes.insert(len(rt1.sequenceOfNodes) - 1, n)
        elif n1.position_in_route == len(rt1.sequenceOfNodes) - 2 and n2.position_in_route == len(
                rt2.sequenceOfNodes) - 2:
            for i in range(len(rt2.sequenceOfNodes) - 2, 0, -1):
                n = rt2.sequenceOfNodes[i]
                rt1.sequenceOfNodes.insert(len(rt1.sequenceOfNodes) - 1, n)
        rt1.demand += rt2.demand
        self.sol.routes.remove(rt2)
        self.update_route_customers(rt1)

    def update_route_customers(self, rt):
        for i in range(1, len(rt.sequenceOfNodes) - 1):
            n = rt.sequenceOfNodes[i]
            n.route = rt
            n.position_in_route = i
