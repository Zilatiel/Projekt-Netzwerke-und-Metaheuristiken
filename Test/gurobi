import gurobipy as gp
from gurobipy import GRB
import time
import json

# Funktion zum Laden der JSON-Daten
def load_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data['nodes'], data['arcs']

# Beispiel: Lade die Daten aus der JSON-Datei
filename = 'Data/chvatal_small.json'  # Pfad zur JSON-Datei
nodes, arcs = load_data(filename)

# Starte den Timer
start_time = time.time()

# Erstelle ein Gurobi Modell
model = gp.Model("network_simplex")

# Verwende den dedizierten Netzwerk-Simplex-Löser
model.setParam('Method', -1)
model.setParam('NetworkAlg', 1)

# Erstelle Variablen für den Fluss auf jeder Kante
flow_vars = {}
for arc in arcs:
    flow_vars[(arc["from"], arc["to"])] = model.addVar(lb=arc["lower_bound"], ub=arc["upper_bound"], obj=arc["cost"], name=f"flow_{arc['from']}_{arc['to']}")

# Definiere die Nachfrage an jedem Knoten
demand = {node: data["demand"] for node, data in nodes.items()}

# Erstelle die Flussgleichungen für jeden Knoten
for node in nodes:
    inflow = gp.quicksum(flow_vars[(i, node)] for i, j in flow_vars if j == node)
    outflow = gp.quicksum(flow_vars[(node, j)] for i, j in flow_vars if i == node)
    model.addConstr(inflow - outflow == demand[node], name=f"node_{node}")

# Optimieren des Modells
model.optimize()

# Stoppe den Timer und berechne die Ausführungszeit
end_time = time.time()
execution_time = end_time - start_time

# Ausgabe der Ausführungszeit
print(f"Execution time: {execution_time} seconds")

# Ausgabe der Ergebnisse
if model.status == GRB.OPTIMAL:
    for arc in arcs:
        print(f"Flow on arc {arc['from']} -> {arc['to']}: {flow_vars[(arc['from'], arc['to'])].x}")
else:
    print("No optimal solution found")
