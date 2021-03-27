# Course: CS261 - Data Structures
# Student Name: Vincent Rastello
# Assignment: 3
# Description: Queue Data structure using max stack data structure underneath, which has linked list data structure
# under that


from max_stack_sll import *


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Init new Queue based on two stacks
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.s1 = MaxStack()  # use as main storage
        self.s2 = MaxStack()  # use as temp storage

    def __str__(self) -> str:
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "QUEUE: " + str(self.s1.size()) + " elements. "
        out += str(self.s1)
        return out

    def is_empty(self) -> bool:
        """
        Return True if queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.s1.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.s1.size()

    # ------------------------------------------------------------------ #

    def enqueue(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        self.s1.push(value)

    def dequeue(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.s1.is_empty():
            raise QueueException

        for i in range(self.size()):
            self.s2.push(self.s1.pop())

        pop_val = self.s2.pop()

        for i in range(self.s2.size()):
            self.s1.push(self.s2.pop())

        return pop_val




# BASIC TESTING
if __name__ == "__main__":
    pass

    print('\n# enqueue example 1')
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print('\n# dequeue example 1')
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue(), q)
        except Exception as e:
            print("No elements in queue", type(e))



