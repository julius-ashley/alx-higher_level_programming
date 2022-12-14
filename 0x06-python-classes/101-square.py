#!/usr/bin/python3
"""This module defines a Square"""


class Square():
    """
        Square: defines a square
        Attributes:
                size: To know the length of sides, area and perimeter

        Method:
                __init__: Initializing the Square attribute

                area: Calculates the area of square
     """
    def __init__(self, size=0, position=(0, 0)):
        """Initializing the instance attribute

        Args:
            Size attributes
            position attributes
        """
        self.size = size
        self.position = position
    # Using property decorator
    # a getter function

    @property
    def size(self):

        """
            size: to return the size attribute
        """
        return self.__size
    # setter function

    @size.setter
    def size(self, value):
        """
            size: To set the size attribute

            Arguments:
                value: an integer or string
        """
        if type(value) != int or value < 0:
            raise ValueError("size must be >= 0")
        elif type(value) == int:
            if value >= 0:
                self.__size = value

    @property
    # getters function
    def position(self):
        """
            position: retrieves the position
        """
        return self.__position

    @position.setter
    # setter function
    def position(self, value):
        """
            position: sets the position attributes
            Argument:
                value: instance attribute
        """
        if type(value) is tuple and len(value) == 2 and \
            type(value[0]) is int and type(value[1]) is int and \
                value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive\
 integers")

    def area(self):
        """Calculates the area of square"""
        return (self.__size ** 2)

    def my_print(self):
        """
            my_print: prints # or blank line to stdout
        """
        if self.__size >= 0:
            if self.__position[0] <= 0 and self.__position[1] <= 0:
                for k in range(self.__size):
                    print('#' * self.__size)
            elif self.__positon[0] <= 0:
                for k in range(self.__position[1]):
                    print()
                for p in range(self.__size):
                    print("#" * self.__size, end="")
            elif self.__position[1] <= 0:
                for w in range(self.__size):
                    print(" " * self.__position[0], end="")
                    print("#" * self.__size)
            else:
                for y in range(self.__position[1]):
                    print()
                for x in range(self.__size):
                    print(" " * self.__position[0], end='')
                    print('#' * self.__size)
        else:
            print()

    # This function prints all the objects in the class
    def __str__(self):
        """This function acts as the print function"""
        items = ""
        if self.__size > 0:
            if self.__position[0] <= 0 and self.__position[1] <= 0:
                for k in range(self.__size):
                    items += "#" * self.__size
                    items += "\n"
            elif self.__position[0] <= 0:
                for k in range(self.__position[1]):
                    items += "\n"
                for k in range(self.__size):
                    items += "#" * self.__size
                    items += "\n"
            elif self.__position[1] <= 0:
                for k in range(self.__size):
                    items += " " * self.__position[0]
                    items += "#" * self.__size
                    items += "\n"
            else:
                for y in range(self.__position[1]):
                    items += "\n"
                for x in range(self.__position[0]):
                    items += " " * self.__position[0]
                    items += "#" * self.__size
                    items += "\n"
            return items[:-1]
        else:
            items += "\n"
            return items[:-1]
