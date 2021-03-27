# Course: CS261 - Data Structures
# Student Name: Vincent Rastello
# Assignment: Assignment 3
# Description: Singly Linked List Data Structure with two sentinels, written all recursively



class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class SLNode:
    """
    Singly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with front and back sentinels
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.head = SLNode(None)
        self.tail = SLNode(None)
        self.head.next = self.tail

        # populate SLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        if self.head.next != self.tail:
            cur = self.head.next.next
            out = out + str(self.head.next.value)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
            length += 1
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.head.next == self.tail

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        Adds give value in a node to the front of linked list
        """
        node = SLNode(value)
        node.next = self.head.next
        self.head.next = node

    def rec_add_back(self, value: object, cur):
        """Recursive add back helper function"""
        node = SLNode(value)
        if cur.next == self.tail:
            node.next = self.tail
            cur.next = node

        else:
            return self.rec_add_back(value, cur.next)

    def add_back(self, value: object) -> None:
        """Calls the recursive function of add back"""
        return self.rec_add_back(value, self.head)

    def rec_insert_at_index(self, index, value, prev):
        """
        Helper Function Recursively inserts given value at given index in list.
        """
        if index < 0 or index > self.length():
            raise SLLException

        node = SLNode(value)
        cur = prev.next

        if index == 0:
            node.next = cur
            prev.next = node

        else:
            index -= 1
            return self.rec_insert_at_index(index, value, prev.next)

    def insert_at_index(self, index: int, value: object) -> None:
        """
        call helper function for insert
        """
        return self.rec_insert_at_index(index, value, self.head)

    def remove_front(self) -> None:
        """
        Removes front of list
        """
        if self.is_empty():
            raise SLLException

        new_next = self.head.next.next
        self.head.next = new_next

    def rec_remove_back(self, cur):
        """
        Recursive function to remove back of list
        """
        if self.is_empty():
            raise SLLException
        if cur.next.next == self.tail:
            cur.next = self.tail
        else:
            return self.rec_remove_back(cur.next)

    def remove_back(self) -> None:
        """
        Helper function calls recursive function
        """
        return self.rec_remove_back(self.head)

    def rec_remove_at_index(self, index, prev):
        """
        Recursive function removes node at index
        """
        if index < 0 or index > self.length() - 1:
            raise SLLException

        cur = prev.next
        if index == 0:
            prev.next = cur.next
        else:
            index -= 1
            return self.rec_remove_at_index(index, prev.next)

    def remove_at_index(self, index: int) -> None:
        """
        Helper function calls rec remove at index
        """
        return self.rec_remove_at_index(index, self.head)

    def get_front(self) -> object:
        """
        Returns front of list value
        """
        if self.is_empty():
            raise SLLException

        return self.head.next.value

    def rec_get_back(self, cur):
        """
        Recursive function to return back of list value
        """
        if self.is_empty():
            raise SLLException
        if cur.next == self.tail:
            return cur.value
        else:
            return self.rec_get_back(cur.next)

    def get_back(self) -> object:
        """
        Helper function to return back of list
        """
        return self.rec_get_back(self.head)

    def rec_remove(self, value, prev):
        """
        Recursive function to remove node of list that contains value.
        """
        cur = prev.next
        if cur == self.tail:
            return False
        if cur.value == value:
            prev.next = cur.next
            return True
        else:
            return self.rec_remove(value, prev.next)

    def remove(self, value: object) -> bool:
        """
        Recursive function that calls remove function
        """
        return self.rec_remove(value, self.head)

    def rec_count(self, value, cur, count):
        """
        Recursive function that counts incidents of value in list
        """
        if cur.value == value:
            count += 1
        if cur.next == self.tail:
            return count
        else:
            return self.rec_count(value, cur.next, count)

    def count(self, value: object) -> int:
        """
        Helper function calls rec count
        """
        return self.rec_count(value, self.head, 0)

    def rec_slice(self, start_index, size, cur, new_list):
        """
        Recursive function that returns slice of list with given size and start index
        """
        length = self.length()
        if start_index < 0 or start_index > length - 1 or size < 0:
            raise SLLException
        if start_index + size > length:
            raise SLLException

        if start_index == 0:
            if size == 0:
                return new_list
            else:
                new_list.add_back(cur.value)
                size -= 1
                return self.rec_slice(start_index, size, cur.next, new_list)
        else:
            start_index -= 1
            return self.rec_slice(start_index, size, cur.next, new_list)

    def slice(self, start_index: int, size: int) -> object:
        """
        Recursive helper function that calls slice function
        """
        new_list = LinkedList()
        cur = self.head.next
        return self.rec_slice(start_index, size, cur, new_list)









if __name__ == '__main__':
    pass

    print('\n# add_front example 1')
    list = LinkedList()
    print(list)
    list.add_front('A')
    list.add_front('B')
    list.add_front('C')
    print(list)

    print('\n# add_back example 1')
    list = LinkedList()
    print(list)
    list.add_back('C')
    list.add_back('B')
    list.add_back('A')
    print(list)


    print('\n# insert_at_index example 1')
    list = LinkedList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            list.insert_at_index(index, value)
            print(list)
        except Exception as e:
            print(type(e))


    print('\n# remove_front example 1')
    list = LinkedList([1, 2])
    print(list)
    for i in range(3):
        try:
            list.remove_front()
            print('Successful removal', list)
        except Exception as e:
            print(type(e))


    print('\n# remove_back example 1')
    list = LinkedList()
    try:
        list.remove_back()
    except Exception as e:
        print(type(e))
    list.add_front('Z')
    list.remove_back()
    print(list)
    list.add_front('Y')
    list.add_back('Z')
    list.add_front('X')
    print(list)
    list.remove_back()
    print(list)


    print('\n# remove_at_index example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6])
    print(list)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            list.remove_at_index(index)
            print(list)
        except Exception as e:
            print(type(e))
    print(list)


    print('\n# get_front example 1')
    list = LinkedList(['A', 'B'])
    print(list.get_front())
    print(list.get_front())
    list.remove_front()
    print(list.get_front())
    list.remove_back()
    try:
        print(list.get_front())
    except Exception as e:
        print(type(e))


    print('\n# get_back example 1')
    list = LinkedList([1, 2, 3])
    list.add_back(4)
    print(list.get_back())
    list.remove_back()
    print(list)
    print(list.get_back())


    print('\n# remove example 1')
    list = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(list)
    for value in [7, 3, 3, 3, 3]:
        print(list.remove(value), list.length(), list)


    print('\n# count example 1')
    list = LinkedList([1, 2, 3, 1, 2, 2])
    print(list, list.count(1), list.count(2), list.count(3), list.count(4))


    print('\n# slice example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = list.slice(1, 3)
    print(list, ll_slice, sep="\n")
    ll_slice.remove_at_index(0)
    print(list, ll_slice, sep="\n")


    print('\n# slice example 2')
    list = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", list)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Slice", index, "/", size, end="")
        try:
            print(" --- OK: ", list.slice(index, size))
        except:
            print(" --- exception occurred.")

