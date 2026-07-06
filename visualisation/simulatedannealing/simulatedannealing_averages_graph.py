import matplotlib.pyplot as plt
import csv


def simulatedannealing_averages_graph() -> None:
    fig, ax = plt.subplots()
    with open("results/simulatedannealing/simulatedannealing_averages.csv", 'r') as input_file:
        result_reader = csv.reader(input_file, delimiter=',')
        results = [float(value) for value, _, _ in result_reader]

    ax.plot(results, label='SimulatedAnnealing')
    ax.set_title('Simulated Annealings (n=100)')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Average Total Costs')
    fig.savefig("results/simulatedannealing/simulatedannealing_averages.png")


if __name__ == "__main__":
    simulatedannealing_averages_graph()
