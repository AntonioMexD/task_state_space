import argparse
from search import Searcher
from states import StatesSpace

def parse_arguments():
    parser = argparse.ArgumentParser(description="Busqueda en clases con UCS (Uniform Cost Search)")
    parser.add_argument("--initial", type=str, help="Estado inicial", required=True)
    parser.add_argument("--goal", type=str, help="Estado objetivo", required=True)
    parser.add_argument("--debug", action="store_true", help="Activar modo depuración")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    debugging = args.debug

    space_dict = {
        'A': [('B', 4), ('C', 5)],
        'B': [('A', 4), ('C', 11), ('D', 9), ('E', 7)],
        'C': [('A', 5), ('B', 11), ('E', 3)],
        'D': [('B', 9), ('E', 13), ('F', 2)],
        'E': [('B', 7), ('C', 3), ('D', 13), ('F', 6)],
        'F': [('D', 2), ('E', 6)],
    }

    space = StatesSpace()

    state_values = space_dict.keys()
    for state_value in state_values:
        space.add_state(state_value)

    for state_value, state_actions in space_dict.items():
        for action in state_actions:
            space.add_action(state_value, action)

    searcher = Searcher(space, debug=debugging)

    initial_value = args.initial
    goal_value = args.goal

    print("Buscando camino de", initial_value,"a", goal_value, "\n")

    space.reset()

    print("Buscar en costo uniforme")
    path, cost = searcher.uniform_cost(initial_value, goal_value)
    print(path, "costo:", cost)
