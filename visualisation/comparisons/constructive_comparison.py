import matplotlib.pyplot as plt
import json


def constructive_comparison() -> None:
    fig, ax = plt.subplots(figsize=(8, 4))
    results = []
    with open("results/depth_first/depth_first.json", 'r') as input_file:
        result = json.load(input_file)
        results.append([str(result['visited_state_count']), str(result['max_states_size']), str(result['solution_count']), str(result['value'])])

    with open("results/depth_first/branchandbound.json", 'r') as input_file:
        result = json.load(input_file)
        results.append([str(result['visited_state_count']), str(result['max_states_size']), str(result['solution_count']), str(result['value'])])

    with open("results/breadth_first/breadth_first.json", 'r') as input_file:
        result = json.load(input_file)
        results.append([str(result['visited_state_count']), str(result['max_states_size']), str(result['solution_count']), str(result['value'])])

    with open("results/breadth_first/best_first.json", 'r') as input_file:
        result = json.load(input_file)
        results.append([str(result['visited_state_count']), str(result['max_states_size']), str(result['solution_count']), str(result['value'])])

    ax.set_title('Constructive Overview')
    ax.set_axis_off()

    ax.table(
        colLabels=['Visited State Count', 'Max States Size', 'Solution Count', 'Objective Value'],
        rowLabels=["DepthFirst", "BranchAndBound", "BreadthFirst", "BestFirst"],
        cellText=results,
        loc='upper left',
    )
    fig.tight_layout()
    fig.savefig("results/comparisons/constructive_comparison.png")


if __name__ == "__main__":
    constructive_comparison()
