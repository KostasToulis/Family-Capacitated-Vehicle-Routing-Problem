from setup import load_model
from solver import Solver


model = load_model('instances/fcvrp_P-n20-k2_2_2_2.txt')
solver = Solver(model)
sol = solver.solve()
print(sol.cost)
