from src.strategies import Strategy
from src.piece import Piece
from src.compare_all_moves_strategy import CompareAllMoves

class player1_letucker(CompareAllMoves):


            # 'number_occupied_spaces': number_occupied_spaces,
            # 'opponents_taken_pieces': opponents_taken_pieces,
            # 'sum_distances': sum_distances,
            # 'sum_distances_opponent': sum_distances_opponent,
            # 'number_of_singles': number_of_singles,
            # 'sum_single_distance_away_from_home': sum_single_distance_away_from_home,
            # 'pieces_on_board': pieces_on_board,
            # 'sum_distances_to_endzone': sum_distances_to_endzone,


    def evaluate_board(self, myboard, colour):
        board_stats = self.assess_board(colour, myboard)
        params = [-0.578612945, -0.194372013, 0.998351437, -0.379138398, -0.48973386, 0.091891502, 0.937047711, 0.055684155]

        board_value = board_stats['number_occupied_spaces'] * params[0] + \
                      board_stats['opponents_taken_pieces'] * params[1] + \
                      board_stats['sum_distances'] * params[2] + \
                      board_stats['sum_distances_opponent'] * params[3] + \
                      board_stats['number_of_singles'] * params[4] + \
                      board_stats['sum_single_distance_away_from_home'] * params[5] + \
                      board_stats['pieces_on_board'] * params[6] + \
                      board_stats['sum_distances_to_endzone'] * params[7]
        return board_value

class player2_letucker(CompareAllMoves):


            # 'NOVEL_FEATURE': novel_feature_value,
            # 'number_occupied_spaces': number_occupied_spaces,
            # 'opponents_taken_pieces': opponents_taken_pieces,
            # 'sum_distances': sum_distances,
            # 'sum_distances_opponent': sum_distances_opponent,
            # 'number_of_singles': number_of_singles,
            # 'sum_single_distance_away_from_home': sum_single_distance_away_from_home,
            # 'pieces_on_board': pieces_on_board,
            # 'sum_distances_to_endzone': sum_distances_to_endzone,


    def evaluate_board(self, myboard, colour):
        board_stats = self.assess_board(colour, myboard)

        params = [-0.970537182, -0.984568516, 0.736305713, -0.96755707, -0.559878932, 0.416247912, 0.990162973, 0.158104991, 0.401819125]

        board_value = board_stats['number_occupied_spaces'] * params[0] + \
                      board_stats['opponents_taken_pieces'] * params[1] + \
                      board_stats['sum_distances'] * params[2] + \
                      board_stats['sum_distances_opponent'] * params[3] + \
                      board_stats['number_of_singles'] * params[4] + \
                      board_stats['sum_single_distance_away_from_home'] * params[5] + \
                      board_stats['pieces_on_board'] * params[6] + \
                      board_stats['sum_distances_to_endzone'] * params[7] + \
                      board_stats['largest_blockade'] * params[8]
                      
        return board_value