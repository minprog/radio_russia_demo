import matplotlib.pyplot as plt
import json


def depth_first_memory_comparison() -> None:
    fig, ax = plt.subplots(figsize=(8, 4))
    with open("results/depth_first/depth_first.json", 'r') as input_file:
        depth_result = json.load(input_file)

    with open("results/depth_first/branchandbound.json", 'r') as input_file:
        bnb_result = json.load(input_file)

    ax.set_title('Depth First Memory Comparison')

    ax.plot(bnb_result['states_sizes'], label='BranchAndBound')
    ax.plot(depth_result['states_sizes'], label='DepthFirst')
    ax.legend(loc='upper right')

    ax.yaxis.get_major_locator().set_params(nbins=20, steps=[1, 2, 5, 10])  # type: ignore[call-arg]
    ax.set_xlabel('Considered States')
    ax.set_ylabel('Number of States in Memory')
    fig.savefig("results/comparisons/depth_first_memory_comparison.png")


if __name__ == "__main__":
    depth_first_memory_comparison()
