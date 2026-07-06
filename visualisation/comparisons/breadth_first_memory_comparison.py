import matplotlib.pyplot as plt
import json


def breadth_first_memory_comparison() -> None:
    fig, ax = plt.subplots(figsize=(8, 4))
    with open("results/breadth_first/breadth_first.json", 'r') as input_file:
        breadth_result = json.load(input_file)

    with open("results/breadth_first/best_first.json", 'r') as input_file:
        best_result = json.load(input_file)

    ax.set_title('Breadth First Memory Comparison')

    ax.plot(breadth_result['states_sizes'], label='BreadthFirst')
    ax.plot(best_result['states_sizes'], label='BestFirst')
    ax.legend(loc='upper right')

    ax.set_xlabel('Considered States')
    ax.set_ylabel('Number of States in Memory')
    fig.savefig("results/comparisons/breadth_first_memory_comparison.png")


if __name__ == "__main__":
    breadth_first_memory_comparison()
