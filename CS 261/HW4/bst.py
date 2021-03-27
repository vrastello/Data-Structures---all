# Course: CS261 - Data Structures
# Student Name: Vincent Rastello
# Assignment: 4
# Description: Binary Search Tree


class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self) -> object:
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self) -> object:
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self) -> object:
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value          # to store node's data
        self.left = None            # pointer to root of left subtree
        self.right = None           # pointer to root of right subtree

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self, start_tree=None) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using in-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "TREE pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # base case
        if not cur:
            return
        # store value of current node
        values.append(str(cur.value))
        # recursive case for left subtree
        self._str_helper(cur.left, values)
        # recursive case for right subtree
        self._str_helper(cur.right, values)

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        Adds new value to tree, maintains BST property. Duplicates placed in right tree.
        """
        # sets new node nad parent
        new_node = TreeNode(value)
        parent = None
        cur_node = self.root
        # while node is not none, goes left if less than parent, right if greater
        while cur_node is not None:
            parent = cur_node
            if new_node.value < cur_node.value:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        # sets to root if nothing in list
        if not parent:
            self.root = new_node

        # puts in left or right child if less or greater/equal
        else:
            if new_node.value < parent.value:
                parent.left = new_node
            else:
                parent.right = new_node

    def contains(self, value: object) -> bool:
        """
        Searches tree for node containing value, returns True if found, false if not.
        """
        cur_node = self.root
        while cur_node:
            if cur_node.value == value:
                return True
            elif value < cur_node.value:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right

        return False

    def get_first(self) -> object:
        """
        Returns value stored in root node, None if empty tree.
        """
        if not self.root:
            return None

        return self.root.value

    def remove_first(self) -> bool:
        """
        Removes the root node of the BST, replaces with it's successor. Returns false if empty tree.
        """
        root_node = self.root
        # checks if empty, or if no leafs or if only one child
        if not self.get_first():
            return False
        elif not root_node.left and not root_node.right:
            root_node = None
        elif not root_node.right and root_node.left:
            root_node = root_node.left
        elif not root_node.left and root_node.right:
            root_node = root_node.right
        # assigns successor and if successor is not right node re-arranges tree
        else:
            parent_s = root_node.right
            successor = parent_s
            if successor.left:
                successor = successor.left

            successor.left = root_node.left
            if successor != root_node.right:
                parent_s.left = successor.right
                successor.right = parent_s

            root_node = successor

        self.root = root_node
        return True

    def remove(self, value) -> bool:
        """
        Removes value and returns true when value removed
        """
        # sets all variables
        found_val = False
        cur_node = self.root
        direction = None
        p_node = None
        if not self.root:
            return False
        # checks for found value
        while cur_node and not found_val:
            if cur_node.value == value:
                found_val = True
                continue
            elif value < cur_node.value:
                if cur_node.left:
                    p_node = cur_node
                cur_node = cur_node.left
                direction = "left"
            else:
                if cur_node.right:
                    p_node = cur_node
                cur_node = cur_node.right
                direction = "right"
            # if value found gets successor unless only one or no child nodes
        if found_val:
            if cur_node == self.root:
                self.remove_first()
                return True
            if not cur_node.left and not cur_node.right:
                if direction == "right":
                    p_node.right = None
                else:
                    p_node.left = None
            elif not cur_node.right and cur_node.left:
                if direction == "right":
                    p_node.right = cur_node.left
                else:
                    p_node.left = cur_node.left
            elif not cur_node.left and cur_node.right:
                if direction == "right":
                    p_node.right = cur_node.right
                else:
                    p_node.left = cur_node.right

            # this section sets successor to node
            else:
                parent_s = cur_node
                if parent_s.right:
                    parent_s = parent_s.right
                successor = parent_s
                while successor.left:
                    parent_s = successor
                    successor = successor.left

                successor.left = cur_node.left
                if successor != cur_node.right:
                    parent_s.left = successor.right
                    successor.right = cur_node.right

                if direction == "right":
                    p_node.right = successor
                else:
                    p_node.left = successor

        return found_val

    def pre_order_traversal(self) -> Queue:
        """
        orders queue for pre-order bst traversal
        """
        node_queue = Queue()
        return self.rec_pre_order_traversal(self.root, node_queue)

    def rec_pre_order_traversal(self, start, node_queue):
        """
        recursive function for pre order
        """
        if start:
            node_queue.enqueue(start.value)
            self.rec_pre_order_traversal(start.left, node_queue)
            return self.rec_pre_order_traversal(start.right, node_queue)

        return node_queue

    def in_order_traversal(self) -> Queue:
        """
        orders queue for in order bst traversal
        """
        node_queue = Queue()
        return self.rec_in_order_traversal(self.root, node_queue)

    def rec_in_order_traversal(self, start, node_queue):
        """
        recursive function for in order
        """
        if start:
            self.rec_in_order_traversal(start.left, node_queue)
            node_queue.enqueue(start.value)
            return self.rec_in_order_traversal(start.right, node_queue)

        return node_queue

    def post_order_traversal(self) -> Queue:
        """
        orders queue for post order bst traversal
        """
        node_queue = Queue()
        return self.rec_post_order_traversal(self.root, node_queue)

    def rec_post_order_traversal(self, start, node_queue):
        """
        recursive function for post order
        """
        if start:
            self.rec_post_order_traversal(start.left, node_queue)
            self.rec_post_order_traversal(start.right, node_queue)
            node_queue.enqueue(start.value)

        return node_queue

    def by_level_traversal(self) -> Queue:
        """
        adds nodes to queue by by level traversal
        """
        final_queue = Queue()
        node_queue = Queue()
        node_queue.enqueue(self.root)
        while not node_queue.is_empty():
            node = node_queue.dequeue()
            if node:
                final_queue.enqueue(node.value)
                node_queue.enqueue(node.left)
                node_queue.enqueue(node.right)

        return final_queue

    def is_full(self) -> bool:
        """
        returns true if tree is full
        """
        node = self.root
        return self.rec_is_full(node)

    def rec_is_full(self, node):
        """
        recursive cal for is_full function
        """
        # if no node base case
        if not node:
            return True

        # if no child nodes
        if not node.left and not node.right:
            return True

        # if complete sub tree, returns and logic for left and right, if both true returns true
        if node.left and node.right:
            return self.rec_is_full(node.left) and self.rec_is_full(node.right)

        return False

    def is_complete(self) -> bool:
        """
        checks if bst is complete tree
        """
        # of no root then tree is complete
        if not self.root:
            return True
        # initializes queue
        queue = Queue()
        incomplete = False

        # adds root to queue
        queue.enqueue(self.root)

        # while queue is not empty deques current node
        while not queue.is_empty():
            cur_node = queue.dequeue()

            # checks left node
            if cur_node.left:
                # if incomplete is true returns false
                if incomplete:
                    return False

                #adds left to queue
                queue.enqueue(cur_node.left)

            # if no left node at that height sets incomplete to true
            else:
                incomplete = True

            # if no right node sets incomplete to true, if left node found after right node
            # tree is incomplete and returns false after looping back up
            if cur_node.right:
                if incomplete:
                    return False
                queue.enqueue(cur_node.right)

            else:
                incomplete = True

        # if it makes it through loop returns true
        return True

    def is_perfect(self) -> bool:
        """
        uses leaf ratio to define a perfect bst
        """
        if not self.root:
            return True
        if not self.root.right and not self.root.left:
            return True

        height = self.height()
        leaves = self.count_leaves()

        if leaves == 2**height:
            return True

        return False


    def size(self) -> int:
        """
        returns size of tree
        """
        return self.rec_size(self.root)

    def rec_size(self, start):
        """
        recursive function to determine size of tree
        """
            # if no node, return value 0
        if not start:
            return 0
        # otherwise adds 1 for current node then calls both right and left nodes
        else:
            return self.rec_size(start.left) + 1 + self.rec_size(start.right)

    def height(self) -> int:
        """
        returns height of bst
        """
        return self.rec_height(self.root)

    def rec_height(self, node):
        """
        recursive height function call
        """
        # if no root node returns -1
        if not node:
            return -1
        # goes down left and right subtree
        else:
            left_height = self.rec_height(node.left)
            right_height = self.rec_height(node.right)

            # whichever is great it adds 1 and goes down that particular tree
            if left_height > right_height:
                return left_height + 1
            else:
                # if equal or right is great goes down right
                return right_height + 1

    def count_leaves(self) -> int:
        """
        recursive call to count leaves of bst
        """
        return self.rec_count_leaves(self.root)

    def rec_count_leaves(self, node):
        """
        recursive helper function to count leaves of bst
        """
        # if no root node return 0
        if not node:
            return 0
        # if no children of root node return 1
        if not node.left and not node.right:
            return 1
        # otherwise adds recursively each branch
        else:
            return self.rec_count_leaves(node.left) + self.rec_count_leaves(node.right)

    def count_unique(self) -> int:
        """
        final function for count unique, takes stack and counts values if unique
        """
        node_stack = self.helper_count_unique()
        count = 0
        while not node_stack.is_empty():
            popVal = node_stack.pop()
            if node_stack.is_empty():
                count += 1
                continue
            if popVal != node_stack.top():
                count += 1

        return count

    def helper_count_unique(self):
        """
        helper recursive caller that initiates stack
        """
        node_stack = Stack()
        return self.rec_count_unique(self.root, node_stack)

    def rec_count_unique(self, node, node_stack):
        """in order traversal adding values to stack"""
        if node:
            self.rec_count_unique(node.left, node_stack)
            node_stack.push(node.value)
            return self.rec_count_unique(node.right, node_stack)

        return node_stack




# BASIC TESTING - PDF EXAMPLES

if __name__ == '__main__':
    """ add() example #1 """
    print("\nPDF - method add() example 1")
    print("----------------------------")
    tree = BST()
    print(tree)
    tree.add(10)
    tree.add(15)
    tree.add(5)
    print(tree)
    tree.add(15)
    tree.add(15)
    print(tree)
    tree.add(5)
    print(tree)

    """ add() example 2 """
    print("\nPDF - method add() example 2")
    print("----------------------------")
    tree = BST()
    tree.add(10)
    tree.add(10)
    print(tree)
    tree.add(-1)
    print(tree)
    tree.add(5)
    print(tree)
    tree.add(-1)
    print(tree)

    """ contains() example 1 """
    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))
    tree2 = BST([])
    print(tree2.contains(20))

    """ contains() example 2 """
    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    """ get_first() example 1 """
    print("\nPDF - method get_first() example 1")
    print("----------------------------------")
    tree = BST()
    print(tree.get_first())
    tree.add(10)
    tree.add(15)
    tree.add(5)
    print(tree.get_first())
    print(tree)

    """ remove() example 1 """
    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    tree = BST([10, 5, 15])
    print(tree.remove(7))
    print(tree.remove(15))
    print(tree.remove(15))

    """ remove() example 2 """
    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.remove(20))
    print(tree)

    """ remove() example 3 """
    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    tree = BST([10, 5, 20, 18, 12, 7, 27, 22, 18, 24, 22, 30])
    print(tree.remove(20))
    print(tree)
    # comment out the following lines
    # if you have not yet implemented traversal methods
    # print(tree.pre_order_traversal())
    # print(tree.in_order_traversal())
    # print(tree.post_order_traversal())
    # print(tree.by_level_traversal())

    """ remove_first() example 1 """
    print("\nPDF - method remove_first() example 1")
    print("-------------------------------------")
    tree = BST([10, 15, 5])
    print(tree.remove_first())
    print(tree)

    """ remove_first() example 2 """
    print("\nPDF - method remove_first() example 2")
    print("-------------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7])
    print(tree.remove_first())
    print(tree)

    """ remove_first() example 3 """
    print("\nPDF - method remove_first() example 3")
    print("-------------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)

    """ Traversal methods example 1 """
    print("\nPDF - traversal methods example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Traversal methods example 2 """
    print("\nPDF - traversal methods example 2")
    print("---------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 1 """
    print("\nComprehensive example 1")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'  N/A {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print()
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 2 """
    print("\nComprehensive example 2")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'N/A   {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in 'DATA STRUCTURES':
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print('', tree.pre_order_traversal(), tree.in_order_traversal(),
          tree.post_order_traversal(), tree.by_level_traversal(),
          sep='\n')

