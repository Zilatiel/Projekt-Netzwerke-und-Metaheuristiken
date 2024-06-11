import gurobipy as gp
from gurobipy import GRB

def solve_min_cost_flow(nodes, arcs):
    # Create a new model
    m = gp.Model("min_cost_flow")

    # Create variables
    flows = {}
    for arc in arcs:
        flows[(arc['from'], arc['to'])] = m.addVar(lb=arc['lower_bound'], ub=arc['upper_bound'], vtype=gp.GRB.CONTINUOUS,
                                                   name=f"flow_{arc['from']}_{arc['to']}")

    # Set objective
    m.setObjective(gp.quicksum(arc['cost'] * flows[(arc['from'], arc['to'])] for arc in arcs), sense=gp.GRB.MINIMIZE)

    # Add flow conservation constraints
    for node, data in nodes.items():
        inflow = gp.quicksum(flows[(arc['from'], arc['to'])] for arc in arcs if arc['to'] == node)
        outflow = gp.quicksum(flows[(arc['from'], arc['to'])] for arc in arcs if arc['from'] == node)
        m.addConstr(inflow - outflow == data['demand'], name=f"balance_{node}")

    # Optimize model
    m.optimize()

    # Extract solution
    if m.status == gp.GRB.OPTIMAL:
        solution_flows = {arc: var.x for arc, var in flows.items()}
        total_cost = sum(arc['cost'] * solution_flows[(arc['from'], arc['to'])] for arc in arcs)
        return solution_flows, total_cost
    else:
        print("No optimal solution found.")
        return None, None

# Beispielhafte Nutzung
nodes = {
    "1": {"demand": -9},
    "2": {"demand": 4},
    "3": {"demand": 17},
    "4": {"demand": 1},
    "5": {"demand": -5},
    "6": {"demand": -8}
}

arcs = [
    {"from": "1", "to": "2", "cost": 3, "lower_bound": 0, "upper_bound": 2},
    {"from": "1", "to": "3", "cost": 5, "lower_bound": 0, "upper_bound": 10},
    {"from": "1", "to": "5", "cost": 1, "lower_bound": 0, "upper_bound": 10},
    {"from": "2", "to": "3", "cost": 1, "lower_bound": 0, "upper_bound": 6},
    {"from": "4", "to": "2", "cost": 4, "lower_bound": 0, "upper_bound": 8},
    {"from": "4", "to": "3", "cost": 1, "lower_bound": 0, "upper_bound": 9},
    {"from": "5", "to": "3", "cost": 6, "lower_bound": 0, "upper_bound": 9},
    {"from": "5", "to": "4", "cost": 1, "lower_bound": 0, "upper_bound": 10},
    {"from": "5", "to": "6", "cost": 1, "lower_bound": 0, "upper_bound": 6},
    {"from": "6", "to": "2", "cost": 1, "lower_bound": 0, "upper_bound": 7},
    {"from": "6", "to": "4", "cost": 1, "lower_bound": 0, "upper_bound": 8}
]

solution, total_cost = solve_min_cost_flow(nodes, arcs)
if solution:
    print("Flussmengen auf den Kanten (Fluss > 0):")
    for arc, flow in solution.items():
        if flow > 0:
            print(f"Kante {arc}: Fluss {flow}")
    print(f"Anzahl der Kanten mit Fluss > 0: {len([flow for flow in solution.values() if flow > 0])}")
    print(f"Gesamtkosten des Netzwerks: {total_cost}")
