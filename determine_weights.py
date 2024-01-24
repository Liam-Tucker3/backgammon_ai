# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 20:26:53 2023

@author: letuc
"""

import numpy as np
from src.custom_strategy import custom_player # Created to allow for cutom experimentation
from src.weight_experiment import WeightExperiment
from src.compare_all_moves_strategy import CompareAllMovesWeightingDistance, CompareAllMovesWeightingDistanceAndSinglesWithEndGame2
from src.strategy_factory import MoveFurthestBackStrategy
from src.random_restart import random_restart
# =============================================================================
# Order of attributes in initial_weights
# 'number_occupied_spaces': number_occupied_spaces,
# 'opponents_taken_pieces': opponents_taken_pieces,
# 'sum_distances': sum_distances,
# 'sum_distances_opponent': sum_distances_opponent,
# 'number_of_singles': number_of_singles,
# 'sum_single_distance_away_from_home': sum_single_distance_away_from_home,
# 'pieces_on_board': pieces_on_board,
# 'sum_distances_to_endzone': sum_distances_to_endzone,
 

# 269 games: minimum number of games such that strategy with 55% chance of winning 
# individual game has at least 95% chance of winning series
def testFinalStrategies():
    
    # Creating strategies that don't include my custom attribute
    w2 = [-0.925672285, -1, 1, -0.066992944, 0.20178664, 0.149303257, 1.227322035, 0.15410344, 0]
    w3 = [-0.677618441, -0.88821331, 0.286821333, -0.458522188, 0.677571427, 0.66484779, 0.588940316, 0.118851684, 0]
    w5 = [-0.556156236, -0.489868686, -0.327466804, -0.761089344, 0.369566927, 0.8245367, 0.662145221, 0.12011533, 0]
    w1 = [-0.578612945, -0.194372013, 0.998351437, -0.379138398, -0.48973386, 0.091891502, 0.937047711, 0.055684155, 0]
    w4 = [-0.518367714, 0.670480008, 0.329387027, -0.971336478, 0.942134589, 0.396376641, 0.081913357, 0.137718485, 0]
    ws = [-0.651285524, -0.3803948, 0.457418599, -0.52741587, 0.340265145, 0.425391178, 0.699473728, 0.117294619, 0]
    ww = [-0.652420443, -0.383952242, 0.466022673, -0.522793883, 0.33279483, 0.421003869, 0.704468506, 0.116933455, 0]
    r1 = custom_player(w1)
    r2 = custom_player(w2)
    r3 = custom_player(w3)
    r4 = custom_player(w4)
    r5 = custom_player(w5)
    r6 = custom_player(ws) # Simple average of top 5 weights
    r7 = custom_player(ww) # Weighted average, weighted by number of victories
    
    # Creating strategies that do include my cusotm attribute
    c1 = [-0.2662481, 0.50135914, 0.289347493, -0.923691027, -0.945535314, 0.354734213, 0.578822592, 0.010391685, 0.89731644]
    c3 = [-0.394634295, -0.237660735, 0.946844601, -0.676908546, -0.828076405, 0.302795755, 0.859162571, 0.074774006, 0.272423228]
    c4 = [-0.799316658, -0.97730048, 0.295315261, -0.472864634, 0.706229756, 0.082302355, 0.145737443, 0.381089639, -0.685917433]
    c2 = [-0.970537182, -0.984568516, 0.736305713, -0.96755707, -0.559878932, 0.416247912, 0.990162973, 0.158104991, 0.401819125]
    c5 = [-0.981082538, -0.7860525, 0.710610019, -0.979795933, 0.392081788, 0.784745383, 0.221030135, 0.419805352, 0.464387108]
    cs = [-0.682363755, -0.496844618, 0.595684617, -0.804163442, -0.247035821, 0.388165124, 0.558983143, 0.208833135, 0.270005694]
    cw = [-0.677260396, -0.489878324, 0.593681695, -0.802890489, -0.260272533, 0.382917484, 0.565273178, 0.204864986, 0.270902899]
    c1 = custom_player(c1)
    c2 = custom_player(c2)
    c3 = custom_player(c3)
    c4 = custom_player(c4)
    c5 = custom_player(c5)
    c6 = custom_player(cs) # Simple average of top 5 weights
    c7 = custom_player(cw) # Weighted average, weighted by number of victories
    
    # op = CompareAllMovesWeightingDistanceAndSinglesWithEndGame2()
    
    players = [r1, r2, r3, r4, r5, r6, r7, c1, c2, c3, c4, c5, c6, c7]
    
    for player in players:
        e1 = WeightExperiment(games_to_play=1, white_strategy=player, black_strategy=CompareAllMovesWeightingDistance(), parallelise=True)
        e1.run()
        print("Against CompareAllMovesWeightingDistance")
        e1.print_results()
        print()
        
        e2 = WeightExperiment(games_to_play=2, white_strategy=player, black_strategy=MoveFurthestBackStrategy(), parallelise=True)
        e2.run()
        print("Against MoveFurthestBackStrategy")
        e2.print_results()
        print()
        
        # e2 = WeightExperiment(games_to_play=2501, white_strategy=player, black_strategy=CompareAllMovesWeightingDistanceAndSinglesWithEndGame2(), parallelise=True)
        # e2.run()
        # print("Against CompareAllMovesWeightingDistanceAndSinglesWithEndGame2()")
        # e2.print_results()
        # print()

if __name__ == '__main__':

    # r = random_restart("data/custom/forced_starting_position_1_restart_", include_custom_attribute = True)
    # r.determine_strategy(269, 50, 5)
    
    testFinalStrategies();


