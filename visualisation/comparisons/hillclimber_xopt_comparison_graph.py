import matplotlib.pyplot as plt
import csv


def hillclimber_xopt_comparison_graph() -> None:
    fig, ax = plt.subplots()
    results = []
    for n in range(1, 6):
        with open(f"results/hillclimber/hillclimber_xopt_{n}.csv", 'r') as input_file:
            result_reader = csv.reader(input_file, delimiter=',')
            results.append([float(value) for value, _, _ in result_reader])

    for index, result in enumerate(results):
        ax.plot(result, label=f'X-Opt {index + 1}')

    ax.legend(loc='upper right')
    ax.set_title('Hill Climber X-Opts (n=100)')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Total Costs')
    fig.savefig("results/comparisons/hillclimber_xopt_comparison_graph.png")


if __name__ == "__main__":
    hillclimber_xopt_comparison_graph()
