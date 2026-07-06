import matplotlib.pyplot as plt
import csv


def random_greedy_graph() -> None:
    fig, ax = plt.subplots()
    with open("results/greedy/random_greedy.csv", 'r') as input_file:
        result_reader = csv.reader(input_file, delimiter=',')
        results = [int(value) for value, _ in result_reader]

    ax.hist(results)
    ax.set_title('Random Greedy Solutions')
    ax.set_xlabel('Total Costs')
    ax.set_ylabel('Number of Solutions')
    fig.savefig("results/greedy/random_greedy.png")


if __name__ == "__main__":
    random_greedy_graph()
