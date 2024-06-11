#import random

if __name__ == "__main__":
    #load_data('Data/chvatal_small.json')
    
    open('Data/chvatal_small.json', 'r') as file
    data = json.load(file)
    nodes = data['nodes']
    arcs2 = data['arcs']

    max_iterations = 50
    final_edges = None

    while True:
        #w = random.choice(list(nodes.keys()))
        w = "1"
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
