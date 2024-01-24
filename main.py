# Play backgammon
from src.compare_all_moves_strategy import CompareAllMovesWeightingDistance, CompareAllMovesWeightingDistanceAndSingles
from src.compare_all_moves_strategy import CompareAllMovesWeightingDistanceAndSinglesWithEndGame2, CompareAllMovesSimple

from src.compare_all_moves_strategy import CompareAllMovesWeightingDistanceAndSinglesWithEndGame
from letucker import player1_letucker
from src.experiment import Experiment
from weight_experiment import WeightExperiment

from custom_strategy import custom_player
import numpy as np

initial_weights = np.array([-1 * float(1), 
                   -1 * float(1), 
                   1,
                   -1 * float(1) / 3,
                   float(0),
                   float(1) / 3,
                   3 * float(1),
                   float(1) / 6])

c = custom_player(initial_weights)

# for i in range(3):
experiment = WeightExperiment(
    games_to_play=25,
    white_strategy=c,
    black_strategy=CompareAllMovesWeightingDistanceAndSinglesWithEndGame2(),
    parallelise=True
)
# experiment.run()
# experiment.print_results()
# freeze_support()

if __name__ == '__main__':
    experiment.run()
    experiment.print_results()


# Null hypothesis is that the strategies equally good
# Define a joint event of a random coin toss to determine who starts followed by a game,
# Under the null hypothesis, for a single event, p(win) = 0.5
# Assuming the strategies are equal (null hypothesis): P(n_wins) = binom(n_wins, n_games, 0.5)


# Want systematically determine weights
# Can include all features (any not important will end up with weight ~0)
# Every weight should be in range [-1, 1]

# Grad student part 3: Given board state, apply alpha-beta pruning and determine best move
# Can write it or code it
