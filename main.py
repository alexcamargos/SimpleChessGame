#!/usr/bin/env python
# encoding: utf-8

# ---------------------------------------------------------------------------------------------------------------------
#  Name: SCGP - Simple Chess Game in Python
#  Version: 0.0.1
#  Summary: A simple chess game with a command line and GUI interfaces written in Python.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
# ---------------------------------------------------------------------------------------------------------------------

"""Simple Chess Game in Python"""

import chess


if __name__ == '__main__':
    chess_game = chess.Chess()

    chess_game.draw_board()
