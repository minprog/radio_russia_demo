import matplotlib.pyplot as plt
import csv


def baseline_graph() -> None:
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


if __name__ == "__main__":
    baseline_graph()
