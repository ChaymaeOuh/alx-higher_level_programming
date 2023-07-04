#!/usr/bin/python3
"""define a class Square"""


class Square:
    """represent a square"""

    def __init(self, size=0):
        """initialize a new square

        Args:
            size(int): the size of the new square
            """
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
