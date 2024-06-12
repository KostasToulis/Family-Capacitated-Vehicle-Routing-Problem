from setup import load_model, create_nodes_families

model = load_model('instances/fcvrp_A034-02f_3_1_2.txt')
families, nodes = create_nodes_families(model)
print(model.num_nodes)