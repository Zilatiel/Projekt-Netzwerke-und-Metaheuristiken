class Network:
    def __init__(self, edges, initial_costs):
        self.edges = edges
        self.initial_costs = initial_costs
        self.fair_prices = {1: 0}

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
                zero_flow_edge = zero_flow_edges[0] 
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
