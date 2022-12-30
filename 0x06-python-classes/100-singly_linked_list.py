#!/usr/bin/python3
# This program inserts a new node into sorted position

class Node:
    """
        This class creates nodes of linked list 
        Node: creates a node
        Attributes:
            data: private instance attribute
            next_node: private instance attribute
    """
    def __init__(self, data, next_node=None):
        """
            __init__: Initializes the attributes
            Args:
                data: data part of node
                next_node: node part of node
        """
        self.data = data
        self.__next_node = next_node

    @property
    # the getter function for data

    def data(self):
        """ 
            data: the getter function to retrieve the data
        """
        return self.__data
    @data.setter
    # the setter fucntion for data

    def data(self, value):
        """
            data: sets the data attribute
            Args:
                value: value to set the data attribute
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    # the getter function for next_node

    def next_node(self):
        """
            next_node: to retrieve the next_node attribute
        """
        return self.__next_node
    @next_node.setter
    # the setter function for next_node

    def next_node(self, value):
        """
            next_node: to set the next_node attribute
                Args:
                    value: value to set the next_node attribute
        """
        if type(value) is Node or type(value) is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a node object")

class SinglyLinkedList:
    """
        SinglyLinkedList: defines a singly linked list
        Attributes:
            head: head pointer to the first node
    """
    def __init__(self):
        """Initializes the attributes"""
        self.__head = None

    # My own __stir__ function that prints all objects in the list
    def __str__(self):
        """This function prints each node's data on a new line"""
        sll = ''
        ptr = self.__head
        if ptr is not None:
            while ptr is not None:
                sll += str(ptr.data) + '\n'
                ptr = ptr.next_node
        return sll[:-1]
    # Method that inserts the node is ascending order
    def sorted_insert(self, value):
        """
            sorted_insert: sorts the nodes in ascending order
            Args:
                value: the value to use in condition when inserting
        """
        # let ptr points to the first node or none
        ptr = self.__head

        # condition to make any new node the is the smallest first node
        if ptr is None or self.__head.data >= value:
            self.__head = Node(value, self.__head)
        else:
            # condition to iterate if the present node's data is small
            while ptr.next_node is not None and ptr.next_node.data < value:
                ptr = ptr.next_node
            ptr.next_node = Node(value, ptr.next_node)