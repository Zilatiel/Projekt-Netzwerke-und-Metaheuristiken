import json
# Datei öffnen und lesen
with open('chvatal_small.json', 'r') as file:
    data = json.load(file)


nodes = data["nodes"]
arcs2 = data["arcs"]

# Create a copy of arcs2
arcs = [arc.copy() for arc in arcs2]

# Set all costs in arcs to zero
for arc in arcs:
    arc["cost"] = 0

def initialize_network(w):
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

class Network:
    def __init__(self, edges, initial_costs):
        self.edges = edges
        self.initial_costs = initial_costs
        self.fair_prices = {2: 0}

    def update_edge_costs(self):
        for (i, j), attrs in self.edges.items():
            if attrs['flow'] > attrs['upper']:
                self.edges[(i, j)]['cost'] = 1000
            else:
                self.edges[(i, j)]['cost'] = self.initial_costs[(i, j)]

    def calculate_fair_prices(self):
        updated = True
        while updated:
            updated = False
            for (i, j), attrs in self.edges.items():
                if attrs['in_basis']:
                    if i in self.fair_prices and j not in self.fair_prices:
                        self.fair_prices[j] = self.fair_prices[i] + attrs['cost']
                        updated = True
                    elif j in self.fair_prices and i not in self.fair_prices:
                        self.fair_prices[i] = self.fair_prices[j] - attrs['cost']
                        updated = True
        for node in set([i for i, _ in self.edges.keys()] + [j for _, j in self.edges.keys()]):
            if node not in self.fair_prices:
                self.fair_prices[node] = 0

    def calculate_reduced_costs(self):
        reduced_costs = {}
        for (i, j), attrs in self.edges.items():
            if not attrs['in_basis']:
                reduced_costs[(i, j)] = attrs['cost'] + self.fair_prices[i] - self.fair_prices[j]
        return reduced_costs

    def print_fair_prices(self):
        print("Fair Prices:")
        for node, price in sorted(self.fair_prices.items()):
            print(f"Node {node}: {price}")

    def print_reduced_costs(self):
        reduced_costs = self.calculate_reduced_costs()
        print("\nReduced Costs for Non-Basis Edges:")
        for edge, cost in sorted(reduced_costs.items()):
            print(f"Edge {edge}: {cost}")

    def print_basis_solution(self, iteration):
        print(f"\nBasis Solution at Iteration {iteration}:")
        for (i, j), attrs in self.edges.items():
            if attrs['in_basis']:
                print(f"Edge {(i, j)}: Flow {attrs['flow']}, Cost {attrs['cost']}")

    def find_highest_reduced_cost_edge(self):
        reduced_costs = self.calculate_reduced_costs()
        highest_edge = None
        highest_value = float('-inf')

        for (i, j), cost in reduced_costs.items():
            if self.edges[(i, j)]['flow'] == 0 and cost < 0:
                if abs(cost) > highest_value:
                    highest_value = abs(cost)
                    highest_edge = (i, j)
            elif self.edges[(i, j)]['flow'] == self.edges[(i, j)]['upper'] and cost > 0:
                if abs(cost) > highest_value:
                    highest_value = abs(cost)
                    highest_edge = (i, j)

        return highest_edge, highest_value

    def find_cycle(self, start_edge, reverse=False):
        def dfs(node, target, visited, path):
            if node == target and path:
                return path
            visited.add(node)
            for (i, j) in self.edges:
                if (i == node or j == node) and self.edges[(i, j)]['in_basis']:
                    neighbor = j if i == node else i
                    if neighbor not in visited:
                        result = dfs(neighbor, target, visited, path + [(i, j)])
                        if result:
                            return result
            visited.remove(node)
            return None

        start_node = start_edge[0]
        end_node = start_edge[1]
        cycle = dfs(end_node, start_node, set(), [start_edge])
        if reverse and cycle:
            cycle.reverse()
        return cycle

    def get_cycle_nodes(self, cycle):
        nodes = [cycle[0][0]]
        for edge in cycle:
            nodes.append(edge[1] if edge[0] == nodes[-1] else edge[0])
        return nodes

    def analyze_cycle(self, cycle):
        cycle_nodes = self.get_cycle_nodes(cycle)
        flow_changes = {'forward': [], 'backward': []}
        for edge in cycle:
            if self.is_forward_edge(edge, cycle_nodes):
                flow_changes['forward'].append(edge)
            else:
                flow_changes['backward'].append(edge)
        return flow_changes

    def is_forward_edge(self, edge, cycle_nodes):
        for i in range(len(cycle_nodes) - 1):
            if edge == (cycle_nodes[i], cycle_nodes[i + 1]):
                return True
            if edge == (cycle_nodes[i + 1], cycle_nodes[i]):
                return False
        if edge == (cycle_nodes[-1], cycle_nodes[0]):
            return True
        if edge == (cycle_nodes[0], cycle_nodes[-1]):
            return False
        return False

    def determine_t_and_update_flows(self, forward_edges, backward_edges, highest_reduced_cost_edge, reverse=False):
        t_values = []
        if not reverse:
            for edge in forward_edges:
                t_values.append(self.edges[edge]['upper'] - self.edges[edge]['flow'])
            for edge in backward_edges:
                t_values.append(self.edges[edge]['flow'])
        else:
            for edge in forward_edges:
                t_values.append(self.edges[edge]['flow'])
            for edge in backward_edges:
                t_values.append(self.edges[edge]['upper'] - self.edges[edge]['flow'])

        t = min(t_values)

        if t == 0:
            zero_flow_edges = [edge for edge in backward_edges if self.edges[edge]['flow'] == 0]
            saturated_edges = [edge for edge in forward_edges if self.edges[edge]['flow'] == self.edges[edge]['upper']]
            if zero_flow_edges:
                # Ensure that the edge with zero flow and highest costs leaves the basis
                highest_cost_zero_flow_edge = max(zero_flow_edges, key=lambda e: self.edges[e]['cost'])
                self.edges[highest_cost_zero_flow_edge]['in_basis'] = False
                self.edges[highest_reduced_cost_edge]['in_basis'] = True
                return t
            if saturated_edges:
                # Ensure that the edge with saturated flow and highest reduced cost leaves the basis
                highest_saturated_edge = max(saturated_edges, key=lambda e: self.edges[e]['cost'])
                self.edges[highest_saturated_edge]['in_basis'] = False
                self.edges[highest_reduced_cost_edge]['in_basis'] = True
                return t

        if reverse:
            for edge in forward_edges:
                self.edges[edge]['flow'] -= t
            for edge in backward_edges:
                self.edges[edge]['flow'] += t
        else:
            for edge in forward_edges:
                self.edges[edge]['flow'] += t
            for edge in backward_edges:
                self.edges[edge]['flow'] -= t

        edges_to_consider = []
        for edge in forward_edges + backward_edges:
            if self.edges[edge]['flow'] == 0 or self.edges[edge]['flow'] == self.edges[edge]['upper']:
                edges_to_consider.append(edge)
            else:
                self.edges[edge]['in_basis'] = True

        if edges_to_consider:
            # Handle the specific case
            zero_flow_edges = [edge for edge in edges_to_consider if self.edges[edge]['flow'] == 0]
            upper_bound_edges = [edge for edge in edges_to_consider if self.edges[edge]['flow'] == self.edges[edge]['upper']]

            if zero_flow_edges and upper_bound_edges:
                # Remove the zero flow edge from the basis
                zero_flow_edge = zero_flow_edges[0]  # There's typically only one
                self.edges[zero_flow_edge]['in_basis'] = False
                # Keep the upper bound edge in the basis
                for edge in upper_bound_edges:
                    self.edges[edge]['in_basis'] = True
            else:
                # Remove only the edge with the highest cost
                max_cost_edge = max(edges_to_consider, key=lambda e: self.edges[e]['cost'])
                self.edges[max_cost_edge]['in_basis'] = False

        return t

    def calculate_total_cost(self):
        total_cost = 0
        for (i, j), attrs in self.edges.items():
            if attrs['flow'] > 0:
                total_cost += attrs['flow'] * attrs['cost']
        return total_cost

    def iterate(self, iteration):
        self.update_edge_costs()
        self.calculate_fair_prices()
        highest_reduced_cost_edge, highest_reduced_cost = self.find_highest_reduced_cost_edge()

        if highest_reduced_cost_edge:
            if self.edges[highest_reduced_cost_edge]['flow'] == self.edges[highest_reduced_cost_edge]['upper']:
                cycle = self.find_cycle(highest_reduced_cost_edge, reverse=True)
            else:
                cycle = self.find_cycle(highest_reduced_cost_edge)
            if cycle:
                flow_changes = self.analyze_cycle(cycle)
                reverse = self.edges[highest_reduced_cost_edge]['flow'] == self.edges[highest_reduced_cost_edge]['upper']
                t = self.determine_t_and_update_flows(flow_changes['forward'], flow_changes['backward'], highest_reduced_cost_edge, reverse)
                self.print_basis_solution(iteration)
                total_cost = self.calculate_total_cost()
                print(f"\nTotal cost: {total_cost}")
                return self.edges
        self.print_basis_solution(iteration)

        total_cost = self.calculate_total_cost()
        print(f"\nTotal cost: {total_cost}")

        return None

