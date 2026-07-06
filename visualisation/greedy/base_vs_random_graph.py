import matplotlib.pyplot as plt
import csv


def base_vs_random_graph() -> None:
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


if __name__ == "__main__":
    base_vs_random_graph()
