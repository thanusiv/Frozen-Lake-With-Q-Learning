from action import Action
import numpy as np
from copy import deepcopy


class Environment:

    def __init__(self):
        self.map = np.array([['S', 'F', 'F', 'F'], ['F', 'H', 'F', 'H'], ['F', 'F', 'F', 'H'], ['H', 'F', 'F', 'G']])

        self.action_space = np.array([Action.Left, Action.Right, Action.Up, Action.Down])
        self.state_space = [i for i in range(np.array(self.map).size)]

        self.no_left_states = [4, 8, 0, 12]
        self.no_right_states = [7, 11, 3, 15]
        self.no_up_states = [1, 2, 0, 3]
        self.no_down_states = [13, 14, 12, 15]

        self.current_state = 0

    def get_action_space(self):
        return self.action_space

    def get_state_space(self):
        return self.state_space

    def get_random_action(self):
        return np.random.choice(self.action_space)

    def step(self, action_index):
        action = Action(action_index)

        if self.invalid_action(action):
            return self.current_state, 0, False

        if action == Action.Left:
            self.current_state -= 1
        elif action == Action.Right:
            self.current_state += 1
        elif action == Action.Up:
            self.current_state -= 4
        else:
            self.current_state += 4

        row, column = self.get_indices_of_current_state()
        letter = self.map[row][column]

        if letter == 'S' or letter == 'F':
            return self.current_state, 0, False
        elif letter == 'G':
            return self.current_state, 1, True
        else:
            return self.current_state, 0, True

    def invalid_action(self, action):
        if (action == Action.Left and self.current_state in self.no_left_states) or \
           (action == Action.Right and self.current_state in self.no_right_states) or \
           (action == Action.Up and self.current_state in self.no_up_states) or \
           (action == Action.Down and self.current_state in self.no_down_states):
            return True

        return False

    def get_indices_of_current_state(self):
        temp = 0
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if temp == self.current_state:
                    return i, j
                temp += 1

    def reset(self):
        self.current_state = 0
        return self.current_state

    def print_current_state(self):
        temp_map = deepcopy(self.map)
        row, column = self.get_indices_of_current_state()
        temp_map[row][column] = 'X'

        for r in temp_map:
            print(r[0], r[1], r[2], r[3])
        print()
