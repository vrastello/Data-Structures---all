# Course: CS261 - Data Structures
# Student Name: Vincent Rastello
# Assignment: A2, Dynamic Array and ADT's Implementation
# Description: Created Dynamic Array with methods similar to python's built in dynamic array.
# Last revised: 02-03-21


from static_array import *


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.size = 0
        self.capacity = 4
        self.first = 0  # do not use / change this value
        self.data = StaticArray(self.capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self.size) + "/" + str(self.capacity) + ' ['
        out += ', '.join([str(self.data[_]) for _ in range(self.size)])
        return out + ']'

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        return self.data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        self.data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size

    # ------------------------------------------------------------------ #

    def resize(self, new_capacity: int) -> None:
        """
        If underlying data structure capacity is less than new size, creates new data structure
        with double capacity and overwrites initial array.
        """
        if (new_capacity >= 1) and (new_capacity >= self.size):
            new_data = StaticArray(new_capacity)
            if not self.is_empty():
                for i in range(self.size):
                    new_data[i] = self.data[i]

            self.capacity = new_capacity
            self.data = new_data

    def append(self, value: object) -> None:
        """
        Adds new value to end of dynamic array, if array size is at capacity, it re-sizes.
        """
        if self.size == self.capacity:
            self.resize(self.capacity * 2)

        self.data[self.size] = value
        self.size += 1

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Inserts value at given index, shifts array to accommodate new item. Re-sizes if necessary.
        """
        if index > self.size or index < 0:
            raise DynamicArrayException
        if self.size == self.capacity:
            self.resize(self.capacity * 2)
        # if adding to end of array not shifting necessary
        if index == self.size:
            self.data[index] = value
            self.size += 1
        else:
            # shifts to the right starting at end of array, puts new value in open slot.
            for i in range(self.size - 1, index - 1, -1):
                self.data[i + 1] = self.data[i]
            self.data[index] = value
            self.size += 1

    def remove_at_index(self, index: int) -> None:
        """
        Removes value at given index by shifting values to the left to overwrite. Sets last value to None
        If size is under 1/4 capacity, shrinks capacity to size*2, with a minimum capacity of 10.
        """
        if index > self.size - 1 or index < 0:
            raise DynamicArrayException
        if self.capacity > 10:
            if self.size < self.capacity/4:
                if self.size * 2 >= 10:
                    self.capacity = self.size * 2
                else:
                    self.capacity = 10
        # shifts values from right to left overwriting deleted index, sets last item to None.
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]

        self.data[self.size - 1] = None
        self.size -= 1

    def slice(self, start_index: int, size: int) -> object:
        """
        Returns new dynamic array starting at given index with given size.
        """
        # validates size is positive integer and start index is [0, N-1)
        new_array = DynamicArray()
        if (size < 0) or (start_index < 0 or start_index > self.size - 1):
            raise DynamicArrayException
        # validates start index plus size does not extend out of bounds
        if (start_index + size) > self.size:
            raise DynamicArrayException
        for i in range(start_index, start_index + size):
            new_array.append(self.data[i])

        return new_array

    def merge(self, second_da: object) -> None:
        """
        Appends values from given array to self array in current order.
        """
        for i in range(second_da.length()):
            self.append(second_da[i])

    def map(self, map_func) -> object:
        """
        Iterates through array applying given function, saves data in new dynamic array.
        """
        new_array = DynamicArray()
        for i in range(self.size):
            new_array.append(map_func(self.data[i]))

        return new_array

    def filter(self, filter_func) -> object:
        """
        Iterates through array applying given function to filter, saves filtered data in new array.
        """
        new_array = DynamicArray()
        for i in range(self.size):
            if filter_func(self.data[i]):
                new_array.append(self.data[i])

        return new_array

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        Iterates through array applying sequential function. Returns resulting value.
        """
        # If array is empty returns initializer
        if self.is_empty():
            return initializer

        # starts at initializer or first item in array
        if initializer is None:
            output = self.data[0]
        else:
            output = reduce_func(initializer, self.data[0])

        # applies function to first two values then applies that result to next value etc.
        for i in range(1, self.size):
            output = reduce_func(output, self.data[i])

        return output

# BASIC TESTING
if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.resize(8)
    print(da.size, da.capacity, da.data)
    da.resize(2)
    print(da.size, da.capacity, da.data)
    da.resize(0)
    print(da.size, da.capacity, da.data)


    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)


    print("\n# append - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.append(1)
    print(da.size, da.capacity, da.data)
    print(da)


    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)


    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.size)
    print(da.capacity)


    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    print(da)
    da.insert_at_index(0, 300)
    print(da)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)


    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)


    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)


    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.size, da.capacity)
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)


    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.size, da.capacity)
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.size, da.capacity)

    for i in range(14):
        print("Before remove_at_index(): ", da.size, da.capacity, end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.size, da.capacity)


    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)


    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")


    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")


    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)


    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)


    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2

    def square(value):
        return value ** 2

    def cube(value):
        return value ** 3

    def plus_one(value):
        return value + 1

    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))


    print("\n# filter example 1")
    def filter_a(e):
        return e > 10

    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))


    print("\n# filter example 2")
    def is_long_word(word, length):
        return len(word) > length

    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))


    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))


    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))