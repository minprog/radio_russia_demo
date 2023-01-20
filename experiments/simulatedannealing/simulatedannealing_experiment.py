from code.algorithms import simulatedannealing as sa
from code.algorithms import randomise

import matplotlib.pyplot as plt
import csv
import copy
from statistics import mean 


def simulateannealing(graph, transmitters):
    random_graph = randomise.random_reassignment(copy.deepcopy(graph), transmitters.get_scheme(1))
    simannealing = sa.SimulatedAnnealing(random_graph, transmitters.get_scheme(1))

    print("Running Simulated Annealing...")
    with open("results/simulatedannealing/simulatedannealing.csv", 'w', newline='') as output_file:
        result_writer = csv.writer(output_file, delimiter=',')
            
        for _ in range(0, 100):
            simannealing.run(1)
            result_writer.writerow((simannealing.graph.calculate_value(), simannealing.graph.to_json()))


def simulateannealing_continue(graph, transmitters, data):
    with open(data, 'r') as input_file:
        result_reader = csv.reader(input_file, delimiter=',')
        *_, last = result_reader
        json_data = last[1]

    graph.from_json(json_data, transmitters.get_scheme(1))
    simannealing = sa.SimulatedAnnealing(graph, transmitters.get_scheme(1))

    print("Continueing Simulated Annealing...")
    with open(data, 'a', newline='') as output_file:
        result_writer = csv.writer(output_file, delimiter=',')
            
        for _ in range(0, 100):
            simannealing.run(1)
            result_writer.writerow((simannealing.graph.calculate_value(), simannealing.graph.to_json()))

def simulatedannealing_averages(graph, transmitters):
    results = []
    for i in range(0, 100):
        result = []
        random_graph = randomise.random_reassignment(copy.deepcopy(graph), transmitters.get_scheme(1))
        simannealing = sa.SimulatedAnnealing(random_graph, transmitters.get_scheme(1))
        
        print(f"Running Annealing: {i}")

        for _ in range(0, 500):
                simannealing.run(1)
                result.append(simannealing.graph.calculate_value())

        results.append(result)

    values = []
    for iteration in zip(*results):
        values.append((mean(iteration), min(iteration), max(iteration)))

    with open("results/simulatedannealing/simulatedannealing_averages.csv", 'w', newline='') as output_file:
        result_writer = csv.writer(output_file, delimiter=',')
        for value in values:
            result_writer.writerow(value)

def simulatedannealing_temperature_comparisons(graph, transmitters):
    for n in range(1, 60, 10):
        results = []
        for i in range(0, 100):
            result = []
            random_graph = randomise.random_reassignment(copy.deepcopy(graph), transmitters.get_scheme(1))
            simannealing = sa.SimulatedAnnealing(random_graph, transmitters.get_scheme(1), temperature=n)
            
            print(f"Running Annealing: {i}")

            for _ in range(0, 500):
                    simannealing.run(1)
                    result.append(simannealing.graph.calculate_value())

            results.append(result)

        values = []
        for iteration in zip(*results):
            values.append((mean(iteration), min(iteration), max(iteration)))

        with open(f"results/simulatedannealing/simulatedannealing_temp_{n}.csv", 'w', newline='') as output_file:
            result_writer = csv.writer(output_file, delimiter=',')
            for value in values:
                result_writer.writerow(value)
        
            
def simulateannealing_graph():
    fig, ax = plt.subplots()
    with open("results/simulatedannealing/simulatedannealing.csv", 'r') as input_file:
        result_reader = csv.reader(input_file, delimiter=',')
        results = [int(value) for value, _ in result_reader]

    ax.plot(results, label='SimulatedAnnealing')
    ax.set_title('Simulated Annealing')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Total Costs')
    fig.savefig("results/simulatedannealing/single_run.png")


def simulatedannealing_averages_graph():
    fig, ax = plt.subplots()
    with open("results/simulatedannealing/simulatedannealing_averages.csv", 'r') as input_file:
        result_reader = csv.reader(input_file, delimiter=',')
        results = [float(value) for value, _, _ in result_reader]

    ax.plot(results, label='SimulatedAnnealing')
    ax.set_title('Simulated Annealings (n=100)')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Average Total Costs')
    fig.savefig("results/simulatedannealing/simulatedannealing_averages.png")


def simulatedannealing_averages_filled_graph():
    fig, ax = plt.subplots()
    with open("results/simulatedannealing/simulatedannealing_averages.csv", 'r') as input_file:
        result_reader = csv.reader(input_file, delimiter=',')
        results = [(float(average), int(minimum), int(maximum)) for average, minimum, maximum in result_reader]
        averages = [average for average, minimum, maximum in results]
        minima = [minimum for average, minimum, maximum in results]
        maxima = [maximum for average, minimum, maximum in results]

    ax.plot(averages, label='SimulatedAnnealing')
    ax.fill_between(range(0, len(averages)), minima, maxima, alpha=0.5, linewidth=0)
    ax.set_title('SimulatedAnnealing (n=100)')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Average Total Costs')
    fig.savefig("results/simulatedannealing/simulatedannealing_averages_filled.png")

def simulatedannealing_temperature_comparisons_graph():
    fig, ax = plt.subplots()
    results = []
    for n in range(1, 60, 10):
        with open(f"results/simulatedannealing/simulatedannealing_temp_{n}.csv", 'r') as input_file:
            result_reader = csv.reader(input_file, delimiter=',')
            results.append([float(value) for value, _, _ in result_reader])

    for temp, result in zip(range(1, 60, 10), results):
        ax.plot(result, label=f'Temperature {temp}')

    ax.legend(loc='upper right')
    ax.set_title('Sim Annealing Temperatures (n=100)')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Total Costs')
    fig.savefig(f"results/simulatedannealing/simulatedannealing_temp_{n}.png")