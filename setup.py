from model import Node, Model, Family


def load_model(file_name):
    model = Model()
    all_nodes = []
    all_lines = list(open(file_name, "r"))

    line_counter = 0

    # 1st line
    ln = all_lines[line_counter]
    no_spaces = ln.split()

    model.num_nodes = int(no_spaces[0])
    model.num_fam = int(no_spaces[1])
    model.num_req = int(no_spaces[2])
    model.capacity = int(no_spaces[3])
    model.vehicles = int(no_spaces[4])

    # 2nd line
    line_counter += 1
    ln = all_lines[line_counter]
    no_spaces = list(map(int, ln.split()))
    model.fam_members = no_spaces

    # 3rd line
    line_counter += 1
    ln = all_lines[line_counter]
    no_spaces = list(map(int, ln.split()))
    model.fam_req = no_spaces

    # 4th line
    line_counter += 1
    ln = all_lines[line_counter]
    no_spaces = list(map(int, ln.split()))
    model.fam_dem = no_spaces

    # 5th - end of file
    cost_matrix = []
    for i in range(model.num_nodes):
        line_counter += 1
        ln = all_lines[line_counter]
        no_spaces = list(map(int, ln.split()))
        cost_matrix.append(no_spaces)

    model.cost_matrix = cost_matrix
    return model


# def create_nodes_families(model):
#     families = []
#     nodes = []
#     c = 0
#     for i,fam in enumerate(model.fam_members):
#         costs = model.cost_matrix[c:fam+1]
#         families.append(Family())
#         for i,cost in enumerate(costs):
#             nodes.append(Node(i,,costs,))

