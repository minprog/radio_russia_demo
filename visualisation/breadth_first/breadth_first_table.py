import matplotlib.pyplot as plt
import json


def breadth_first_table() -> None:
    fig, ax = plt.subplots(figsize=(8, 4))

    with open("results/breadth_first/breadth_first.json", 'r') as input_file:
        result = json.load(input_file)

    cells = [str(result['visited_state_count']), str(result['max_states_size']), str(result['solution_count']), str(result['value'])]

    ax.set_title('Breadth First Overview')
    ax.set_axis_off()

    ax.table(
        colLabels=['Visited State Count', 'Max States Size', 'Solution Count', 'Objective Value'],
        rowLabels=["DepthFirst"],
        cellText=[cells],
        loc='upper left',
    )
    fig.tight_layout()
    fig.savefig("results/breadth_first/breadth_first.png")


if __name__ == "__main__":
    breadth_first_table()
