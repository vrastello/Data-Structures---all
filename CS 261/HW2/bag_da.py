# Course: CS261 - Data Structures
# Student Name: Vincent Rastello
# Assignment: A2, Dynamic Array and ADT's Implementation
# Description: Bag ADT, a non-ordered container with methods to add, remove, count, clear and compare
# two bags for equality. Uses dynamic array as underlying data structure.
# Last revised: 02-03-21

from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS CLASS IN ANY WAY
        """
        return self.da.length()

    def add(self, value: object) -> None:
        """
        Appends value to underlying dynamic array in order to add value to bag ADT.
        """
        self.da.append(value)

    def remove(self, value: object) -> bool:
        """
        Iterates through underlying dynamic array and applies remove_at_index method to first
        matching value it finds. Returns True if value found, false if not.
        """
        for i in range(self.size()):
            if self.da[i] == value:
                self.da.remove_at_index(i)
                return True

        return False

    def count(self, value: object) -> int:
        """
        Iterates through underlying dynamic array and counts incidents of target value. Returns count.
        """
        count = 0
        for i in range(self.size()):
            if self.da[i] == value:
                count += 1

        return count

    def clear(self) -> None:
        """
        Overwrites underlying dynamic array to empty dynamic array.
        """
        self.da = DynamicArray()

    def equal(self, second_bag: object) -> bool:
        """
        Compares two bags to check for equality, ie if all items and amounts of items are the same.
        Returns true if equal, false if not.
        """
        # if a bag is empty, checks if both are empty and returns true, if only one is empty--false.
        if self.da.is_empty() or second_bag.da.is_empty():
            if second_bag.da.is_empty() and self.da.is_empty():
                return True
            else:
                return False
        # checks for bigger bag, uses bigger bag as outer loop so no items are missed.
        if self.size() >= second_bag.size():
            big_bag = self
            small_bag = second_bag
        else:
            big_bag = second_bag
            small_bag = self
        # Outer loop checks each item in inner loop for equality, if equal checks count in both bags.
        for i in range(big_bag.size()):
            for j in range(small_bag.size()):
                if big_bag.da[i] == small_bag.da[j]:
                    if big_bag.count(big_bag.da[i]) != small_bag.count(small_bag.da[j]):
                        return False
                    # if count is equal breaks loop and goes to next value in outer loop
                    else:
                        break
                # if no equal value found, bags are not equal
                if j == small_bag.size() - 1:
                    return False

        return True




# BASIC TESTING
if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))
