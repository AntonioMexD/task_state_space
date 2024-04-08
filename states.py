class State:
    def __init__(self, value):
        self.value = value
        self.actions = []
        self.visited = False
        self.parent = None
        self.cost = None

    def add_action(self, action):
        if action not in self.actions:
            self.actions.append(action)

    def mark_visited(self):
        self.visited = True

    def mark_unvisited(self):
        self.visited = False

    def was_visited(self):
        return self.visited

    def was_reached(self):
        return self.cost is not None or self.parent is not None
    
    def set_parent(self, value):
        self.parent = value

    def set_cost(self, cost):
        self.cost = cost

    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        return f"{self.value} -> {self.actions}"

class StatesSpace:
    def __init__(self):
        self.space = {}

    def add_state(self, value):
        self.space[value] = State(value)

    def add_action(self, value1, value2):
        self.space[value1].add_action(value2)

    def get_state(self, value):
        if isinstance(value, tuple):
            return self.space[value[0]]
        else:
            return self.space[value]

    def reset(self):
        self.reset_visited()
        self.reset_costs()

    def reset_costs(self):
        for state in self.space.values():
            state.set_cost(None)

    def reset_visited(self):
        for state in self.space.values():
            state.mark_unvisited()

    def __str__(self):
        return "\n".join(str(state) for state in self.space.values())
