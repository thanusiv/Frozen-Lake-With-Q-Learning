import numpy as np
import random
import time


class Q_Learning:

    def __init__(self, environment, **parameters):
        self.env = environment

        self.num_episodes = parameters.get('num_episodes', 10000)
        self.max_steps_per_episode = parameters.get('max_steps_per_episode', 100)
        self.learning_rate = parameters.get('learning_rate', 0.1)
        self.discount_rate = parameters.get('discount_rate', 0.99)
        self.exploration_rate = parameters.get('exploration_rate', 1)
        self.max_exploration_rate = parameters.get('max_exploration_rate', 1)
        self.min_exploration_rate = parameters.get('min_exploration_rate', 0.01)
        self.exploration_decay_rate = parameters.get('exploration_decay_rate', 0.001)

        self.q_table = np.zeros((len(environment.get_state_space()), len(environment.get_action_space())))
        self.all_episode_rewards = []

    def run_algorithm(self):
        for episode in range(self.num_episodes):
            rewards_for_current_episode = 0
            state = self.env.reset()

            for step in range(self.max_steps_per_episode):
                rand = random.uniform(0, 1)
                if rand < self.exploration_rate:
                    action_index = self.env.get_random_action().value
                else:
                    action_index = np.argmax(self.q_table[state, :])

                new_state, reward, done = self.env.step(action_index)

                self.q_table[state][action_index] = self.q_table[state][action_index] * (1 - self.learning_rate) + \
                                                    self.learning_rate * (
                                                            reward + self.discount_rate * np.max(
                                                        self.q_table[new_state, :]))

                state = new_state
                rewards_for_current_episode += reward

                if done:
                    break

            self.exploration_rate = self.min_exploration_rate + \
                                    (self.max_exploration_rate - self.min_exploration_rate) * np.exp(
                -self.exploration_decay_rate * episode)

            self.all_episode_rewards.append(rewards_for_current_episode)

    def print_results(self):
        print('Q-Table')
        print(self.q_table)
        print('-------------------------------------')

        # Calculate and print the average reward per thousand episodes
        rewards_per_thousand_episodes = np.split(np.array(self.all_episode_rewards), self.num_episodes / 1000)
        count = 1000

        print("Average reward per thousand episodes")
        for r in rewards_per_thousand_episodes:
            print(count, ": ", str(sum(r) / 1000))
            count += 1000
        print()

    def run_and_print_latest_iteration(self):
        state = self.env.reset()
        for step in range(self.max_steps_per_episode):
            self.env.print_current_state()
            time.sleep(1)
            action_index = np.argmax(self.q_table[state, :])
            new_state, _, done = self.env.step(action_index)
            state = new_state

            if done:
                print('The agent has reached the goal!!!')
                break
