import matplotlib.pyplot as plt
import csv


def hillclimber_averages_filled_graph() -> None:
    fig, ax = plt.subplots()
    with open("results/hillclimber/hillclimber_averages.csv", 'r') as input_file:
        result_reader = csv.reader(input_file, delimiter=',')
        results = [(float(average), int(minimum), int(maximum)) for average, minimum, maximum in result_reader]
        averages = [average for average, minimum, maximum in results]
        minima = [minimum for average, minimum, maximum in results]
        maxima = [maximum for average, minimum, maximum in results]

    ax.plot(averages, label='HillClimber')
    ax.fill_between(range(0, len(averages)), minima, maxima, alpha=0.5, linewidth=0)
    ax.set_title('Hill Climbers (n=100)')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Average Total Costs')
    fig.savefig("results/hillclimber/hillclimber_averages_filled.png")


if __name__ == "__main__":
    hillclimber_averages_filled_graph()