if __name__ == "__main__":
    max_iterations = 50
    final_edges = None

    while True:
        #w = random.choice(list(nodes.keys()))
        w = "2"
        print(f"Starting with node w = {w}")
        edges_input, initial_costs = initialize_network(w)

        network = Network(edges_input, initial_costs)
        iteration = 0

        while iteration < max_iterations:
            iteration += 1
            updated_edges = network.iterate(iteration)
            if updated_edges:
                final_edges = updated_edges
                network = Network(updated_edges, initial_costs)
            else:
                break

        if iteration < max_iterations:
            break
        else:
            print("Exceeded max iterations, choosing a new w.")

    if final_edges is not None:
        initial_final_edges = {edge: attrs for edge, attrs in final_edges.items() if attrs['cost'] != 1}

        updated_costs = {(int(arc['from']), int(arc['to'])): arc['cost'] for arc in arcs2}

        for edge, new_cost in updated_costs.items():
            if edge in initial_final_edges:
                initial_final_edges[edge]['cost'] = new_cost

        print("\nFinal Edges with Updated Costs:")
        for edge, attrs in initial_final_edges.items():
            print(f"    {edge}: {{'cost': {attrs['cost']}, 'flow': {attrs['flow']}, 'in_basis': {attrs['in_basis']}, 'upper': {attrs['upper']}}},")

        # Run again with updated costs
        network = Network(initial_final_edges, updated_costs)
        iteration = 0
        final_edges = None

        while iteration < max_iterations:
            iteration += 1
            updated_edges = network.iterate(iteration)
            if updated_edges:
                final_edges = updated_edges
                network = Network(updated_edges, updated_costs)
            else:
                break

        if iteration < max_iterations and iteration > 1:
            print("\nFinal Edges after second iteration process:")
            for edge, attrs in final_edges.items():
                print(f"    {edge}: {{'cost': {attrs['cost']}, 'flow': {attrs['flow']}, 'in_basis': {attrs['in_basis']}, 'upper': {attrs['upper']}}},")
        elif iteration < max_iterations and iteration == 1:
            for edge, attrs in initial_final_edges.items():
                print(f"    {edge}: {{'cost': {attrs['cost']}, 'flow': {attrs['flow']}, 'in_basis': {attrs['in_basis']}, 'upper': {attrs['upper']}}},")
        else:
            print("Exceeded max iterations during the second run.")

    elif final_edges is None and iteration == 1:
      initial_final_edges = {edge: attrs for edge, attrs in edges_input.items() if attrs['cost'] != 1}

      updated_costs = {(int(arc['from']), int(arc['to'])): arc['cost'] for arc in arcs2}

      for edge, new_cost in updated_costs.items():
          if edge in initial_final_edges:
              initial_final_edges[edge]['cost'] = new_cost

      # Print the final edges with updated costs
      print("\nFinal Edges with Updated Costs:")
      for edge, attrs in initial_final_edges.items():
          print(f"    {edge}: {{'cost': {attrs['cost']}, 'flow': {attrs['flow']}, 'in_basis': {attrs['in_basis']}, 'upper': {attrs['upper']}}},")

      # Run again with updated costs
      network = Network(initial_final_edges, updated_costs)
      iteration = 0
      final_edges = None

      while iteration < max_iterations:
          iteration += 1
          updated_edges = network.iterate(iteration)
          if updated_edges:
              final_edges = updated_edges
              network = Network(updated_edges, updated_costs)
          else:
              break

      if iteration < max_iterations and iteration > 1:
          print("\nFinal Edges after second iteration process:")
          for edge, attrs in final_edges.items():
              print(f"    {edge}: {{'cost': {attrs['cost']}, 'flow': {attrs['flow']}, 'in_basis': {attrs['in_basis']}, 'upper': {attrs['upper']}}},")
      elif iteration < max_iterations and iteration == 1:
          for edge, attrs in initial_final_edges.items():
              print(f"    {edge}: {{'cost': {attrs['cost']}, 'flow': {attrs['flow']}, 'in_basis': {attrs['in_basis']}, 'upper': {attrs['upper']}}},")
      else:
          print("Exceeded max iterations during the second run.")

    else:
        print("No valid final edges to update.")



