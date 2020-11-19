"""
File: linkedqueue.py
Project 8.3
"""

from node import Node
from abstractcollection import AbstractCollection

class LinkedQueue(AbstractCollection):
    """A link-based queue implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.front = self.rear = None
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self.front
        while not cursor is None:
            yield cursor.data
            cursor = cursor.next
        
    def peek(self):
        """
        Returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if the stack is empty."""
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        return self.front.data

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.front = self.rear = None

    def add(self, item):
        """Adds item to the rear of the queue."""
        newNode = Node(item, None)
        if self.isEmpty():
            self.front = newNode
        else:
            self.rear.next = newNode
        self.rear = newNode
        self.size += 1

    def pop(self):
        """
        Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if the queue is empty.
        Postcondition: the front item is removed from the queue."""
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        oldItem = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return oldItem
        
    def remove(self, item):
        """Removes the given item from the queue.
        Precondition: item must be in the queue"""
        if not item in self:
            raise AttributeError(str(item) + " is not in the queue")
        # Find the position of item in the queue
        if item == self.front.data:
            self.front = self.front.next
        else:
            probe = self.front
            while item != probe.next.data:
                probe = probe.next
            probe.next = probe.next.next
        self.size -= 1
        if self.isEmpty():
            self.rear = None
        
