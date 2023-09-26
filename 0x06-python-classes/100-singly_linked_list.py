#!/usr/bin/python3
"""Singly linked list module"""


class Node:
    """Node class"""

    def __init__(self, data, next_node=None):
        """Initialize the class

        Args:
            data (int): data stored in Node
            next_node (Node, optional): next node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Get data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set data"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get next node instance"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set next node instance"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly linked list class"""

    def __init__(self):
        """Initialize the class"""
        self.__head = None

    def sorted_insert(self, value):
        """Sorted insert to a list

        Args:
            value (Node): a node to insert
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = self.__head
            self.__head = new_node
        elif self.__head.data >= new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while (current.next_node and
                    current.next_node.data < value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """String representation for LL"""
        tmp = []
        current = self.__head
        while current:
            tmp.append(str(current.data))
            current = current.next_node
        return ('\n'.join(tmp))
