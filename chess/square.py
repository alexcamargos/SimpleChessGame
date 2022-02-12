#!/usr/bin/env python
# encoding: utf-8

# ---------------------------------------------------------------------------------------------------------------------
# Name: square.py
# Version: 0.0.1
# Summary: SCGP - Simple Chess Game in Python
#          A simple chess game with a command line and GUI interfaces written in Python.
#
# Author: Alexsander Lopes Camargos
# Author-email: alcamargos@vivaldi.net
#
# License: MIT
# ---------------------------------------------------------------------------------------------------------------------

"""SCGP - Simple Chess Game in Python

    Square - Represent a cell on the chess board.
"""


class Square:
    """Represents one block of the 8×8 grid and optional information."""

    def __init__(self, file, rank, color, piece):
        self.__file = file
        self.__rank = rank
        self.__color = color
        self.__piece = piece

    def __str__(self):
        return f'{self.__class__.__name__}({self.square_name}, {self.color}, {self.piece})'

    @property
    def file(self):
        """Gets the file of the square, like ``e``."""

        return self.__file

    @property
    def rank(self):
        """Gets the rank of the square, like ``4``."""

        return self.__rank

    @property
    def color(self):
        """Gets the color of the square, like ``White``."""

        return self.__color.value

    @property
    def piece(self):
        """Gets the piece in the square, like ``Bishop``."""

        return self.__piece

    @piece.setter
    def piece(self, piece):
        """Set the piece in the square."""

        self.__piece = piece

    @property
    def square_name(self):
        """Gets the name of the square, like ``e4``."""

        return f'{self.file}{self.rank}'
