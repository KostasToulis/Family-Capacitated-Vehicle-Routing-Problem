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


def find_position(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target+1:
            left = mid + 1
        else:
            right = mid - 1
    return left if left < len(arr) else -1


def create_nodes_families(model):
    families = []
    nodes = []
    for i in range(len(model.fam_members)):
        family = Family(i, [], model.fam_dem[i], model.fam_req[i])
        families.append(family)

    fam_index = []
    c = 0
    for i in model.fam_members:
        fam_index.append(i + c)
        c = i

    for i in range(len(model.cost_matrix)):
        family = find_position(fam_index, i)
        node = Node(i, family, model.cost_matrix[i], families[family].demand)
        nodes.append(node)

    for node in nodes:
        families[node.family].nodes.append(node)

    return families, nodes