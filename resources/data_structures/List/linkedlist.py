"""
File: linkedlist.py
Project 9.1

Includes the list iterator for the LinkedList class.
"""

from node import TwoWayNode
from abstractlist import AbstractList

class LinkedList(AbstractList):
    """A link-based list implementation."""

    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        # Uses a circular linked structure with a dummy header node
        self.head = TwoWayNode()
        self.head.previous = self.head.next = self.head
        AbstractList.__init__(self, sourceCollection)

    # Helper method returns node at position i
    def getNode(self, i):
        """Helper method: returns a pointer to the node at position i."""
        if i == len(self):
            return self.head
        elif i == len(self) - 1:
            return self.head.previous
        probe = self.head.next
        while i > 0:
            probe = probe.next
            i -= 1
        return probe

    #Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self.head.next
        while cursor != self.head:
            yield cursor.data
            cursor = cursor.next

    def __getitem__(self, i):
        """Precondition: 0 <= i < len(self)
        Returns the item at position i.
        Raises: IndexError."""
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        return self.getNode(i).data

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.modCount = 0
        self.head = TwoWayNode()
        self.head.previous = self.head.next = self.head
        
    def __setitem__(self, i, item):
        """Precondition: 0 <= i < len(self)
        Replaces the item at position i.
        Raises: IndexError."""
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        self.getNode(i).data = item

    def insert(self, i, item):
        """Inserts the item at position i."""
        if i < 0: i = 0
        elif i > len(self): i = len(self)
        theNode = self.getNode(i)
        newNode = TwoWayNode(item, theNode.previous, theNode)
        theNode.previous.next = newNode
        theNode.previous = newNode
        self.size += 1
        self.incModCount()

    def pop(self, i = None):
        """Precondition: 0 <= i < len(self).
        Removes and returns the item at position i.
        If i is None, i is given a default of len(self) - 1.
        Raises: IndexError."""
        if i == None: i = len(self) - 1
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        theNode = self.getNode(i)
        item = theNode.data
        theNode.previous.next = theNode.next
        theNode.next.previous = theNode.previous
        self.size -= 1
        self.incModCount()
        return item

    def listIterator(self):
        """Returns a list iterator."""
        return LinkedList.ListIterator(self)

    class ListIterator(object):
        """Represents the list iterator for linked list."""

        def __init__(self, backingStore):
            self.backingStore = backingStore
            self.modCount = backingStore.getModCount()
            self.first()

        def first(self):
            """Returns the cursor to the beginning of the backing store."""
            self.cursor = self.backingStore.head.next
            self.lastItemPos = None

        def hasNext(self):
            """Returns True if the iterator has a next item or False otherwise."""
            return self.cursor != self.backingStore.head

        def next(self):
            """Preconditions: hasNext returns True
            The list has not been modified except by this iterator's mutators.
            Returns the current item and advances the cursor to the next item.
            Postcondition: lastItemPos is now defined.
            Raises: ValueError if no next item.
            AttributeError if illegal mutation of backing store."""
            if not self.hasNext():
                raise ValueError("No next item in list iterator")
            if self.modCount != self.backingStore.getModCount():
                raise AttributeError("Illegal modification of backing store")
            self.lastItemPos = self.cursor
            self.cursor = self.cursor.next
            return self.lastItemPos.data

        def last(self):
            """Moves the cursor to the end of the backing store."""
            self.cursor = self.backingStore.head
            self.lastItemPos = None

        def hasPrevious(self):
            """Returns True if the iterator has a previous item or False otherwise."""
            return self.cursor.previous != self.backingStore.head

        def previous(self):
            """Preconditions: hasPrevious returns True
            The list has not been modified except by this iterator's mutators.
            Returns the current item and moves the cursor to the previous item.
            Postcondition: lastItemPos is now defined.
            Raises: ValueError if no next item.
            AttributeError if illegal mutation of backing store."""
            if not self.hasPrevious():
                raise ValueError("No previous item in list iterator")
            self.cursor = self.cursor.previous
            self.lastItemPos = self.cursor
            return self.lastItemPos.data

        def replace(self, item):
            """Preconditions: the current position is defined.
            The list has not been modified except by this iterator's mutators.
            Replaces the items at the current position with item."""
            if self.lastItemPos == None:
                raise AttributeError("The current position is undefined.")
            if self.modCount != self.backingStore.getModCount():
                raise AttributeError("List has been modified illegally.")
            self.lastItemPos.data = item
            self.lastItemPos = None

        def insert(self, item):         
            """Preconditions:
            The list has not been modified except by this iterator's mutators.
            Adds item to the end if the current position is undefined, or
            inserts it at that position."""
            if self.modCount != self.backingStore.getModCount():
                raise AttributeError("List has been modified illegally.")
            if self.lastItemPos is None:
                self.backingStore.add(item)
            else:
                newNode = TwoWayNode(item, self.lastItemPos.previous, self.lastItemPos)
                self.lastItemPos.previous.next = newNode
                self.lastItemPos.previous = newNode
                self.backingStore.incModCount()
                self.backingStore.size += 1
                self.lastItemPos = None
            self.modCount += 1

        def remove(self):         
            """Preconditions: the current position is defined.
            The list has not been modified except by this iterator's mutators.
            Pops the item at the current position."""
            if self.lastItemPos == None:
                raise AttributeError("The current position is undefined.")
            if self.modCount != self.backingStore.getModCount():
                raise AttributeError("List has been modified illegally.")
            item = self.lastItemPos.data
            # If the item removed was obtained via previous, move cursor ahead
            if self.lastItemPos == self.cursor:
                self.cursor = self.cursor.next
            self.lastItemPos.previous.next = self.lastItemPos.next
            self.lastItemPos.next.previous = self.lastItemPos.previous
            self.backingStore.size -= 1
            self.backingStore.incModCount()
            self.modCount += 1
            self.lastItemPos = None
           





