"""
File: arrayheap.py

Defines the class ArrayHeap
"""

from abstractcollection import AbstractCollection

class ArrayHeap(AbstractCollection):

    def __init__(self, sourceCollection = None, profiler = None):
        self.heap = list()
        self.profiler = profiler
        AbstractCollection.__init__(self, sourceCollection)

    def peek(self):
        if self.isEmpty():
            raise AttributeError("Heap is empty")
        return self.heap[0]

    def add(self, item):
        self.size += 1
        self.heap.append(item)
        curPos = len(self.heap) - 1
        while curPos > 0:
            if self.profiler: self.profiler.comparison()
            parent = (curPos - 1) // 2
            parentItem = self.heap[parent]
            if parentItem <= item:
                break
            else:
                if self.profiler: self.profiler.exchange()
                self.heap[curPos] = self.heap[parent]
                self.heap[parent] = item
                curPos = parent

    def pop(self):
        if self.isEmpty():
            raise Exception("Heap is empty")
        self.size -= 1
        topItem = self.heap[0]
        bottomItem = self.heap.pop(len(self.heap) - 1)
        if len(self) == 0:
            return bottomItem
           
        self.heap[0] = bottomItem
        lastIndex = len(self.heap) - 1
        curPos = 0
        while True:
            if self.profiler: self.profiler.comparison()
            leftChild = 2 * curPos + 1 
            rightChild = 2 * curPos + 2
            if leftChild > lastIndex:
                break
            if rightChild > lastIndex:
                maxChild = leftChild;
            else:
                if self.profiler: self.profiler.exchange()
                leftItem  = self.heap[leftChild]
                rightItem = self.heap[rightChild]
                if leftItem < rightItem:
                    maxChild = leftChild
                else:
                    maxChild = rightChild
            maxItem = self.heap[maxChild]
            if bottomItem <= maxItem:
                break
            else:
                self.heap[curPos] = self.heap[maxChild]
                self.heap[maxChild] = bottomItem
                curPos = maxChild
        return topItem

    def __iter__(self):
        tempList = list(self.heap)
        resultList = []
        while not self.isEmpty():
            resultList.append(self.pop())
        self.heap = tempList
        self.size = len(self.heap)
        return iter(resultList)
      
    def __str__(self):
        def strHelper(position, level):
            result = ""
            if position < len(self):
                result += strHelper(2 * position + 2, level + 1)
                result += "|" * level
                result += str(self.heap[position]) + "\n"
                result += strHelper(2 * position + 1, level + 1)
            return result
        return strHelper(0, 0)

def main():
    heap = ArrayHeap()
    print("Adding D B A C F E G")
    heap.add("D")
    heap.add("B")
    heap.add("A")
    heap.add("C")
    heap.add("F")
    heap.add("E")
    heap.add("G")

    print("\nPeek:", heap.peek())

    print("\nString:\n" + str(heap))

    print("\nfor loop: ")
    for item in heap:
        print(item, end=" ")

    print("\n\nRemovals: ")
    while not heap.isEmpty(): print(heap.pop(), end=" ")

    heap = ArrayHeap(range(1, 8))
    print("\n\nHeap with 1..7:")
    print(heap)
    print("\nfor loop: ")
    for item in heap:
        print(item, end=" ")

if __name__ == "__main__":
    main()




