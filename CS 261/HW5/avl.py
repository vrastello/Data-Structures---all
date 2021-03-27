# Course: CS261 - Data Structures
# Author: Vincent Rastello
# Assignment: 5
# Description: AVL

import random

from bst import BST
from bst import TreeNode
from bst import Stack
from bst import Queue


class AVLTreeNode(TreeNode):
    """
    AVL Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        super().__init__(value)
        self.parent = None
        self.height = 0


class AVL(BST):

    def get_height(self, root):
        """returns root height, if empty node returns -1"""
        if not root:
            return -1
        else:
            return root.height

    def getMinValueNode(self, root):
        """continues down left side until left is none, then returns root: min value"""
        if root is None or root.left is None:
            return root

        return self.getMinValueNode(root.left)

    def updateHeight(self, node):
        """updates height by finding max of left and right heights and adding one """
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

    def balanceFactor(self, node):
        """returns balance factor by subtracting left height from right"""
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, root):
        """moves pivot node to be parent of root node, pivot node is left node"""
        pivot = root.left  # set up pointers
        tmp = pivot.right
        # re-assign pivot's right child to root and update parent pointers
        pivot.right = root
        pivot.parent = root.parent
        root.parent = pivot
        # assign right child of pivot to root's left and update it's parent
        root.left = tmp
        if tmp:   # check for null
            tmp.parent = root

        # update pivots parent, check which subtree root was in
        if pivot.parent:
            if pivot.parent.left == root:
                pivot.parent.left = pivot
            else:
                pivot.parent.right = pivot

        # update heights
        self.updateHeight(root)
        self.updateHeight(pivot)
        return pivot

    def rotate_left(self, root):
        """moves pivot node to be parent of root node, pivot node is right node"""
        pivot = root.right  # set up pointers
        tmp = pivot.left
        # re-assign pivot's right child to root and update parent pointers
        pivot.left = root
        pivot.parent = root.parent
        root.parent = pivot
        # assign right child of pivot to root's right and update it's parent
        root.right = tmp
        if tmp:   # check for null
            tmp.parent = root

        # update pivots parent, check which subtree root was in
        if pivot.parent:
            if pivot.parent.left == root:
                pivot.parent.left = pivot
            else:
                pivot.parent.right = pivot

        # update heights
        self.updateHeight(root)
        self.updateHeight(pivot)
        return pivot

    def rebalance(self, root):
        """Re-balances doing single or double rotations if needed"""
        if self.balanceFactor(root) > 1:   # L-R
            if self.balanceFactor(root.left) < 0:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
            else:  # L-L
                return self.rotate_right(root)

        elif self.balanceFactor(root) < -1:  # R-L
            if self.balanceFactor(root.right) > 0:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)
            else:  # R-R
                return self.rotate_left(root)

        else:
            return root   # doesn't need rebalance

    def _add_helper(self, root, value):
        """add helper for add, recursively adds and updates heights and rebalances"""

        if not root:  # If empty, adds value with new node
            return AVLTreeNode(value)
        # goes down left sub tree, updating parents
        if value < root.value:
            left_sub_root = self._add_helper(root.left, value)
            root.left = left_sub_root
            left_sub_root.parent = root
            # goes down right sub tree updating parents
        elif value > root.value:
            right_sub_root = self._add_helper(root.right, value)
            root.right = right_sub_root
            right_sub_root.parent = root
        else:
            return root

        # recursively updates heights of all nodes and rebalances
        self.updateHeight(root)
        return self.rebalance(root)

    def _remove_helper(self, root, value):
        """recursively removes value updates heights and rebalances as necessary"""
        # base case, if empty return root
        if not root:
            return root

        # goes down left tree recursively
        elif value < root.value:
            left_sub_root = self._remove_helper(root.left, value)
            root.left = left_sub_root

        # goes down right tree recursively
        elif value > root.value:
            right_sub_root = self._remove_helper(root.right, value)
            root.right = right_sub_root

        # if value is found
        # if no left or right child found, returns other child
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # finds successor with get min value
            # replaces root value with successor value
            temp = self.getMinValueNode(root.right)
            root.value = temp.value
            root.right = self._remove_helper(root.right, temp.value)

        if root is None:
            return root

        self.updateHeight(root)
        return self.rebalance(root)

    def add(self, value):
        """
        adds new value to AVL using helper function
        """
        self.root = self._add_helper(self.root, value)

    def remove(self, value) -> bool:
        """
        if value is not found returns False, else removes using helper function and returns true.
        """
        if not self.contains(value):
            return False
        self.root = self._remove_helper(self.root, value)
        return True

if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),          #RR
        (3, 2, 1),          #LL
        (1, 3, 2),          #RL
        (3, 1, 2),          #LR
    )
    for case in test_cases:
        avl = AVL(case)
        print(avl)


    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),   # RR, RR
        (10, 30, 30, 50, 40),   # RR, RL
        (30, 20, 10, 5, 1),     # LL, LL
        (30, 20, 10, 1, 5),     # LL, LR
        (5, 4, 6, 3, 7, 2, 8),  # LL, RR
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        avl = AVL(case)
        print('INPUT  :', case)
        print('RESULT :', avl)


    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),                             # no AVL rotation
        ((1, 2, 3), 2),                             # no AVL rotation
        ((1, 2, 3), 3),                             # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),     # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),     # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),     # no AVL rotation
    )
    for tree, del_value in test_cases:
        avl = AVL(tree)
        print('INPUT  :', avl, "DEL:", del_value)
        avl.remove(del_value)
        print('RESULT :', avl)


    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),     # RR
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),     # LL
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),     # RL
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),     # LR
    )
    for tree, del_value in test_cases:
        avl = AVL(tree)
        print('INPUT  :', avl, "DEL:", del_value)
        avl.remove(del_value)
        print('RESULT :', avl)


    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    avl = AVL(case)
    for del_value in case:
        print('INPUT  :', avl, del_value)
        avl.remove(del_value)
        print('RESULT :', avl)


    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    avl = AVL(case)
    for _ in case[:-2]:
        print('INPUT  :', avl.size(), avl, avl.root)
        avl.remove(avl.root.value)
        print('RESULT :', avl)


    print("\nPDF - method remove() example 5")
    print("-------------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        avl = AVL(case)
        if avl.size() != len(case):
            raise Exception("PROBLEM WITH ADD OPERATION")
        for value in case[::2]:
            avl.remove(value)
        if avl.size() != len(case) - len(case[::2]):
            raise Exception("PROBLEM WITH REMOVE OPERATION")
    print('Stress test finished')


    """ Comprehensive example 1 """
    print("\nComprehensive example 1")
    print("-----------------------")
    tree = AVL()
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
    tree = AVL()
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
