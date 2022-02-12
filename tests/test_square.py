#!/usr/bin/env python
# encoding: utf-8

# ---------------------------------------------------------------------------------------------------------------------
# Name: test_square.py
# Version: 0.0.1
# Summary: SCGP - Simple Chess Game in Python
#          A simple chess game with a command line and GUI interfaces written in Python.
#
# Author: Alexsander Lopes Camargos
# Author-email: alcamargos@vivaldi.net
#
# License: MIT
# ---------------------------------------------------------------------------------------------------------------------

"""SCGP - Simple Chess Game in Python"""

from chess.square import Square
from chess.util import *

# A cell on the chess board.
square = Square('e', '4', ColorNames.WHITE, 'Pawn')


def test_chess_board_square_file():
    assert square.file == 'e'


def test_chess_board_rank():
    assert square.rank == '4'


def test_chess_board_square_name():
    assert square.square_name == 'e4'


def test_chess_board_square_color():
    assert square.color == 'White'


def test_chess_board_square_piece():
    assert square.piece == 'Pawn'


def test_chess_board_square_piece_change():
    square.piece = 'Bishop'

    assert square.piece == 'Bishop'
