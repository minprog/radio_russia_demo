import matplotlib.pyplot as plt
import json


def depth_first_memory_graph() -> None:
    fig, ax = plt.subplots(figsize=(8, 4))
    with open("results/depth_first/depth_first.json", 'r') as input_file:
        result = json.load(input_file)

    sizes = result['states_sizes']

    ax.set_title('Depth First Memory Growth')

    hb = ax.hexbin(
        range(len(sizes)),
        sizes,
        gridsize=(80, max(sizes) + 1),
        cmap='viridis',
        mincnt=1,
    )
    fig.colorbar(hb, ax=ax, label='Frequency')
    ax.set_xlabel('Considered States')
    ax.set_ylabel('Number of States in Memory')
    fig.savefig("results/depth_first/depth_first_memory.png")


if __name__ == "__main__":
    depth_first_memory_graph()
