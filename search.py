from queue import PriorityQueue as _PriorityQueue

class Frontier:
    def __init__(self):
        self.values = []

    def put(self, value):
        self.values.append(value)

    def has(self, value):
        return value in self.values

    def empty(self):
        return len(self.values) == 0

class Stack(Frontier):
    def get(self):
        return self.values.pop()

class Queue(Frontier):
    def get(self):
        return self.values.pop(0)

class PrioritizedQueue(_PriorityQueue, Frontier):
    def __init__(self):
        _PriorityQueue.__init__(self)
        Frontier.__init__(self)

    def put(self, value):
        # value = (item, priority)
        _PriorityQueue.put(self, (value[1], value[0]))

    def get(self):
        priority, state = _PriorityQueue.get(self)
        return state, priority

class Searcher:
    def __init__(self, space, debug=False):
        self.space = space
        self.debug = debug

    def depth_first(self, initial_value, goal_value):
        return self.search(initial_value, goal_value, frontier=Stack())

    def breadth_first(self, initial_value, goal_value):
        return self.search(initial_value, goal_value, frontier=Queue())
    
    def uniform_cost(self, initial_value, goal_value):
        return self.weighted_search(initial_value, goal_value, frontier=PrioritizedQueue())

    def search(self, initial_value, goal_value, frontier):
        initial_state = self.space.get_state(initial_value)
        frontier.put(initial_state)

        while not frontier.empty():
            current_state = frontier.get()
            if self.debug: print(current_state)
            current_state.mark_visited()

            if current_state.value == goal_value:
                return self.build_solution_path(current_state)

            for action in current_state.actions:
                next_state = self.space.get_state(action)
                if not next_state.was_visited() and not frontier.has(next_state):
                    next_state.set_parent(current_state)
                    frontier.put(next_state)

    def weighted_search(self, initial_value, goal_value, frontier):
        initial_state = self.space.get_state(initial_value)
        initial_state.set_cost(0)
        frontier.put((initial_state, 0))

        while not frontier.empty():
            current_state, current_cost = frontier.get()
            current_state.mark_visited()
            if self.debug: print(current_state.value, current_cost)

            if current_state.value == goal_value:
                if self.debug: print("Goal found")
                return self.build_solution_path(current_state), current_cost

            for action in current_state.actions:
                next_state = self.space.get_state(action)
                action_cost = current_cost + action[1]

                if not next_state.was_reached() or action_cost < next_state.cost:
                    next_state.set_parent(current_state)
                    next_state.set_cost(action_cost)

                    if self.debug:print("Expanding:", next_state.value, action_cost)
                    frontier.put((next_state, action_cost))

        return []

    def build_solution_path(self, state):
        path = []
        while state:
            path.append(state.value)
            state = state.parent
        return list(reversed(path))