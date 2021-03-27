# Course: CS261 - Data Structures
# Assignment: 5
# Student: Vincent Rastello
# Description: Min heap using dynamic array as underlying structure


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        Adds new node to end of heap, if parent is greater, percolates up until it finds correct spot.
        """
        self.heap.append(node)
        last = self.heap.length() - 1
        parent = (last - 1) // 2
        while last > 0 and self.heap[parent] > self.heap[last]:
            self.heap.swap(parent, last)
            last = parent
            parent = (last - 1) // 2

    def get_min(self) -> object:
        """
        if emtpy raises exception, otherwise returns min
        """
        if self.is_empty():
            raise MinHeapException
        return self.heap[0]

    def remove_min(self) -> object:
        """
        Removes min, pops last value from hash and sets as new min, percolates down until correct spot
        is found. Returns removed value
        """
        if self.is_empty():
            raise MinHeapException
        if self.heap.length() == 1:
            return self.heap.pop()
        removed = self.heap[0]
        self.heap[0] = self.heap.pop()
        index = 0
        length = self.heap.length()
        left = 2*index + 1
        right = 2*index + 2
        # as long as not a leaf node, keeps swapping down until finds it's spot
        while right < length or left < length:
            # if no right node, then swaps left node, else returns removed
            if right > length - 1:
                if self.heap[index] > self.heap[left]:
                    self.heap.swap(index, left)
                    index = left
                else:
                    return removed

            # continues to swap down with lesser of two children
            else:
                if self.heap[left] <= self.heap[right]:
                    lesser = left
                else:
                    lesser = right

                if self.heap[index] > self.heap[lesser]:
                    self.heap.swap(index, lesser)
                    index = lesser
                else:
                    return removed

            left = 2 * index + 1
            right = 2 * index + 2

        return removed

    def build_heap(self, da: DynamicArray) -> None:
        """
        builds new heap with given unordered dynamic array, overwrites previous heap.
        """
        self.heap = DynamicArray()
        for i in range(da.length()):
            self.heap.append(da[i])   # puts unordered heap as new heap
        length = self.heap.length()
        non_leaf = length//2   # finds first non_leaf node
        while non_leaf > 0:
            # checks all non_leaf nodes to percolate down if they need to
            non_leaf -= 1
            left = 2 * non_leaf + 1
            right = 2 * non_leaf + 2
            while right < length or left < length:
                # if only left child available
                if right > length - 1:
                    if self.heap[non_leaf] > self.heap[left]:
                        self.heap.swap(non_leaf, left)
                    break

                # if both left and right available, finds lesser
                else:
                    if self.heap[left] <= self.heap[right]:
                        lesser = left
                    else:
                        lesser = right

                    if self.heap[non_leaf] > self.heap[lesser]:
                        self.heap.swap(non_leaf, lesser)
                        non_leaf = lesser
                        left = 2 * non_leaf + 1
                        right = 2 * non_leaf + 2
                    # if no lesser value moves to next inner node (non-leaf)
                    else:
                        break

# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)


    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())


    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())


    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
