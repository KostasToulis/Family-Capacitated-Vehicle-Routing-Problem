from setup import load_model
from solver import selection_part

model = load_model('instances/fcvrp_A034-02f_3_1_2.txt')
candidate_nodes = selection_part(model)
print(candidate_nodes)
