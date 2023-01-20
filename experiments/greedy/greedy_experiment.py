from code.algorithms import greedy as gr
import matplotlib.pyplot as plt
import csv


def random_greedy(graph, transmitters):
    results = []
    for _ in range(10000):
        random_greedy_graph = gr.RandomGreedy(graph, transmitters.get_scheme((1)))
        random_greedy_graph.run()
        results.append((random_greedy_graph.graph.calculate_value(), random_greedy_graph.graph.to_json()))

    with open("results/greedy/random_greedy.csv", 'w', newline='') as output_file:
        result_writer = csv.writer(output_file, delimiter=',')
        for result in results:
            result_writer.writerow(result)


def greedy(graph, transmitters):
    greedy_graph = gr.Greedy(graph, transmitters.get_scheme((1)))
    greedy_graph.run()
    with open("results/greedy/greedy.csv", 'w', newline='') as output_file:
        result_writer = csv.writer(output_file, delimiter=',')
        result_writer.writerow((greedy_graph.graph.calculate_value(), greedy_graph.graph.to_json()))


def random_greedy_graph():
    fig, ax = plt.subplots()
    with open("results/greedy/random_greedy.csv", 'r') as input_file:
        result_reader = csv.reader(input_file, delimiter=',')
        results = [int(value) for value, _ in result_reader]

    ax.hist(results)
    ax.set_title('Random Greedy Solutions')
    ax.set_xlabel('Total Costs')
    ax.set_ylabel('Number of Solutions')
    fig.savefig("results/greedy/random_greedy.png")


def base_vs_random_graph():
    fig, ax = plt.subplots()
    
    with open("results/greedy/random_greedy.csv", 'r') as input_file:
        result_reader = csv.reader(input_file, delimiter=',')
        results = [int(value) for value, _ in result_reader]

    with open("results/greedy/greedy.csv", 'r') as input_file:
        result_reader = csv.reader(input_file, delimiter=',')
        greedy_result = [int(value) for value, _ in result_reader]

    ax.hist(results, label='Random')
    ax.vlines(greedy_result, 0, 4500, colors=['red'], label='Base')
    ax.legend(loc='upper right')
    ax.set_title('Base Greedy vs Random Greedy')
    ax.set_xlabel('Total Costs')
    ax.set_ylabel('Number of Solutions')
    fig.savefig("results/greedy/base_vs_random.png")