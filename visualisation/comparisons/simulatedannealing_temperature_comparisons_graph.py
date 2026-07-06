import matplotlib.pyplot as plt
import csv


def simulatedannealing_temperature_comparisons_graph() -> None:
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
    fig.savefig("results/comparisons/simulatedannealing_temperature_comparisons_graph.png")


if __name__ == "__main__":
    simulatedannealing_temperature_comparisons_graph()
