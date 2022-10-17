#!/usr/bin/python3
"""Defines a rectangle class"""

Class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes data for the rectangle
        Args:
            width:width of rectangle
            height:height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrives width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Defines width of rectangle
        Args:
            value: integer that represents the width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Retrives height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Defines height of rectangle
        Args:
            value: integer that represents the width
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >=0")

    def area(self):
        """Returns the rectangle's area"""
        return (self.__width *self.__height)

    def perimeter(self):
        """Returns the rectangle's perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))
