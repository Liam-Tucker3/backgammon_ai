# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 21:57:32 2023

@author: letuc
"""
from board import Board
from src.colour import Colour
from src.piece import Piece

# Creating initial board
b = Board()
b.add_many_pieces(1, Colour.WHITE, 2)
b.add_many_pieces(2, Colour.BLACK, 3)
b.add_many_pieces(2, Colour.WHITE, 5)
b.add_many_pieces(6, Colour.BLACK, 6)
b.add_many_pieces(4, Colour.WHITE, 12)
b.add_many_pieces(4, Colour.BLACK, 13)
b.add_many_pieces(1, Colour.BLACK, 15)
b.add_many_pieces(2, Colour.WHITE, 17)
b.add_many_pieces(6, Colour.WHITE, 19)
b.add_many_pieces(2, Colour.BLACK, 22)

b.print_board()

# In best possible format
dice_roll = [5, 2]



