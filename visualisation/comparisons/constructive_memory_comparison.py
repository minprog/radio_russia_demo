import matplotlib.pyplot as plt
import json


def constructive_memory_comparison() -> None:
    fig, ax = plt.subplots(figsize=(8, 4))
    with open("results/breadth_first/breadth_first.json", 'r') as input_file:
        breadth_result = json.load(input_file)

    with open("results/depth_first/depth_first.json", 'r') as input_file:
        depth_result = json.load(input_file)

    ax.set_title('Breadth First Memory Growth')

    ax.plot(breadth_result['states_sizes'], label='States')
    ax.plot(depth_result['states_sizes'], label='States')

    ax.set_xlabel('Considered States')
    ax.set_ylabel('Number of States in Memory')
    fig.savefig("results/comparisons/constructive_memory_comparison.png")


if __name__ == "__main__":
    constructive_memory_comparison()
