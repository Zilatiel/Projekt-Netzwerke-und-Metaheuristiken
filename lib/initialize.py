def initialize_network(w):
    # Create a copy of arcs2 
    arcs = [arc.copy() for arc in arcs2]

    # Set all costs in arcs to zero
    for arc in arcs:
      arc["cost"] = 0

    new_arcs = []
    existing_arcs = []

    for node, data in nodes.items():
        if node == w:
            continue
        if data["demand"] < 0:
            arc = next((arc for arc in arcs if arc["from"] == node and arc["to"] == w), None)
            if arc:
                arc["cost"] = 0
                existing_arcs.append(arc)
            else:
                new_arcs.append({"from": node, "to": w, "cost": 1, "lower_bound": 0, "upper_bound": 1000})
        else:
            arc = next((arc for arc in arcs if arc["from"] == w and arc["to"] == node), None)
            if arc:
                arc["cost"] = 0
                existing_arcs.append(arc)
            else:
                new_arcs.append({"from": w, "to": node, "cost": 1, "lower_bound": 0, "upper_bound": 1000})

    all_arcs = existing_arcs + new_arcs
    assert len(all_arcs) == len(nodes) - 1

    flow_distribution = {node: 0 for node in nodes}
    for node, data in nodes.items():
        if node != w:
            flow_distribution[node] = data["demand"]
    flow_distribution[w] = -sum(flow_distribution[node] for node in nodes if node != w)

    for arc in all_arcs:
        if arc["to"] == w:
            arc["flow"] = -flow_distribution[arc["from"]]
        elif arc["from"] == w:
            arc["flow"] = flow_distribution[arc["to"]]
        arc["in_basis"] = True

    initial_tree_edges = {(arc["from"], arc["to"]) for arc in all_arcs}

    for arc in arcs:
        if (arc["from"], arc["to"]) not in initial_tree_edges:
            arc["flow"] = 0
            arc["in_basis"] = False
            all_arcs.append(arc)

    edges_dict = {}
    initial_costs = {}
    for arc in all_arcs:
        edges_dict[(int(arc["from"]), int(arc["to"]))] = {
            'cost': arc['cost'],
            'flow': arc['flow'],
            'in_basis': arc['in_basis'],
            'upper': arc['upper_bound']
        }
        initial_costs[(int(arc["from"]), int(arc["to"]))] = arc['cost']

    return edges_dict, initial_costs
