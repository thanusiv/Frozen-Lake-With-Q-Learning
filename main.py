from environment import Environment
from q_learning import Q_Learning


def main():
    frozen_lake_environment = Environment()
    q_learning_algo = Q_Learning(frozen_lake_environment)

    q_learning_algo.run_algorithm()

    q_learning_algo.print_results()
    q_learning_algo.run_and_print_latest_iteration()


if __name__ == '__main__':
    main()
