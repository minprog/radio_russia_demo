import matplotlib.pyplot as plt
import csv


def hillclimb_graph() -> None:
    fig, ax = plt.subplots()
    with open("results/hillclimber/hillclimber.csv", 'r') as input_file:
        result_reader = csv.reader(input_file, delimiter=',')
        results = [int(value) for value, _ in result_reader]

    ax.plot(results, label='HillClimber')
    ax.set_title('Hill Climber')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Total Costs')
    fig.savefig("results/hillclimber/single_run.png")


if __name__ == "__main__":
    hillclimb_graph()
