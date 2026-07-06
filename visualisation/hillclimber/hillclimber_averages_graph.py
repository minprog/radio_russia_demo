import matplotlib.pyplot as plt
import csv


def hillclimber_averages_graph() -> None:
    fig, ax = plt.subplots()
    with open("results/hillclimber/hillclimber_averages.csv", 'r') as input_file:
        result_reader = csv.reader(input_file, delimiter=',')
        results = [float(value) for value, _, _ in result_reader]

    ax.plot(results, label='HillClimber')
    ax.set_title('Hill Climbers (n=100)')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Average Total Costs')
    fig.savefig("results/hillclimber/hillclimber_averages.png")


if __name__ == "__main__":
    hillclimber_averages_graph()
