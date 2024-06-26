class Network:
    def __init__(self, edges):
        self.edges = edges
        self.fair_prices = {1: 0}

    def update_in_basis(self):
        for edge, attrs in self.edges.items():
            if attrs['flow'] == 0:
                attrs['in_basis'] = False
            elif attrs['flow'] == attrs['upper']:
                attrs['in_basis'] = False
            else:
                attrs['in_basis'] = True

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

    def print_fair_prices(self):
        print("Fair Prices:")
        for node, price in sorted(self.fair_prices.items()):
            print(f"Node {node}: {price}")

    def calculate_reduced_costs(self):
        reduced_costs = {}
        for (i, j), attrs in self.edges.items():
            if not attrs['in_basis']:
                reduced_costs[(i, j)] = attrs['cost'] + self.fair_prices[i] - self.fair_prices[j]
        return reduced_costs


    def print_reduced_costs(self):
        reduced_costs = self.calculate_reduced_costs()
        null_flow_costs = {edge: cost for edge, cost in reduced_costs.items() if self.edges[edge]['flow'] == 0}
        saturated_flow_costs = {edge: cost for edge, cost in reduced_costs.items() if self.edges[edge]['flow'] == self.edges[edge]['upper']}

        print("\nReduced Costs for Non-Basis Edges (Null Flow):")
        for edge, cost in sorted(null_flow_costs.items()):
            print(f"Edge {edge}: {cost}")

        print("\nReduced Costs for Non-Basis Edges (Saturated Flow):")
        for edge, cost in sorted(saturated_flow_costs.items()):
            print(f"Edge {edge}: {cost}")

    def find_highest_reduced_cost_edge(self):
        reduced_costs = self.calculate_reduced_costs()
        highest_positive_edge = None
        highest_negative_edge = None
        highest_positive = float('-inf')
        highest_negative = float('inf')

        for (i, j), cost in reduced_costs.items():
            if self.edges[(i, j)]['flow'] == self.edges[(i, j)]['upper'] and cost > 0:
                if cost > highest_positive:
                    highest_positive = cost
                    highest_positive_edge = (i, j)
            elif self.edges[(i, j)]['flow'] == 0 and cost < 0:
                if cost < highest_negative:
                    highest_negative = cost
                    highest_negative_edge = (i, j)

        # Vergleich Absolutbeträge
        if highest_positive_edge and highest_negative_edge:
            if abs(highest_positive) >= abs(highest_negative):
                return highest_positive_edge, highest_positive, 'saturated'
            else:
                return highest_negative_edge, highest_negative, 'null'
        elif highest_positive_edge:
            return highest_positive_edge, highest_positive, 'saturated'
        elif highest_negative_edge:
            return highest_negative_edge, highest_negative, 'null'
        else:
            return None, 0, None

    def find_cycle(self, start_edge):
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

    def determine_t_and_update_flows(self, forward_edges, backward_edges, edge_type):
        t_values = []

        if edge_type == 'null':
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

        if edge_type == 'null':
            for edge in forward_edges:
                self.edges[edge]['flow'] += t
            for edge in backward_edges:
                self.edges[edge]['flow'] -= t
        else:
            for edge in forward_edges:
                self.edges[edge]['flow'] -= t
            for edge in backward_edges:
                self.edges[edge]['flow'] += t

        return t

    def calculate_total_cost(self):
        total_cost = 0
        for (i, j), attrs in self.edges.items():
            if attrs['flow'] > 0:
                total_cost += attrs['flow'] * attrs['cost']
        return total_cost

    def iterate(self):
        self.update_in_basis()
        self.calculate_fair_prices()
        self.print_fair_prices()
        self.print_reduced_costs()
        highest_reduced_cost_edge, highest_reduced_cost, edge_type = self.find_highest_reduced_cost_edge()
        print(f"\nEdge with the highest reduced cost (in absolute value): {highest_reduced_cost_edge}")
        print(f"Highest reduced cost value: {highest_reduced_cost} (Edge type: {edge_type})")

        if edge_type:
            cycle = self.find_cycle(highest_reduced_cost_edge)
            cycle_nodes = self.get_cycle_nodes(cycle)
            print(f"\nCycle including the edge {highest_reduced_cost_edge}: {cycle}")
            print(f"Cycle nodes: {' -> '.join(map(str, cycle_nodes))}")

            analyzer = CycleAnalyzer(cycle_nodes, cycle)
            flow_changes = analyzer.analyze_cycle()
            print(f"Forward edges: {flow_changes['forward']}")
            print(f"Backward edges: {flow_changes['backward']}")

            t = self.determine_t_and_update_flows(flow_changes['forward'], flow_changes['backward'], edge_type)
            print(f"\nFlow changes applied with t = {t}:")

            updated_edges = {}
            for edge, attrs in self.edges.items():
                updated_edges[edge] = {'cost': attrs['cost'], 'flow': attrs['flow'], 'in_basis': attrs['in_basis'], 'upper': attrs['upper']}

            # aktualisierte Kanten in nem Format, das für die nächste Iteration geeignet ist.
            print("\nUpdated edges:")
            for edge, attrs in updated_edges.items():
                print(f"    {edge}: {{'cost': {attrs['cost']}, 'flow': {attrs['flow']}, 'in_basis': {attrs['in_basis']}, 'upper': {attrs['upper']}}},")

            total_cost = self.calculate_total_cost()
            print(f"\nTotal cost: {total_cost}")

            return updated_edges

        else:
            return None

class CycleAnalyzer:
    def __init__(self, cycle, cycle_edges):
        self.cycle = cycle
        self.cycle_edges = cycle_edges

    def analyze_cycle(self):
        flow_changes = {'forward': [], 'backward': []}
        for edge in self.cycle_edges:
            if edge in self.get_edges_from_cycle():
                flow_changes['forward'].append(edge)
            else:
                flow_changes['backward'].append(edge)
        return flow_changes

    def get_edges_from_cycle(self):
        edges = []
        num_nodes = len(self.cycle)
        for i in range(num_nodes):
            edge = (self.cycle[i], self.cycle[(i + 1) % num_nodes])
            edges.append(edge)
        return edges

if __name__ == "__main__":
    initial_edges = {
            (1, 2): {'cost': 3, 'flow': 0, 'in_basis': False, 'upper': 2},
            (1, 3): {'cost': 5, 'flow': 0, 'in_basis': False, 'upper': 10},
            (1, 5): {'cost': 1, 'flow': 9, 'in_basis': True, 'upper': 10},
            (2, 3): {'cost': 1, 'flow': 6, 'in_basis': False, 'upper': 6},
            (4, 2): {'cost': 4, 'flow': 4, 'in_basis': True, 'upper': 8},
            (4, 3): {'cost': 1, 'flow': 3, 'in_basis': True, 'upper': 9},
            (5, 3): {'cost': 6, 'flow': 8, 'in_basis': True, 'upper': 9},
            (5, 4): {'cost': 1, 'flow': 0, 'in_basis': False, 'upper': 10},
            (5, 6): {'cost': 1, 'flow': 6, 'in_basis': False, 'upper': 6},
            (6, 2): {'cost': 1, 'flow': 6, 'in_basis': True, 'upper': 7},
            (6, 4): {'cost': 1, 'flow': 8, 'in_basis': False, 'upper': 8},
        }
    network = Network(initial_edges)

    # Anzahl der Iterationen
    for i in range(10):
        print(f"\nIteration {i+1}")
        updated_edges = network.iterate()
        if updated_edges:
            network = Network(updated_edges)
        else:
            break
