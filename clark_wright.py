# import numpy as np
# import math
# import time
# import itertools
# from model import Route
#
#
# class Saving:
#     def __init__(self, node1, node2, value):
#         self.i = node1
#         self.j = node2
#         self.value = value
#
#
# def CalculateSavingsMatrix(nodes):
#     savings = []
#     for i in range(len(nodes)):
#         for j in range(i + 1, len(nodes)):
#             value = nodes[j].costs[0] + nodes[i].costs[0] - nodes[i].costs[nodes[j].id]
#             savings.append(Saving(nodes[i], nodes[j], value))
#     return savings
#
#
# def CheckEdgeNode(route, node):
#     if (route.nodes[1].id == node.id or route.nodes[-2].id == node.id):
#         return True
#     else:
#         return False
#
#
# def CheckEdgeNodePosition(route, node):
#     if (route.nodes[1].id == node.id):
#         return 1
#     elif (route.nodes[-2].id == node.id):
#         return 2
#
#
# def ConnectRoutes(route1, route2):
#     id = route1.id
#     route = route1.nodes[:-1]
#     for i in range(1, len(route2.nodes)):
#         route.append(route2.nodes[i])
#     return Route(id, route)
#
#
# def ReverseRoute(route):
#     route.nodes.reverse()
#     return route[1, :]
#
#
# def UpdateRouteNodes(route):
#     for node in route.nodes:
#         node.route = route
#
#
# def clark_n_wright(model, candidate_nodes):
#
#     #Create one route per customer
#     routes = []
#     for i, node in enumerate(candidate_nodes):
#         route = Route(i, model.capacity)
#         route.sequenceOfNodes = [model.depot, node, model.depot]
#         route.demand = node.demand
#         route.cost = node.costs[0] + node.costs[0]
#         node.route = route
#         routes.append(route)
#
#     savings = CalculateSavingsMatrix(candidate_nodes)
#     savings.sort(key=lambda x: x.value, reverse=True)
#
#     for saving in savings:
#         route1 = saving.i.route
#         route2 = saving.j.route
#         if (CheckEdgeNode(route1, saving.i) and CheckEdgeNode(route2, saving.j) and not (
#                 saving.i.isVisited and saving.j.isVisited) and saving.i.route != saving.j.route):
#             if (route1.demand + route2.demand <= model.capacity):
#                 position1 = CheckEdgeNodePosition(route1, saving.i)
#                 position2 = CheckEdgeNodePosition(route2, saving.j)
#                 if position1 == 2 and position2 == 1:
#                     route = ConnectRoutes(route1, route2)
#                 elif position1 == 2 and position2 == 2:
#                     route2.nodes.reverse()
#                     route = ConnectRoutes(route1, route2)
#                 elif position1 == 1 and position2 == 1:
#                     route1.nodes.reverse()
#                     route = ConnectRoutes(route1, route2)
#                 elif position1 == 1 and position2 == 2:
#                     route = ConnectRoutes(route2, route1)
#                 UpdateRouteNodes(route)
#
#     finalRoutes = []
#     for i in range(1, len(nodes)):
#         if nodes[i].route.isAdded == False:
#             finalRoutes.append(nodes[i].route)
#             nodes[i].route.isAdded = True
#
#     coords = []
#     solutionDist = 0
#     for route in finalRoutes:
#         path = []
#         solutionDist += route.distance
#         for node in route.nodes:
#             path.append([node.x, node.y])
#         coords.append(path)
#
#     print(coords)
#     print(solutionDist)


from model import *


class Solution:
    def __init__(self):
        self.cost = 0.0
        self.routes = []


class Saving:
    def __init__(self, n1, n2, sav):
        self.n1 = n1
        self.n2 = n2
        self.score = sav






    # def ReportSolution(self, sol):
    #     for i in range(0, len(sol.routes)):
    #         rt = sol.routes[i]
    #         for j in range(0, len(rt.sequenceOfNodes)):
    #             print(rt.sequenceOfNodes[j].ID, end=' ')
    #         print(rt.cost)
    #     SolDrawer.draw('MinIns', self.sol, self.allNodes)
    #     print(self.sol.cost)













