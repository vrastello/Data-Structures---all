# Course: CS261 - Data Structures
# Student Name: Vince Rastello
# Assignment: Assignment 1, Python Fundamentals Review
# Description: 14 problems reviewing python fundamentals and emphasizing speed and optimization. Unable
#               to use any built in data structures or methods, must use attached class only.

import random
import string
from a1_include import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------


def min_max(arr: StaticArray) -> ():
    """
    Tests for single value in array, if so returns tuple. Then sets first value in array to min and max. Iterates
    through array, if greater or less sets new min/max. Returns min max tuple after loop.
    """
    if arr.size() == 1:
        output = (arr[0], arr[0])
        return output

    max_val = arr[0]
    min_val = arr[0]

    for index in range(arr.size()):
        if arr[index] > max_val:
            max_val = arr[index]
        if arr[index] < min_val:
            min_val = arr[index]

    output = (min_val, max_val)
    return output


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------


def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    Iterates through given array and checks if divisible by target numbers, if true places fizzbuzz words into new array
    if not true adds original number in new array.
    """
    new_arr = StaticArray(arr.size())

    for index in range(arr.size()):
        if arr[index] % 15 == 0:
            new_arr[index] = 'fizzbuzz'
            continue
        elif arr[index] % 5 == 0:
            new_arr[index] = 'buzz'
        elif arr[index] % 3 == 0:
            new_arr[index] = 'fizz'
        else:
            new_arr[index] = arr[index]

    return new_arr


# ------------------- PROBLEM 3 - REVERSE -----------------------------------


def reverse(arr: StaticArray) -> None:
    """
    iterates through half of array size using floor division (for odd size array--median number will stay in middle),
    points first and last to variables, then assigns values to opposite indexes
    """
    for index in range(arr.size() // 2):
        first = arr[index]
        last = arr[arr.size() - 1 - index]  # uses index value - array size to iterate through backwards
        arr[index] = last
        arr[arr.size() - 1 - index] = first


# ------------------- PROBLEM 4 - ROTATE ------------------------------------


def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    creates new array of same size, then equates steps to steps remainder of array size. All steps greater than array
    size will use remainder to get to end location. Negative remainders add steps in positive direction but end in
    same spot as if they had gone to the left. If indexing past end of array subtract array size to end at correct index
    """
    new_arr = StaticArray(arr.size())
    for index in range(arr.size()):
        steps = steps % arr.size()

        if steps + index <= arr.size() - 1:
            new_arr[steps + index] = arr[index]
        # if indexing out of bounds:
        else:
            new_index = index + steps - arr.size()
            new_arr[new_index] = arr[index]

    return new_arr


# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------


def sa_range(start: int, end: int) -> StaticArray:
    """
    Takes range and creates array counting down or up from start to end number. Checks if start or end is greater. Then
    establishes size by subtracting smaller amount and adding one to be inclusive. Then creates new array and adds
    descending or ascending values using iterative method.
    """
    if start > end:
        size = start - end + 1
        new_arr = StaticArray(size)
        for index in range(size):
            new_arr[index] = start
            start -= 1

    elif start < end:
        size = end - start + 1
        new_arr = StaticArray(size)
        for index in range(size):
            new_arr[index] = start
            start += 1

    else:
        new_arr = StaticArray(1)
        new_arr[0] = start

    return new_arr


# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------


def is_sorted(arr: StaticArray) -> int:
    """
    Checks if array is sorted. Returns 1 if ascending, 2 if descending, 0 if not.
    Uses helper functions ascending and descending to determine if array is strictly one or the other.
    """

    def ascending(array):
        """checks if array is in ascending order"""
        for index in range(array.size() - 1):
            if arr[index] >= arr[index + 1]:
                return False

        return True

    def descending(array):
        """checks if array is in descending order"""
        for index in range(array.size() - 1):
            if arr[index] <= arr[index + 1]:
                return False

        return True

    if arr.size() == 1:
        return 1
    if ascending(arr) is True:
        return 1
    if descending(arr) is True:
        return 2

    return 0


# ------------------- PROBLEM 7 - SA_SORT -----------------------------------


def sa_sort(arr: StaticArray) -> None:
    """
    This uses simple insertion sort to sort values in array in ascending order.
    """
    for index in range(1, arr.size()):
        value = arr[index]
        pos = index - 1
        while pos >= 0 and arr[pos] > value:
            arr[pos + 1] = arr[pos]
            pos -= 1
        arr[pos + 1] = value


# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------


