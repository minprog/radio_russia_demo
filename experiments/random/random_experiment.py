from code.algorithms import randomise
import matplotlib.pyplot as plt
import copy
import csv


def baseline(graph, transmitters):
    results = []
    for _ in range(10000):
        random_graph = randomise.random_reassignment(copy.deepcopy(graph), transmitters.get_scheme(1))
        results.append((random_graph.calculate_value(), random_graph.to_json()))

    with open("results/random/baseline.csv", 'w', newline='') as output_file:
        result_writer = csv.writer(output_file, delimiter=',')
        for result in results:
            result_writer.writerow(result)

def baseline_graph():
    fig, ax = plt.subplots()
    with open("results/random/baseline.csv", 'r') as input_file:
        result_reader = csv.reader(input_file, delimiter=',')
        results = [int(value) for value, _ in result_reader]

    ax.hist(results, label='Random')
    ax.legend(loc='upper right')
    ax.set_title('Baseline Random Solutions')
    ax.set_xlabel('Total Costs')
    ax.set_ylabel('Number of Solutions')
    fig.savefig("results/random/baseline.png")