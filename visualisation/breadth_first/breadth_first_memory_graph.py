import matplotlib.pyplot as plt
import json


def breadth_first_memory_graph() -> None:
    fig, ax = plt.subplots(figsize=(8, 4))
    with open("results/breadth_first/breadth_first.json", 'r') as input_file:
        result = json.load(input_file)

    ax.set_title('Breadth First Memory Growth')

    ax.plot(result['states_sizes'], label='States')
    ax.set_xlabel('Considered States')
    ax.set_ylabel('Number of States in Memory')
    fig.savefig("results/breadth_first/breadth_first_memory.png")


if __name__ == "__main__":
    breadth_first_memory_graph()