def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    Removes duplicates of original array and returns unique values in new array. Iterates through original array
    counting unique values, sets count to new array size. Creates new array, sets first index's equal. Sets new index
    count to one, iterates through original array adding unique values at new index.
    """

    # starting at second value checks previous value for equality, if equal skips, if not adds to size of new array
    new_size = 1
    for index in range(1, arr.size()):
        if arr[index] == arr[index - 1]:
            continue
        new_size += 1

    # creates array using found size
    new_arr = StaticArray(new_size)
    new_arr[0] = arr[0]
    new_index = 1

    # uses same method to iterate through original array and add to new array.
    for index in range(1, arr.size()):
        if arr[index] == arr[index - 1]:
            continue
        new_arr[new_index] = arr[index]
        new_index += 1

    return new_arr


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------


def count_sort(arr: StaticArray) -> StaticArray:
    """
    This is a descending count sort with negative values.
    """
    # finds min and max values of given array using min_max function
    max_element = min_max(arr)[1]
    min_element = min_max(arr)[0]

    # uses min and max to establish size of count array with negative values
    range_of_elements = max_element - min_element + 1

    # create count array and new array (output array)
    count_arr = StaticArray(range_of_elements)
    new_arr = StaticArray(arr.size())

    # fill count array with zero's so numbers can be added iteratively
    for index in range(range_of_elements):
        count_arr[index] = 0

    # store count of each number in count array using minimum element to offset for negative range
    for index in range(arr.size()):
        count_arr[arr[index] - min_element] += 1

    # change count array by adding values with previous value starting from end of array to create
    # descending order. Now count array contains position of element for new array
    for index in range(count_arr.size() - 2, -1, -1):
        count_arr[index] += count_arr[index + 1]

    # adds values in source array to new array using the value stored at count array (element position)
    # subtract one to account for unused starting position. Subtract from count array value so that
    # duplicate values are stored in the next index position.
    for index in range(arr.size() - 1, -1, -1):
        new_arr[count_arr[arr[index] - min_element] - 1] = arr[index]
        count_arr[arr[index] - min_element] -= 1

    return new_arr


# ------------------- PROBLEM 10 - SA_INTERSECTION --------------------------


def sa_intersection(arr1: StaticArray, arr2: StaticArray, arr3: StaticArray) -> StaticArray:
    """
    Finds intersection of three arrays and returns. Finds smallest array, then iterates through small array, if other
    two array's values are lower uses while loops to index to equal or greater than value in both arrays. If all equal
    adds to temporary static array, adds to a size counter and indexes all array's to next value. Then puts values in
    new array and uses size counter to set array length.
    """

    # These three lines find smallest array, names other arrays medium and large arbitrarily
    if (arr1.size() <= arr2.size()) and (arr1.size() <= arr3.size()):
        small, medium, large = arr1, arr2, arr3

    elif (arr2.size() <= arr1.size()) and (arr2.size() <= arr3.size()):
        small, medium, large = arr2, arr1, arr3

    else:
        small, medium, large = arr3, arr1, arr2

    temp_arr = StaticArray(small.size())
    count = 0
    index_2 = 0
    index_3 = 0

    # iterates through smaller array, increases index of other two arrays if they are less than value of smaller array.
    for index_1 in range(small.size()):
        while (small[index_1] > medium[index_2]) and (index_2 < medium.size() - 1):
            index_2 += 1

        while (small[index_1] > large[index_3]) and (index_3 < large.size() - 1):
            index_3 += 1

        # once all values are greater or equal to small array value, checks if all equal, if so adds to temp array.
        if small[index_1] == medium[index_2] == large[index_3]:
            temp_arr[count] = small[index_1]
            count += 1
            # if you have reached end of either larger arrays, don't keep checking for matching values
            if index_2 == medium.size() - 1 or index_3 == large.size() - 1:
                break
            index_2 += 1
            index_3 += 1

    # if no intersection found, returns special array with None value
    if count == 0:
        new_arr = StaticArray(1)
        new_arr[0] = None
        return new_arr

    # dumps values of temp array into new array and returns
    new_arr = StaticArray(count)
    for index in range(count):
        new_arr[index] = temp_arr[index]

    return new_arr


# ------------------- PROBLEM 11 - SORTED SQUARES ---------------------------


def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    Receives sorted list of numbers ranging from negative to positive and returns squared numbers in ascending order.
    Indexes from beginning and end of list at the same time.
    """
    square_arr = StaticArray(arr.size())

    # initializes three different indexes
    index_1 = 0     # for negative numbers if present
    index_2 = arr.size() - 1    # for positive values
    index_3 = square_arr.size() - 1     # actual index of values being added to new array

    # starting at beginning of array, if values are negative squares values and adds to end of new array if greater
    # or equal to the squared positive value at end of list. Inc/dec index values if they are added to list.
    while index_1 < arr.size() and arr[index_1] < 0:
        neg_square = arr[index_1] * arr[index_1]
        square = arr[index_2] * arr[index_2]

        if neg_square >= square:
            square_arr[index_3] = neg_square
            index_1 += 1
            index_3 -= 1

        # adds positive square to new list and increases/decreases indexes
        if neg_square < square:
            square_arr[index_3] = square
            index_2 -= 1
            index_3 -= 1

    # after negative values are added, continues adding positive values where they left off.
    while index_2 > -1 and arr[index_2] >= 0:
        square = arr[index_2] * arr[index_2]
        square_arr[index_3] = square
        index_2 -= 1
        index_3 -= 1

    return square_arr


