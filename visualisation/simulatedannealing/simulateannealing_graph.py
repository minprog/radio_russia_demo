import matplotlib.pyplot as plt
import csv


def simulateannealing_graph() -> None:
    fig, ax = plt.subplots()
    with open("results/simulatedannealing/simulatedannealing.csv", 'r') as input_file:
        result_reader = csv.reader(input_file, delimiter=',')
        results = [int(value) for value, _ in result_reader]

    ax.plot(results, label='SimulatedAnnealing')
    ax.set_title('Simulated Annealing')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Total Costs')
    fig.savefig("results/simulatedannealing/single_run.png")


if __name__ == "__main__":
    simulateannealing_graph()
