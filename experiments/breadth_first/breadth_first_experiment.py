from code.algorithms import breadth_first as bf
import matplotlib.pyplot as plt
import csv
import json


def breadth_first(graph, transmitters):
    breadth = bf.BreadthFirst(graph, transmitters.get_scheme(1)[0:4])
    breadth.run()
    
    with open("results/breadth_first/breadth_first.json", 'w', newline='') as output_file:
        json.dump({
            'visited_state_count': breadth.visited_state_count,
            'max_states_size': breadth.max_states_size,
            'solution_count': breadth.solution_count,
            'states_sizes': breadth.states_sizes,
            'value': breadth.graph.calculate_value(),
            'solution': breadth.graph.to_json()
        }, output_file)


def breadth_first_memory_graph():
    fig, ax = plt.subplots(figsize=(8, 4))
    with open("results/breadth_first/breadth_first.json", 'r') as input_file:
        result = json.load(input_file)

    ax.set_title('Breadth First Memory Growth')

    ax.plot(result['states_sizes'], label='States')
    ax.set_xlabel('Considered States')
    ax.set_ylabel('Number of States')   
    fig.savefig("results/breadth_first/breadth_first_memory.png")


def best_first(graph, transmitters):
    breadth = bf.BestFirst(graph, transmitters.get_scheme(1)[0:4])
    breadth.run()
    
    with open("results/breadth_first/best_first.json", 'w', newline='') as output_file:
        json.dump({
            'visited_state_count': breadth.visited_state_count,
            'max_states_size': breadth.max_states_size,
            'solution_count': breadth.solution_count,
            'states_sizes': breadth.states_sizes,
            'value': breadth.graph.calculate_value(),
            'solution': breadth.graph.to_json()
        }, output_file)

def breadth_first_table():
    fig, ax = plt.subplots(figsize=(8, 4))

    with open("results/breadth_first/breadth_first.json", 'r') as input_file:
        result = json.load(input_file)
    
    cells = [str(result['visited_state_count']), str(result['max_states_size']), str(result['solution_count']), str(result['value'])]

    ax.set_title('Breadth First Overview')
    ax.set_axis_off()

    ax.table(
        colLabels=['Visited State Count', 'Max States Size', 'Solution Count', 'Objective Value'],
        rowLabels=["DepthFirst"],
        cellText=[cells],
        loc='upper left',
    )
    fig.tight_layout()
    fig.savefig("results/breadth_first/breadth_first.png")


def constructive_comparison():
    fig, ax = plt.subplots(figsize=(8, 4))
    results = []
    with open("results/depth_first/depth_first.json", 'r') as input_file:
        result = json.load(input_file)
        results.append([str(result['visited_state_count']), str(result['max_states_size']), str(result['solution_count']), str(result['value'])])
    
    with open("results/depth_first/branchandbound.json", 'r') as input_file:
        result = json.load(input_file)
        results.append([str(result['visited_state_count']), str(result['max_states_size']), str(result['solution_count']), str(result['value'])])
    
    with open("results/breadth_first/breadth_first.json", 'r') as input_file:
        result = json.load(input_file)
        results.append([str(result['visited_state_count']), str(result['max_states_size']), str(result['solution_count']), str(result['value'])])

    with open("results/breadth_first/best_first.json", 'r') as input_file:
        result = json.load(input_file)
        results.append([str(result['visited_state_count']), str(result['max_states_size']), str(result['solution_count']), str(result['value'])])
    
    ax.set_title('Constructive Overview')
    ax.set_axis_off()

    ax.table(
        colLabels=['Visited State Count', 'Max States Size', 'Solution Count', 'Objective Value'],
        rowLabels=["DepthFirst", "BranchAndBound", "BreadthFirst", "BestFirst"],
        cellText=results,
        loc='upper left',
    )
    fig.tight_layout()
    fig.savefig("results/breadth_first/comparison.png")
    fig.savefig("results/depth_first/comparison.png")

def breadth_first_memory_comparison():
    fig, ax = plt.subplots(figsize=(8, 4))
    with open("results/breadth_first/breadth_first.json", 'r') as input_file:
        breadth_result = json.load(input_file)
    
    with open("results/breadth_first/best_first.json", 'r') as input_file:
        best_result = json.load(input_file)

    ax.set_title('Breadth First Memory Comparison')

    ax.plot(breadth_result['states_sizes'], label='BreadthFirst')
    ax.plot(best_result['states_sizes'], label='BestFirst')
    ax.legend(loc='upper right')

    ax.set_xlabel('Considered States')
    ax.set_ylabel('Number of States')   
    fig.savefig("results/breadth_first/breadth_first_memory_comparison.png")

def constructive_memory_comparison():
    fig, ax = plt.subplots(figsize=(8, 4))
    with open("results/breadth_first/breadth_first.json", 'r') as input_file:
        breadth_result = json.load(input_file)
    
    with open("results/depth_first/depth_first.json", 'r') as input_file:
        depth_result = json.load(input_file)

    ax.set_title('Breadth First Memory Growth')

    ax.plot(breadth_result['states_sizes'], label='States')
    ax.plot(depth_result['states_sizes'], label='States')

    ax.set_xlabel('Considered States')
    ax.set_ylabel('Number of States')   
    fig.savefig("results/breadth_first/memory_comparison.png")