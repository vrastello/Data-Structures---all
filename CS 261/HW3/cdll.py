# Course: CS261 - Data Structures
# Student Name: Vincent Rastello
# Assignment: 3
# Description: Circular double linked list data structure with one sentinel


class CDLLException(Exception):
    """
    Custom exception class to be used by Circular Doubly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DLNode:
    """
    Doubly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        self.next = None
        self.prev = None
        self.value = value


class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with sentinel
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sentinel = DLNode(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate CDLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'CDLL ['
        if self.sentinel.next != self.sentinel:
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.value)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list

        This can also be used as troubleshooting method. This method works
        by independently measuring length during forward and backward
        traverse of the list and return the length if results agree or error
        code of -1 or -2 if thr measurements are different.

        Return values:
        >= 0 - length of the list
        -1 - list likely has an infinite loop (forward or backward)
        -2 - list has some other kind of problem

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        # length of the list measured traversing forward
        count_forward = 0
        cur = self.sentinel.next
        while cur != self.sentinel and count_forward < 101_000:
            count_forward += 1
            cur = cur.next

        # length of the list measured traversing backwards
        count_backward = 0
        cur = self.sentinel.prev
        while cur != self.sentinel and count_backward < 101_000:
            count_backward += 1
            cur = cur.prev

        # if any of the result is > 100,000 -> list has a loop
        if count_forward > 100_000 or count_backward > 100_000:
            return -1

        # if counters have different values -> there is some other problem
        return count_forward if count_forward == count_backward else -2

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.sentinel.next == self.sentinel

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        Adds node with given value to front of list
        """
        node = DLNode(value)
        node.next = self.sentinel.next
        node.prev = self.sentinel
        self.sentinel.next.prev = node
        self.sentinel.next = node

    def add_back(self, value: object) -> None:
        """
        adds node with given value to front of list
        """
        node = DLNode(value)
        node.next = self.sentinel
        node.prev = self.sentinel.prev
        self.sentinel.prev = node
        self.sentinel.prev.prev.next = node

    def insert_at_index(self, index: int, value: object) -> None:
        """
        inserts node with given value at given index
        """
        if index < 0 or index > self.length():
            raise CDLLException

        node = DLNode(value)
        cur = self.sentinel.next

        for i in range(index):
            cur = cur.next

        node.next = cur
        node.prev = cur.prev
        cur.prev.next = node
        cur.prev = node

    def remove_front(self) -> None:
        """
        removes front node of linked list
        """
        if self.is_empty():
            raise CDLLException

        self.sentinel.next = self.sentinel.next.next
        self.sentinel.next.prev = self.sentinel

    def remove_back(self) -> None:
        """
        removes last node of linked list
        """
        if self.is_empty():
            raise CDLLException

        self.sentinel.prev.prev.next = self.sentinel
        self.sentinel.prev = self.sentinel.prev.prev

    def remove_at_index(self, index: int) -> None:
        """
        removes node at given index
        """
        if index < 0 or index > self.length() - 1:
            raise CDLLException

        cur = self.sentinel.next
        for i in range(index):
            cur = cur.next

        cur.prev.next = cur.next
        cur.next.prev = cur.prev

    def get_front(self) -> object:
        """
        returns value of node at front of list
        """
        if self.is_empty():
            raise CDLLException

        return self.sentinel.next.value

    def get_back(self) -> object:
        """
        returns value of node at last item of list
        """
        if self.is_empty():
            raise CDLLException

        return self.sentinel.prev.value

    def remove(self, value: object) -> bool:
        """
        removes first node in list with given value, returns true or false if removed or not
        """
        cur = self.sentinel.next

        while cur != self.sentinel:
            if cur.value == value:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                return True
            cur = cur.next

        return False

    def count(self, value: object) -> int:
        """
        returns count of given value in list
        """
        cur = self.sentinel.next
        count = 0

        while cur != self.sentinel:
            if cur.value == value:
                count += 1
            cur = cur.next

        return count

    def swap_pairs(self, index1: int, index2: int) -> None:
        """
        Swaps two nodes at the given index's, does not change values of nodes
        """
        if index1 < 0 or index1 > self.length() - 1:
            raise CDLLException
        if index2 < 0 or index2 > self.length() - 1:
            raise CDLLException

        node1 = self.sentinel.next
        for i in range(index1):
            node1 = node1.next

        node2 = self.sentinel.next
        for i in range(index2):
            node2 = node2.next

        after_node1 = node1.next
        before_node1 = node1.prev
        after_node2 = node2.next
        before_node2 = node2.prev

        if before_node2 == node1:
            before_node2 = node2
            after_node1 = node1

        if after_node2 == node1:
            after_node2 = node2
            before_node1 = node1
            
        node1.next = after_node2
        node1.prev = before_node2
        node2.next = after_node1
        node2.prev = before_node1
        node2.prev.next = node2
        node2.next.prev = node2
        node1.prev.next = node1
        node1.next.prev = node1

    def reverse(self) -> None:
        """
        Reverses order of nodes in linked list
        """
        forward = self.sentinel.next
        back = self.sentinel.prev

        for i in range(self.length()//2):
            after_forward = forward.next
            before_forward = forward.prev
            after_back = back.next
            before_back = back.prev

            if before_back == forward:
                before_back = back
                after_forward = forward

            forward.next = after_back
            forward.prev = before_back
            back.next = after_forward
            back.prev = before_forward
            back.prev.next = back
            back.next.prev = back
            forward.prev.next = forward
            forward.next.prev = forward

            forward = after_forward
            back = before_back

    def sort(self) -> None:
        """
        Uses insertion sort to sort linked list
        """
        key = self.sentinel.next
        next_index = key.next
        for i in range(self.length() - 1):
            key = next_index
            j = key.prev
            next_index = key.next
            if key.value < j.value:
                j.next = key.next
                j.next.prev = j
                while j != self.sentinel and key.value < j.value:
                    j = j.prev
                key.next = j.next
                key.prev = j
                key.next.prev = key
                j.next = key

    def rotate(self, steps: int) -> None:
        """
        TODO: Write this implementation
        """
        if not self.is_empty():
            steps = steps % self.length()
            for i in range(steps):
                new_front = self.sentinel.prev
                self.remove_back()
                new_front.next = self.sentinel.next
                new_front.prev = self.sentinel
                self.sentinel.next.prev = new_front
                self.sentinel.next = new_front

    def remove_duplicates(self) -> None:
        """
        If duplicate value found, removes all values of that type. Leaves only unique values in list
        """
        cur = self.sentinel.next

        while cur != self.sentinel:
            if cur.value == cur.next.value:
                while cur.value == cur.next.value:
                    cur.next = cur.next.next
                    cur.next.prev = cur
                cur.prev.next = cur.next
                cur.next.prev = cur.prev

            cur = cur.next

    def odd_even(self) -> None:
        """
        Sorts list with odd index's first in order, then even indexes after that in order
        """
        index_1 = self.sentinel.next.next
        index_2 = self.sentinel.next

        while index_2.next != self.sentinel:
            index_2 = index_2.next
            if index_2.next != self.sentinel:
                index_1.prev.next = index_2.next
                index_2.next.prev = index_1.prev
                index_1.prev = index_2.next
                index_2.next = index_2.next.next
                index_1.prev.next = index_1
                index_2.next.prev = index_2

    def add_integer(self, num: int) -> None:
        """
        self is list that represents a number, adds given integer to it, the list represents a number with
        ascending digits from left to right.
        """
        n = num
        cur = self.sentinel

        while n > 0:
            if cur.prev == self.sentinel:
                self.add_front(0)
            cur = cur.prev
            add = n % 10
            n //= 10
            cur.value += add
            if cur.value >= 10:
                carry_over = cur
                while carry_over.value >= 10:
                    remainder = carry_over.value % 10
                    carry_over.value = remainder
                    if carry_over.prev == self.sentinel:
                        self.add_front(0)
                    carry_over.prev.value += 1
                    carry_over = carry_over.prev


if __name__ == '__main__':
    pass

    print('\n# add_front example 1')
    lst = CircularList()
    print(lst)
    lst.add_front('A')
    lst.add_front('B')
    lst.add_front('C')
    print(lst)

    print('\n# add_back example 1')
    lst = CircularList()
    print(lst)
    lst.add_back('C')
    lst.add_back('B')
    lst.add_back('A')
    print(lst)

    print('\n# insert_at_index example 1')
    lst = CircularList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print('\n# remove_front example 1')
    lst = CircularList([1, 2])
    print(lst)
    for i in range(3):
        try:
            lst.remove_front()
            print('Successful removal', lst)
        except Exception as e:
            print(type(e))

    print('\n# remove_back example 1')
    lst = CircularList()
    try:
        lst.remove_back()
    except Exception as e:
        print(type(e))
    lst.add_front('Z')
    lst.remove_back()
    print(lst)
    lst.add_front('Y')
    lst.add_back('Z')
    lst.add_front('X')
    print(lst)
    lst.remove_back()
    print(lst)

    print('\n# remove_at_index example 1')
    lst = CircularList([1, 2, 3, 4, 5, 6])
    print(lst)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))
    print(lst)

    print('\n# get_front example 1')
    lst = CircularList(['A', 'B'])
    print(lst.get_front())
    print(lst.get_front())
    lst.remove_front()
    print(lst.get_front())
    lst.remove_back()
    try:
        print(lst.get_front())
    except Exception as e:
        print(type(e))

    print('\n# get_back example 1')
    lst = CircularList([1, 2, 3])
    lst.add_back(4)
    print(lst.get_back())
    lst.remove_back()
    print(lst)
    print(lst.get_back())

    print('\n# remove example 1')
    lst = CircularList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(lst)
    for value in [7, 3, 3, 3, 3]:
        print(lst.remove(value), lst.length(), lst)

    print('\n# count example 1')
    lst = CircularList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print('\n# swap_pairs example 1')
    lst = CircularList([0, 1, 2, 3, 4, 5, 6])
    test_cases = ((0, 6), (0, 7), (-1, 6), (1, 5),
                  (4, 2), (3, 3), (1, 2), (2, 1))

    for i, j in test_cases:
        print('Swap nodes ', i, j, ' ', end='')
        try:
            lst.swap_pairs(i, j)
            print(lst)
        except Exception as e:
            print(type(e))

    print('\n# reverse example 1')
    test_cases = (
        [1, 2, 3, 3, 4, 5],
        [1, 2, 3, 4, 5],
        ['A', 'B', 'C', 'D']
    )
    for case in test_cases:
        lst = CircularList(case)
        lst.reverse()
        print(lst)

    print('\n# reverse example 2')
    lst = CircularList()
    print(lst.length())
    print(lst)
    lst.reverse()
    print(lst.length())
    print(lst)
    lst.add_back(2)
    print(lst.length())
    lst.add_back(3)
    print(lst.length())
    lst.add_front(1)
    print(lst.length())
    lst.reverse()
    print(lst.length())
    print(lst)

    print('\n# reverse example 3')
    class Student:
        def __init__(self, name, age):
            self.name, self.age = name, age

        def __eq__(self, other):
            return self.age == other.age

        def __str__(self):
             return str(self.name) + ' ' + str(self.age)


    s1, s2 = Student('John', 20), Student('Andy', 20)
    lst = CircularList([s1, s2])
    print(lst)
    lst.reverse()
    print(lst)
    print(s1 == s2)

    print('\n# reverse example 4')
    lst = CircularList([1, 'A'])
    lst.reverse()
    print(lst)

    print('\n# sort example 1')
    test_cases = (
        [1, 10, 2, 20, 3, 30, 4, 40, 5],
        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
        [(1, 1), (20, 1), (1, 20), (2, 20)]
    )
    for case in test_cases:
        lst = CircularList(case)
        print(lst)
        lst.sort()
        print(lst)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    for steps in [1, 2, 0, -1, -2, 28, -100]:
        lst = CircularList(source)
        lst.rotate(steps)
        print(lst, steps)

    print('\n# rotate example 2')
    lst = CircularList([10, 20, 30, 40])
    for j in range(-1, 2, 2):
        for _ in range(3):
            lst.rotate(j)
            print(lst)

    print('\n# rotate example 3')
    lst = CircularList()
    lst.rotate(10)
    print(lst)

    print('\n# remove_duplicates example 1')
    test_cases = (
        [1, 2, 3, 4, 5], [1, 1, 1, 1, 1],
        [], [1], [1, 1], [1, 1, 1, 2, 2, 2],
        [0, 1, 1, 2, 3, 3, 4, 5, 5, 6],
        list("abccd"),
        list("005BCDDEEFI")
    )

    for case in test_cases:
        lst = CircularList(case)
        print('INPUT :', lst)
        lst.remove_duplicates()
        print('OUTPUT:', lst)

    print('\n# odd_even example 1')
    test_cases = (
        [1, 2, 3, 4, 5], list('ABCDE'),
        [], [100], [100, 200], [100, 200, 300],
        [100, 200, 300, 400],
        [10, 'A', 20, 'B', 30, 'C', 40, 'D', 50, 'E']
    )

    for case in test_cases:
        lst = CircularList(case)
        print('INPUT :', lst)
        lst.odd_even()
        print('OUTPUT:', lst)

    print('\n# add_integer example 1')
    test_cases = (
      ([1, 2, 3], 10456),
      ([], 25),
      ([2, 0, 9, 0, 7], 108),
      ([9, 9, 9], 9_999_999),
    )
    for list_content, integer in test_cases:
        lst = CircularList(list_content)
        print('INPUT :', lst, 'INTEGER', integer)
        lst.add_integer(integer)
        print('OUTPUT:', lst)
