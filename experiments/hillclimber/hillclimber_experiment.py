from code.algorithms import hillclimber as hc
from code.algorithms import randomise

import matplotlib.pyplot as plt
import csv
import copy
from statistics import mean 


def hillclimb(graph, transmitters):
    random_graph = randomise.random_reassignment(copy.deepcopy(graph), transmitters.get_scheme(1))
    climber = hc.HillClimber(random_graph, transmitters.get_scheme(1))

    print("Running Hill Climber...")
    with open("results/hillclimber/hillclimber.csv", 'w', newline='') as output_file:
        result_writer = csv.writer(output_file, delimiter=',')
            
        for _ in range(0, 1000):
            climber.run(1)
            result_writer.writerow((climber.graph.calculate_value(), climber.graph.to_json()))


def hillclimb_continue(graph, transmitters, data):
    with open(data, 'r') as input_file:
        result_reader = csv.reader(input_file, delimiter=',')
        *_, last = result_reader
        json_data = last[1]

    graph.from_json(json_data, transmitters.get_scheme(1))
    climber = hc.HillClimber(graph, transmitters.get_scheme(1))

    print("Continueing Hill Climber...")
    with open(data, 'a', newline='') as output_file:
        result_writer = csv.writer(output_file, delimiter=',')
            
        for _ in range(0, 1000):
            climber.run(1)
            result_writer.writerow((climber.graph.calculate_value(), climber.graph.to_json()))

def hillclimber_averages(graph, transmitters):
    results = []
    for i in range(0, 100):
        result = []
        random_graph = randomise.random_reassignment(copy.deepcopy(graph), transmitters.get_scheme(1))
        climber = hc.HillClimber(random_graph, transmitters.get_scheme(1))
        
        print(f"Running Hill Climber: {i}")

        for _ in range(0, 1000):
                climber.run(1)
                result.append(climber.graph.calculate_value())

        results.append(result)

    values = []
    for iteration in zip(*results):
        values.append((mean(iteration), min(iteration), max(iteration)))

    with open("results/hillclimber/hillclimber_averages.csv", 'w', newline='') as output_file:
        result_writer = csv.writer(output_file, delimiter=',')
        for value in values:
            result_writer.writerow(value)

def hillclimber_xopt_comparison(graph, transmitters):
    for n in range(1, 6):
        results = []
        for i in range(0, 100):
            result = []
            random_graph = randomise.random_reassignment(copy.deepcopy(graph), transmitters.get_scheme(1))
            climber = hc.HillClimber(random_graph, transmitters.get_scheme(1))
            
            print(f"Running Hill Climber: {i}")

            for _ in range(0, 500):
                climber.run(1, mutate_nodes_number=n)
                result.append(climber.graph.calculate_value())

            results.append(result)

        values = []
        for iteration in zip(*results):
            values.append((mean(iteration), min(iteration), max(iteration)))

        results.append(values)
    
        with open(f"results/hillclimber/hillclimber_xopt_{n}.csv", 'w', newline='') as output_file:
            result_writer = csv.writer(output_file, delimiter=',')
            for value in values:
                result_writer.writerow(value)
        
            
def hillclimb_graph():
    fig, ax = plt.subplots()
    with open("results/hillclimber/hillclimber.csv", 'r') as input_file:
        result_reader = csv.reader(input_file, delimiter=',')
        results = [int(value) for value, _ in result_reader]

    ax.plot(results, label='HillClimber')
    ax.set_title('Hill Climber')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Total Costs')
    fig.savefig("results/hillclimber/single_run.png")


def hillclimber_averages_graph():
    fig, ax = plt.subplots()
    with open("results/hillclimber/hillclimber_averages.csv", 'r') as input_file:
        result_reader = csv.reader(input_file, delimiter=',')
        results = [float(value) for value, _, _ in result_reader]

    ax.plot(results, label='HillClimber')
    ax.set_title('Hill Climbers (n=100)')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Average Total Costs')
    fig.savefig("results/hillclimber/hillclimber_averages.png")


def hillclimber_averages_filled_graph():
    fig, ax = plt.subplots()
    with open("results/hillclimber/hillclimber_averages.csv", 'r') as input_file:
        result_reader = csv.reader(input_file, delimiter=',')
        results = [(float(average), int(minimum), int(maximum)) for average, minimum, maximum in result_reader]
        averages = [average for average, minimum, maximum in results]
        minima = [minimum for average, minimum, maximum in results]
        maxima = [maximum for average, minimum, maximum in results]

    ax.plot(averages, label='HillClimber')
    ax.fill_between(range(0, len(averages)), minima, maxima, alpha=0.5, linewidth=0)
    ax.set_title('Hill Climbers (n=100)')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Average Total Costs')
    fig.savefig("results/hillclimber/hillclimber_averages_filled.png")

def hillclimber_xopt_comparison_graph():
    fig, ax = plt.subplots()
    results = []
    for n in range(1, 6):
        with open(f"results/hillclimber/hillclimber_xopt_{n}.csv", 'r') as input_file:
            result_reader = csv.reader(input_file, delimiter=',')
            results.append([float(value) for value, _, _ in result_reader])

    for index, result in enumerate(results):
        ax.plot(result, label=f'X-Opt {index + 1}')

    ax.legend(loc='upper right')
    ax.set_title('Hill Climber X-Opts (n=100)')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Total Costs')
    fig.savefig("results/hillclimber/hillclimber_xopt_comparison.png")