# Course: CS261 - Data Structures
# Student Name: Vincent Rastello
# Assignment: A2, Dynamic Array and ADT's Implementation
# Description: Stack ADT, has methods to push, pop or return value at top. Uses dynamic array.
# Last revised: 02-03-21

from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "STACK: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da[i]) for i in range(self.da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da.length()

    # ------------------------------------------------------------------ #

    def push(self, value: object) -> None:
        """
        Pushes value to top of stack ADT, using underlying dynamic array method append.
        """
        self.da.append(value)

    def pop(self) -> object:
        """
        Pops value off top of stack ADT, returns popped value. If stack empty raises error.
        """
        if self.is_empty():
            raise StackException
        pop = self.da[self.size() - 1]
        self.da.remove_at_index(self.size() - 1)
        return pop

    def top(self) -> object:
        """
        Returns value at top of stack, raises error if stack is empty.
        """
        if self.is_empty():
            raise StackException
        top = self.da[self.size() - 1]
        return top



# BASIC TESTING
if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))

    for value in [1, 2, 3, 4, 5]:
        s.push(value)

    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))

    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)