# ------------------- PROBLEM 12 - ADD_NUMBERS ------------------------------


def add_numbers(arr1: StaticArray, arr2: StaticArray) -> StaticArray:
    """
    Translates numbers from list form to actual integer, adds integers then puts numbers into list form.
    """
    num_1 = 0
    num_2 = 0

    # sets digits of numbers to 10^array size - 1
    digit_1 = 10**(arr1.size() - 1)
    digit_2 = 10**(arr2.size() - 1)

    # these two loops multiply first digit by the 10's value, then add to number and divide digit value by 10 to loop
    # through all digits
    for index in range(arr1.size()):
        num_1 += int(arr1[index] * digit_1)
        digit_1 /= 10

    for index in range(arr2.size()):
        num_2 += int(arr2[index] * digit_2)
        digit_2 /= 10

    sum = num_1 + num_2
    n = sum
    new_digit = 0

    # finds number of digits in sum
    while n > 0:
        new_digit += 1
        n //= 10

    # sets return array to sum's digits, decreases digits and sets to 10^digits
    new_arr = StaticArray(new_digit)
    new_digit -= 1
    new_digit = 10**new_digit

    # finds first digit in number by floor division, then decreases by one digit using modulus. Adds values to array
    for index in range(new_arr.size()):
        new_arr[index] = int(sum//new_digit)
        sum %= new_digit
        new_digit /= 10

    return new_arr


# ------------------- PROBLEM 13 - BALANCED_STRINGS -------------------------


def balanced_strings(s: str) -> StaticArray:
    """
    Receives string and returns array with all possible slices of balanced strings. Iterates through string, tallies up
    letters count as it goes, once all are equal increments count variable. Then sets bottom index to current index,
    letters count to zero and scans through next area of text.
    """
    a, b, c, index_1, index_2, count, array_size = 0, 0, 0, 0, 0, 0, 0

    # sets temp array size
    for _ in s:
        array_size += 1

    # divided by three to save memory space since minimum length of string is 3.
    temp_arr = StaticArray(array_size//3)

    # increments index scanning array, increments a,b,c variables
    for letter in range(array_size):
        index_2 += 1

        if s[letter].lower() == 'a':
            a += 1

        if s[letter].lower() == 'b':
            b += 1

        if s[letter].lower() == 'c':
            c += 1

        # once letters are equal, saves slice in temp array, sets 'bottom' index to current index, resets all counts
        # and increments count variable which will be new array size.
        if a > 0 and a == b == c:
            temp_arr[count] = s[index_1:index_2]
            index_1 = index_2
            a, b, c = 0, 0, 0
            count += 1

    new_arr = StaticArray(count)

    for index in range(count):
        new_arr[index] = temp_arr[index]

    return new_arr

# ------------------- PROBLEM 14 - TRANSFORM_STRING -------------------------


def transform_string(source: str, s1: str, s2: str) -> str:
    """
    Transforms string using homework guidelines. For this problem I used slicing to replace the values at the correct
    indexes with the target values
    """
    for index in range(len(source)):

        # if character is in s1, inserts character in s2 at same index
        if source[index] in s1:
            s1_index = s1.index(source[index])
            source = source[:index] + s2[s1_index] + source[index + 1:]

        # all these elif statements check for target values and insert desired character using slice.
        elif source[index].isupper():
            source = source[:index] + ' ' + source[index + 1:]

        elif source[index].islower():
            source = source[:index] + '#' + source[index + 1:]

        elif source[index].isdigit():
            source = source[:index] + '!' + source[index + 1:]

        else:
            source = source[:index] + '=' + source[index + 1:]

    return source

# BASIC TESTING
if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(min_max(arr))

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(min_max(arr))

    print('\n# min_max example 3')
    arr = StaticArray(3)
    for i, value in enumerate([3, 3, 3]):
        arr[i] = value
    print(min_max(arr))

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    source = [_ for _ in range(-20, 15, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100]:
        print(rotate(arr, steps), steps)
    print(arr)

    source = [_ for _ in range(-10000, 10000, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1000000000]:
        print(rotate(arr, steps), steps)
    print(arr)

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-105, -99), (-99, -105)]
    for start, end in cases:
        print(start, end, sa_range(start, end))

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print('Result:', is_sorted(arr), arr)

    print('\n# sa_sort example 1')
    test_cases = (
        [1, 10, 2, 20, 3, 30, 4, 40, 5],
        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
        [(1, 1), (20, 1), (1, 20), (2, 20)],
        [random.randrange(-30000, 30000) for _ in range(5_000)]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr if len(case) < 50 else 'Started sorting large array')
        sa_sort(arr)
        print(arr if len(case) < 50 else 'Finished sorting large array')

    print('\n# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [random.randrange(-499, 499) for _ in range(1_000_000)]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr if len(case) < 50 else 'Started sorting large array')
        result = count_sort(arr)
        print(result if len(case) < 50 else 'Finished sorting large array')

    print('\n# sa_intersection example 1')
    test_cases = (
        ([-3, -3, 1, 4, 7, 7], [-10, -5, -3, 0, 0, 1, 7], [-9, -9, -3, -2, -1, 4, 7, 7, 7, 8]),
        ([-9, -5, -2, 1, 3, 5, 6, 7, 10], [-9, -8, -6, -3, 3], [-5, -3, 3, 10]),
        ([-7, -5, -4, -1, 3, 6, 9], [-7, -7, -6, -5, -2, -2, 2, 3], [-7, -4, -2, -1, 2, 4, 4, 5]),
        ([1, 2, 3], [3, 4, 5], [2, 3, 4]),
        ([1, 2], [2, 4], [3, 4]),
        ([1, 1, 2, 2, 5, 75], [1, 2, 2, 12, 75, 90], [-5, 2, 2, 2, 20, 75, 95])
    )
    for case in test_cases:
        arr = []
        for i, lst in enumerate(case):
            arr.append(StaticArray(len(lst)))
            for j, value in enumerate(sorted(lst)):
                arr[i][j] = value
        print(sa_intersection(arr[0], arr[1], arr[2]))

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
        [random.randrange(-10_000, 10_000) for _ in range(1_000_000)]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr if len(case) < 50 else 'Started sorting large array')
        result = sorted_squares(arr)
        print(result if len(case) < 50 else 'Finished sorting large array')

    print('\n# add_numbers example 1')
    test_cases = (
        ([1, 2, 3], [4, 5, 6]),
        ([0], [2, 5]),
        ([2, 0, 9, 0, 7], [1, 0, 8]),
        ([9, 9, 9], [9, 9, 9, 9])
    )
    for num1, num2 in test_cases:
        n1 = StaticArray(len(num1))
        n2 = StaticArray(len(num2))
        for i, value in enumerate(num1):
            n1[i] = value
        for i, value in enumerate(num2):
            n2[i] = value
        print('Original nums:', n1, n2)
        print('Sum: ', add_numbers(n1, n2))

    print('\n# balanced_strings example 1')
    test_cases = (
        'aaabbbccc', 'abcabcabc', 'babcCACBCaaB', 'aBcCbA', 'aBc',
        'aBcaCbbAcbCacAbcBa', 'aCBBCAbAAcCAcbCBBa', 'bACcACbbACBa',
        'CBACcbcabcAaABb'
    )
    for case in test_cases:
        print(balanced_strings(case))

    print('\n# transform_strings example 1')
    test_cases = ('eMKCPVkRI%~}+$GW9EOQNMI!_%{#ED}#=-~WJbFNWSQqDO-..@}',
                  'dGAqJLcNC0YFJQEB5JJKETQ0QOODKF8EYX7BGdzAACmrSL0PVKC',
                  'aLiAnVhSV9}_+QOD3YSIYPR4MCKYUF9QUV9TVvNdFuGqVU4$/%D',
                  'zmRJWfoKC5RDKVYO3PWMATC7BEIIVX9LJR7FKtDXxXLpFG7PESX',
                  'hFKGVErCS$**!<OS<_/.>NR*)<<+IR!,=%?OAiPQJILzMI_#[+}',
                  'EOQUQJLBQLDLAVQSWERAGGAOKUUKOPUWLQSKJNECCPRRXGAUABN',
                  'WGBKTQSGVHHHHHTZZZZZMQKBLC66666NNR11111OKUN2KTGYUIB',
                  'YFOWAOYLWGQHJQXZAUPZPNUCEJABRR6MYR1JASNOTF22MAAGTVA',
                  'GNLXFPEPMYGHQQGZGEPZXGJVEYE666UKNE11111WGNW2NVLCIOK',
                  'VTABNCKEFTJHXATZTYGZVLXLAB6JVGRATY1GEY1PGCO2QFPRUAP',
                  'UTCKYKGJBWMHPYGZZZZZWOKQTM66666GLA11111CPF222RUPCJT')
    for case in test_cases:
        print(transform_string(case, '612HZ', '261TO'))
