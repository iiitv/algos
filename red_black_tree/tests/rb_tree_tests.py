import unittest
import random
from datetime import datetime

from ..rb_tree import RedBlackTree, Node, BLACK, RED
NIL_LEAF = RedBlackTree.NIL_LEAF


class RbTreeTests(unittest.TestCase):

    def test_find_node(self):
        """ Use the tree we get from the test_build function
            and test the find function on each node"""
        rb_tree = RedBlackTree()
        rb_tree.add(2)
        node_2 = rb_tree.root
        rb_tree.add(1)
        node_1 = rb_tree.root.left
        rb_tree.add(4)
        node_4 = rb_tree.root.right
        rb_tree.add(5)
        node_5 = node_4.right
        rb_tree.add(9)
        node_9 = node_5.right
        rb_tree.add(3)
        node_3 = node_4.left
        rb_tree.add(6)
        node_6 = node_9.left
        rb_tree.add(7)
        node_7 = node_5.right
        rb_tree.add(15)
        node_15 = node_9.right
        """
                            ___5B___
                        __2R__      7R
                      1B     4B    6B 9B
                            3R         15R
        """
        # valid cases
        self.assertEqual(rb_tree.find_node(5), node_5)
        self.assertEqual(rb_tree.find_node(2), node_2)
        self.assertEqual(rb_tree.find_node(1), node_1)
        self.assertEqual(rb_tree.find_node(4), node_4)
        self.assertEqual(rb_tree.find_node(3), node_3)
        self.assertEqual(rb_tree.find_node(7), node_7)
        self.assertEqual(rb_tree.find_node(6), node_6)
        self.assertEqual(rb_tree.find_node(9), node_9)
        self.assertEqual(rb_tree.find_node(15), node_15)
        # invalid cases
        self.assertIsNone(rb_tree.find_node(-1))
        self.assertIsNone(rb_tree.find_node(52454225))
        self.assertIsNone(rb_tree.find_node(0))
        self.assertIsNone(rb_tree.find_node(401))
        self.assertIsNone(rb_tree.find_node(3.00001))

    # ***************TEST INSERTIONS***************

    def test_recoloring_only(self):
        """
        Create a red-black tree, add a red node such that we only have to recolor
        upwards twice
        add 4, which recolors 2 and 8 to BLACK,
                6 to RED
                    -10, 20 to BLACK
        :return:
        """
        tree = RedBlackTree()
        root = Node(value=10, color=BLACK, parent=None)
        # LEFT SUBTREE
        node_m10 = Node(value=-10, color=RED, parent=root)  # OK
        node_6 = Node(value=6, color=BLACK, parent=node_m10)  # OK
        node_8 = Node(value=8, color=RED, parent=node_6,
                      left=NIL_LEAF, right=NIL_LEAF)  # OK
        node_2 = Node(value=2, color=RED, parent=node_6,
                      left=NIL_LEAF, right=NIL_LEAF)  # OK
        node_6.left = node_2  # OK
        node_6.right = node_8  # OK
        node_m20 = Node(value=-20, color=BLACK, parent=node_m10,
                        left=NIL_LEAF, right=NIL_LEAF)  # OK
        node_m10.left = node_m20  # OK
        node_m10.right = node_6  # OK

        # RIGHT SUBTREE
        node_20 = Node(value=20, color=RED, parent=root)  # OK
        node_15 = Node(value=15, color=BLACK, parent=node_20,
                       left=NIL_LEAF, right=NIL_LEAF)  # OK
        node_25 = Node(25, color=BLACK, parent=node_20,
                       left=NIL_LEAF, right=NIL_LEAF)  # OK
        node_20.left = node_15  # OK
        node_20.right = node_25  # OK

        root.left = node_m10  # OK
        root.right = node_20  # OK

        tree.root = root
        tree.add(4)
        """
                    _____10B_____                                     _____10B_____
               __-10R__        __20R__                           __-10R__        __20R__
            -20B      6B     15B     25B  --FIRST RECOLOR-->  -20B      6R     15B     25B
                    2R  8R                                            2B  8B
               Add-->4R                                                4R



                                  _____10B_____
                             __-10B__        __20B__
   --SECOND RECOLOR-->    -20B      6R     15B     25B
                                  2B  8B
                                   4R
        """
        """ This should trigger two recolors.
            2 and 8 should turn to black,
            6 should turn to red,
            -10 and 20 should turn to black
            10 should try to turn to red, but since it's the root it can't be black"""
        expected_values = [-20, -10, 2, 4, 6, 8, 10, 15, 20, 25]
        values = list(tree)
        self.assertEqual(values, expected_values)

        self.assertEqual(node_2.color, BLACK)
        self.assertEqual(node_8.color, BLACK)
        self.assertEqual(node_6.color, RED)
        self.assertEqual(node_m10.color, BLACK)
        self.assertEqual(node_20.color, BLACK)

    def test_recoloring_two(self):
        rb_tree = RedBlackTree()
        root = Node(value=10, color=BLACK, parent=None,
                    left=NIL_LEAF, right=NIL_LEAF)
        # left subtree
        node_m10 = Node(value=-10, color=RED, parent=root,
                        left=NIL_LEAF, right=NIL_LEAF)
        node_m20 = Node(value=-20, color=BLACK, parent=node_m10,
                        left=NIL_LEAF, right=NIL_LEAF)
        node_6 = Node(value=6, color=BLACK, parent=node_m10,
                      left=NIL_LEAF, right=NIL_LEAF)
        node_m10.left = node_m20
        node_m10.right = node_6

        # right subtree
        node_20 = Node(value=20, color=RED, parent=root,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_15 = Node(value=15, color=BLACK, parent=node_20,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_25 = Node(value=25, color=BLACK, parent=node_20,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_20.left = node_15
        node_20.right = node_25
        node_12 = Node(value=12, color=RED, parent=node_15,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_17 = Node(value=17, color=RED, parent=node_15,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_15.left = node_12
        node_15.right = node_17

        root.left = node_m10
        root.right = node_20
        rb_tree.root = root
        rb_tree.add(19)

        """

                 _____10B_____                                        _____10B_____
            __-10R__        __20R__                              __-10R__        __20R__
         -20B      6B     15B     25B     FIRST RECOLOR-->    -20B      6B     15R     25B
                       12R  17R                                             12B  17B
                        Add-->19R                                                 19R


        SECOND RECOLOR


                _____10B_____
           __-10B__        __20B__
        -20B      6B     15R     25B
                      12B  17B
                            19R
        """
        expected_values = [-20, -10, 6, 10, 12, 15, 17, 19, 20, 25]
        values = list(rb_tree)
        self.assertEqual(values, expected_values)

        node_19 = node_17.right
        self.assertEqual(node_19.value, 19)
        self.assertEqual(node_19.color, RED)
        self.assertEqual(node_19.parent, node_17)

        self.assertEqual(node_17.color, BLACK)
        self.assertEqual(node_12.color, BLACK)
        self.assertEqual(node_15.color, RED)
        self.assertEqual(node_20.color, BLACK)
        self.assertEqual(node_25.color, BLACK)
        self.assertEqual(node_m10.color, BLACK)
        self.assertEqual(rb_tree.root.color, BLACK)

    def test_right_rotation(self):
        tree = RedBlackTree()
        root = Node(value=10, color=BLACK, parent=None)

        # LEFT SUBTREE
        node_m10 = Node(value=-10, color=BLACK, parent=root,
                        left=NIL_LEAF, right=NIL_LEAF)
        node_7 = Node(value=7, color=RED, parent=node_m10,
                      left=NIL_LEAF, right=NIL_LEAF)
        node_m10.right = node_7

        # RIGHT SUBTREE
        node_20 = Node(value=20, color=BLACK, parent=root,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_15 = Node(value=15, color=RED, parent=node_20,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_20.left = node_15

        root.left = node_m10
        root.right = node_20

        tree.root = root
        tree.add(13)

        """
                  ____10B____                                           ____10B____
              -10B          20B       --(LL -> R) RIGHT ROTATE-->    -10B         15B
                 7R       15R                                           7R      13R 20R
                 Add -> 13R
        """
        expected_values = [-10, 7, 10, 13, 15, 20]
        values = list(tree)
        self.assertEqual(values, expected_values)

        node_20 = node_15.right
        node_13 = node_15.left

        # this should be the parent of both now
        self.assertEqual(node_15.color, BLACK)
        self.assertEqual(node_15.parent.value, 10)

        self.assertEqual(node_20.value, 20)
        self.assertEqual(node_20.color, RED)
        self.assertEqual(node_20.parent.value, 15)
        self.assertEqual(node_20.left, NIL_LEAF)
        self.assertEqual(node_20.right, NIL_LEAF)

        self.assertEqual(node_13.value, 13)
        self.assertEqual(node_13.color, RED)
        self.assertEqual(node_13.parent.value, 15)
        self.assertEqual(node_13.left, NIL_LEAF)
        self.assertEqual(node_13.right, NIL_LEAF)

    def test_left_rotation_no_sibling(self):
        rb_tree = RedBlackTree()
        root = Node(value=10, color=BLACK, parent=None,
                    left=NIL_LEAF, right=NIL_LEAF)
        # LEFT SUBTREE
        node_7 = Node(value=7, color=BLACK, parent=root,
                      left=NIL_LEAF, right=NIL_LEAF)
        node_8 = Node(value=8, color=RED, parent=node_7,
                      left=NIL_LEAF, right=NIL_LEAF)
        node_7.right = node_8

        # RIGHT SUBTREE
        rightest = Node(value=20, color=BLACK, parent=root,
                        left=NIL_LEAF, right=NIL_LEAF)
        root.left = node_7
        root.right = rightest

        rb_tree.root = root
        rb_tree.add(9)
        """
                 -->     10B                                10B
        ORIGINAL -->  7B    20B  --LEFT ROTATION-->       8B   20B
                 -->    8R                              7R  9R
                 -->     9R
        We add 9, which is the right child of 8 and causes a red-red relationship
        this calls for a left rotation, so 7 becomes left child of 8 and 9 the right child of 8
        8 is black, 7 and 9 are red
        """
        expected_values = [7, 8, 9, 10, 20]
        values = list(rb_tree)
        self.assertEqual(values, expected_values)

        node_9 = node_8.right

        self.assertEqual(node_9.value, 9)
        self.assertEqual(node_9.color, RED)
        self.assertEqual(node_9.parent.value, 8)
        self.assertEqual(node_9.left, NIL_LEAF)
        self.assertEqual(node_9.right, NIL_LEAF)

        self.assertEqual(node_8.parent.value, 10)
        self.assertEqual(node_8.color, BLACK)
        self.assertEqual(node_8.left.value, 7)
        self.assertEqual(node_8.right.value, 9)

        self.assertEqual(node_7.color, RED)
        self.assertEqual(node_7.parent.value, 8)
        self.assertEqual(node_7.left, NIL_LEAF)
        self.assertEqual(node_7.right, NIL_LEAF)

    def test_right_rotation_no_sibling_left_subtree(self):
        rb_tree = RedBlackTree()
        root = Node(value=10, color=BLACK, parent=None,
                    left=NIL_LEAF, right=NIL_LEAF)
        # LEFT SUBTREE
        node_m10 = Node(value=-10, color=BLACK, parent=root,
                        left=NIL_LEAF, right=NIL_LEAF)
        node_m11 = Node(value=-11, color=RED, parent=node_m10,
                        left=NIL_LEAF, right=NIL_LEAF)
        node_m10.left = node_m11
        # RIGHT SUBTREE
        node_20 = Node(value=20, color=BLACK, parent=root,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_15 = Node(value=15, color=RED, parent=node_20,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_20.left = node_15

        root.left = node_m10
        root.right = node_20
        rb_tree.root = root
        rb_tree.add(-12)
        """


                            ____10____                                       ____10____
                       __-10B__     20B  (LL->R) Right rotate-->          -11B        20B
                   -11R          15R                                   -12R  -10R   15R
          Add--> 12R



        red-red relationship with -11 -12, so we do a right rotation where -12 becomes the left child of -11,
                                                                            -10 becomes the right child of -11
        -11's parent is root, -11 is black, -10,-12 are RED
        """
        expected_values = [-12, -11, -10, 10, 15, 20]
        values = list(rb_tree)
        self.assertEqual(values, expected_values)

        node_m12 = node_m11.left
        self.assertEqual(rb_tree.root.left.value, -11)

        self.assertEqual(node_m12.value, -12)
        self.assertEqual(node_m12.color, RED)
        self.assertEqual(node_m12.parent.value, -11)
        self.assertEqual(node_m12.left, NIL_LEAF)
        self.assertEqual(node_m12.right, NIL_LEAF)

        self.assertEqual(node_m11.color, BLACK)
        self.assertEqual(node_m11.parent, rb_tree.root)
        self.assertEqual(node_m11.left.value, -12)
        self.assertEqual(node_m11.right.value, -10)

        self.assertEqual(node_m10.color, RED)
        self.assertEqual(node_m10.parent.value, -11)
        self.assertEqual(node_m10.left, NIL_LEAF)
        self.assertEqual(node_m10.right, NIL_LEAF)

    def test_left_right_rotation_no_sibling(self):
        rb_tree = RedBlackTree()
        root = Node(value=10, color=BLACK, parent=None,
                    left=NIL_LEAF, right=NIL_LEAF)
        # LEFT PART
        node_m10 = Node(value=-10, color=BLACK, parent=root,
                        left=NIL_LEAF, right=NIL_LEAF)
        node_7 = Node(value=7, color=RED, parent=node_m10,
                      left=NIL_LEAF, right=NIL_LEAF)
        node_m10.right = node_7

        # RIGHT PART
        node_20 = Node(value=20, color=BLACK, parent=root,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_15 = Node(value=15, color=RED, parent=node_20,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_20.left = node_15

        root.left = node_m10
        root.right = node_20

        rb_tree.root = root
        rb_tree.add(17)
        """
                    ___10___                                                     ____10____
                 -10B      20B                                                -10B        20B
                    7R   15R        --(LR=>RL) Left Rotate (no recolor) -->      7R     17R
                    Add--> 17R                                                         15R



                                                ____10____
        Right Rotate (with recolor) -->      -10B        17B
                                                7R     15R 20R

        15-17 should do a left rotation so 17 is now the parent of 15.
        Then, a right rotation should be done so 17 is the parent of 20(15's prev parent)
        Also, a recoloring should be done such that 17 is now black and his children are red
        """
        expected_values = [-10, 7, 10, 15, 17, 20]
        values = list(rb_tree)
        self.assertEqual(values, expected_values)

        node_15 = node_15
        node_20 = node_20
        node_17 = node_15.parent
        self.assertEqual(rb_tree.root.right, node_17)

        self.assertEqual(node_17.value, 17)
        self.assertEqual(node_17.color, BLACK)
        self.assertEqual(node_17.parent, rb_tree.root)
        self.assertEqual(node_17.left.value, 15)
        self.assertEqual(node_17.right.value, 20)

        self.assertEqual(node_20.parent.value, 17)
        self.assertEqual(node_20.color, RED)
        self.assertEqual(node_20.left, NIL_LEAF)
        self.assertEqual(node_20.right, NIL_LEAF)

        self.assertEqual(node_15.parent.value, 17)
        self.assertEqual(node_15.color, RED)
        self.assertEqual(node_15.left, NIL_LEAF)
        self.assertEqual(node_15.right, NIL_LEAF)

    def test_right_left_rotation_no_sibling(self):
        rb_tree = RedBlackTree()
        root = Node(value=10, color=BLACK, parent=None,
                    left=NIL_LEAF, right=NIL_LEAF)
        # LEFT PART
        nodem10 = Node(value=-10, color=BLACK, parent=root,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_7 = Node(value=7, color=RED, parent=nodem10,
                      left=NIL_LEAF, right=NIL_LEAF)
        nodem10.right = node_7

        # RIGHT PART
        node_20 = Node(value=20, color=BLACK, parent=root,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_15 = Node(value=15, color=RED, parent=node_20,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_20.left = node_15

        root.left = nodem10
        root.right = node_20

        rb_tree.root = root
        rb_tree.add(2)
        """

            ___10___                                                        ___10___
         -10B       20B                                                  -10B       20B
            7R     15R   --- (LR=>RL) Right Rotation (no recolor)-->        2R    15R
    Add--> 2R                                                                7R


                                                 _____10_____
        Left Rotation (with recolor) -->     __2B__       __20B__
                                         -10R     7R    15R


        2 goes as left to 7, but both are red so we do a RIGHT-LEFT rotation
        First a right rotation should happen, so that 2 becomes the parent of 7 [2 right-> 7]
        Second a left rotation should happen, so that 2 becomes the parent of -10 and 7
        2 is black, -10 and 7 are now red. 2's parent is the root - 10
        """
        expected_values = [-10, 2, 7, 10, 15, 20]
        values = list(rb_tree)
        self.assertEqual(values, expected_values)

        node_2 = node_7.parent
        self.assertEqual(node_2.parent.value, 10)
        self.assertEqual(node_2.color, BLACK)
        self.assertEqual(node_2.left.value, -10)
        self.assertEqual(node_2.right.value, 7)

        self.assertEqual(node_7.color, RED)
        self.assertEqual(node_7.parent.value, 2)
        self.assertEqual(node_7.left, NIL_LEAF)
        self.assertEqual(node_7.right, NIL_LEAF)

        self.assertEqual(nodem10.color, RED)
        self.assertEqual(nodem10.parent.value, 2)
        self.assertEqual(nodem10.left, NIL_LEAF)
        self.assertEqual(nodem10.right, NIL_LEAF)

    def test_recolor_lr(self):
        rb_tree = RedBlackTree()
        root = Node(value=10, color=BLACK, parent=None)
        # RIGHT SUBTREE
        node_m10 = Node(value=-10, color=RED, parent=root,
                        left=NIL_LEAF, right=NIL_LEAF)
        node_m20 = Node(value=-20, color=BLACK, parent=node_m10,
                        left=NIL_LEAF, right=NIL_LEAF)
        node_m10.left = node_m20
        node_6 = Node(value=6, color=BLACK, parent=node_m10,
                      left=NIL_LEAF, right=NIL_LEAF)
        node_m10.right = node_6
        node_1 = Node(value=1, color=RED, parent=node_6,
                      left=NIL_LEAF, right=NIL_LEAF)
        node_6.left = node_1
        node_9 = Node(value=9, color=RED, parent=node_6,
                      left=NIL_LEAF, right=NIL_LEAF)
        node_6.right = node_9

        # LEFT SUBTREE
        node_20 = Node(value=20, color=BLACK, parent=root,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_15 = Node(value=15, color=RED, parent=node_20,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_20.left = node_15
        node_30 = Node(value=30, color=RED, parent=node_20,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_20.right = node_30

        root.left = node_m10
        root.right = node_20
        rb_tree.root = root
        rb_tree.add(4)
        """

                _________10B_________                                      _________10B_________
           ___-10R___              __20B__                            ___-10R___              __20B__
        -20B      __6B__         15R     30R  ---RECOLORS TO -->   -20B      __6R__         15R     30R
                1R     9R                                                  1B     9B
                  4R                                                         4R

                                      _________10B_________
                                 ___6R___              __20B__                                   ______6B__
        LEFT ROTATOES TO --> __-10B__    9B         15R      30R   ---RIGHT ROTATES TO-->   __-10R__       _10R_
                          -20B      1B                                                   -20B      1B    9B   __20B__
                                      4R                                                             4R     15R     30R



        Adding 4, we recolor once, then we check upwards and see that there's a black sibling.
        We see that our direction is RightLeft (RL) and do a Left Rotation followed by a Right Rotation
        -10 becomes 6's left child and 1 becomes -10's right child
        """
        expected_values = [-20, -10, 1, 4, 6, 9, 10, 15, 20, 30]
        values = list(rb_tree)
        self.assertEqual(values, expected_values)

        node_10 = rb_tree.root.right
        node_4 = node_1.right

        self.assertEqual(rb_tree.root.value, 6)
        self.assertEqual(rb_tree.root.parent, None)
        self.assertEqual(rb_tree.root.left.value, -10)
        self.assertEqual(rb_tree.root.right.value, 10)

        self.assertEqual(node_m10.parent.value, 6)
        self.assertEqual(node_m10.color, RED)
        self.assertEqual(node_m10.left.value, -20)
        self.assertEqual(node_m10.right.value, 1)

        self.assertEqual(node_10.color, RED)
        self.assertEqual(node_10.parent.value, 6)
        self.assertEqual(node_10.left.value, 9)
        self.assertEqual(node_10.right.value, 20)

        self.assertEqual(node_m20.color, BLACK)
        self.assertEqual(node_m20.parent.value, -10)
        self.assertEqual(node_m20.left, NIL_LEAF)
        self.assertEqual(node_m20.right, NIL_LEAF)

        self.assertEqual(node_1.color, BLACK)
        self.assertEqual(node_1.parent.value, -10)
        self.assertEqual(node_1.left, NIL_LEAF)
        self.assertEqual(node_1.right.color, RED)
        self.assertEqual(node_4.value, 4)
        self.assertEqual(node_4.color, RED)

    def test_functional_test_build_tree(self):
        rb_tree = RedBlackTree()
        rb_tree.add(2)
        self.assertEqual(rb_tree.root.value, 2)
        self.assertEqual(rb_tree.root.color, BLACK)
        node_2 = rb_tree.root
        """ 2 """
        expected_values = [2]
        values = list(rb_tree)
        self.assertEqual(values, expected_values)

        rb_tree.add(1)
        """
            2B
           1R
        """
        expected_values = [1, 2]
        values = list(rb_tree)
        self.assertEqual(values, expected_values)

        node_1 = rb_tree.root.left
        self.assertEqual(node_1.value, 1)
        self.assertEqual(node_1.color, RED)

        rb_tree.add(4)
        """
            2B
          1R  4R
        """
        expected_values = [1, 2, 4]
        values = list(rb_tree)
        self.assertEqual(values, expected_values)

        node_4 = rb_tree.root.right
        self.assertEqual(node_4.value, 4)
        self.assertEqual(node_4.color, RED)
        self.assertEqual(node_4.left, NIL_LEAF)
        self.assertEqual(node_4.right, NIL_LEAF)

        rb_tree.add(5)
        """
            2B                              2B
          1R  4R    ---CAUSES RECOLOR-->  1B  4B
               5R                              5R
        """
        expected_values = [1, 2, 4, 5]
        values = list(rb_tree)
        self.assertEqual(values, expected_values)

        node_5 = node_4.right
        self.assertEqual(node_5.value, 5)
        self.assertEqual(node_4.color, BLACK)
        self.assertEqual(node_1.color, BLACK)
        self.assertEqual(node_5.color, RED)

        rb_tree.add(9)
        """
            2B                                           __2B__
          1B  4B        ---CAUSES LEFT ROTATION-->     1B     5B
                5R                                          4R  9R
                 9R
        """
        expected_values = [1, 2, 4, 5, 9]
        values = list(rb_tree)
        self.assertEqual(values, expected_values)

        node_9 = node_5.right
        self.assertEqual(node_9.value, 9)
        self.assertEqual(node_9.color, RED)
        self.assertEqual(node_9.left, NIL_LEAF)
        self.assertEqual(node_9.right, NIL_LEAF)

        self.assertEqual(node_4.color, RED)
        self.assertEqual(node_4.left, NIL_LEAF)
        self.assertEqual(node_4.right, NIL_LEAF)
        self.assertEqual(node_4.parent.value, 5)

        self.assertEqual(node_5.parent.value, 2)
        self.assertEqual(node_5.color, BLACK)
        self.assertEqual(node_5.left.value, 4)
        self.assertEqual(node_5.right.value, 9)

        rb_tree.add(3)
        """
            __2B__                                  __2B__
          1B      5B     ---CAUSES RECOLOR-->     1B      5R
                4R  9R                                  4B  9B
               3R                                      3R
        """
        expected_values = [1, 2, 3, 4, 5, 9]
        values = list(rb_tree)
        self.assertEqual(values, expected_values)

        node_3 = node_4.left
        self.assertEqual(node_3.value, 3)
        self.assertEqual(node_3.color, RED)
        self.assertEqual(node_3.left, NIL_LEAF)
        self.assertEqual(node_3.right, NIL_LEAF)
        self.assertEqual(node_3.parent.value, 4)

        self.assertEqual(node_4.color, BLACK)
        self.assertEqual(node_4.right, NIL_LEAF)
        self.assertEqual(node_4.parent.value, 5)

        self.assertEqual(node_9.color, BLACK)
        self.assertEqual(node_9.parent.value, 5)

        self.assertEqual(node_5.color, RED)
        self.assertEqual(node_5.left.value, 4)
        self.assertEqual(node_5.right.value, 9)

        rb_tree.add(6)
        """
        Nothing special
           __2B__
         1B      5R___
               4B    _9B
              3R    6R
        """
        expected_values = [1, 2, 3, 4, 5, 6, 9]
        values = list(rb_tree)
        self.assertEqual(values, expected_values)

        node_6 = node_9.left
        self.assertEqual(node_6.value, 6)
        self.assertEqual(node_6.color, RED)
        self.assertEqual(node_6.parent.value, 9)
        self.assertEqual(node_6.left, NIL_LEAF)
        self.assertEqual(node_6.right, NIL_LEAF)

        rb_tree.add(7)
        """
                   __2B__                                                    __2B__
                 1B      ___5R___             ---LEFT  ROTATION TO-->       1B   ___5R___
                       4B      _9B_                                             4B      9B
                     3R       6R                                               3R      7R
                               7R                                                     6B
            RIGHT ROTATION (RECOLOR) TO
                 __2B__
               1B    ___5R___
                    4B      7B
                   3R     6R  9R
        """
        expected_values = [1, 2, 3, 4, 5, 6, 7, 9]
        values = list(rb_tree)
        self.assertEqual(values, expected_values)

        node_7 = node_5.right
        self.assertEqual(node_7.value, 7)
        self.assertEqual(node_7.color, BLACK)
        self.assertEqual(node_7.left.value, 6)
        self.assertEqual(node_7.right.value, 9)
        self.assertEqual(node_7.parent.value, 5)

        self.assertEqual(node_5.color, RED)
        self.assertEqual(node_5.right.value, 7)

        self.assertEqual(node_6.color, RED)
        self.assertEqual(node_6.left, NIL_LEAF)
        self.assertEqual(node_6.right, NIL_LEAF)
        self.assertEqual(node_6.parent.value, 7)

        self.assertEqual(node_9.color, RED)
        self.assertEqual(node_9.left, NIL_LEAF)
        self.assertEqual(node_9.right, NIL_LEAF)
        self.assertEqual(node_9.parent.value, 7)

        rb_tree.add(15)
        """
                    __2B__                                         __2B__
               1B    ___5R___                                    1B    ___5R___
                    4B      7B       ---RECOLORS TO-->                4B       7R
                   3R     6R  9R                                     3R       6B 9B
                               15R                                                15R
                Red-red relationship on 5R-7R. 7R's sibling is BLACK, so we need to rotate.
                7 is the right child of 5, 5 is the right child of 2, so we have RR => L: Left rotation with recolor
                What we get is:

                            ___5B___
                        __2R__      7R
                      1B     4B    6B 9B
                            3R         15R
        """
        expected_values = [1, 2, 3, 4, 5, 6, 7, 9, 15]
        values = list(rb_tree)
        self.assertEqual(values, expected_values)

        node_15 = node_9.right
        self.assertEqual(node_15.color, RED)
        self.assertEqual(node_15.parent.value, 9)
        self.assertEqual(node_15.left, NIL_LEAF)
        self.assertEqual(node_15.right, NIL_LEAF)

        self.assertEqual(node_9.color, BLACK)
        self.assertEqual(node_9.left, NIL_LEAF)
        self.assertEqual(node_9.right.value, 15)
        self.assertEqual(node_9.parent.value, 7)

        self.assertEqual(node_6.color, BLACK)

        self.assertEqual(node_7.color, RED)
        self.assertEqual(node_7.left.value, 6)
        self.assertEqual(node_7.right.value, 9)

        self.assertEqual(rb_tree.root.value, 5)
        self.assertIsNone(node_5.parent)
        self.assertEqual(node_5.right.value, 7)
        self.assertEqual(node_5.left.value, 2)

        self.assertEqual(node_2.color, RED)
        self.assertEqual(node_2.parent.value, 5)
        self.assertEqual(node_2.left.value, 1)
        self.assertEqual(node_2.right.value, 4)

        self.assertEqual(node_4.parent.value, 2)
        self.assertEqual(node_4.color, BLACK)
        self.assertEqual(node_4.left.value, 3)
        self.assertEqual(node_4.right, NIL_LEAF)

    def test_right_left_rotation_after_recolor(self):
        rb_tree = RedBlackTree()
        root = Node(value=10, color=BLACK, parent=None,
                    left=NIL_LEAF, right=NIL_LEAF)
        node_10 = root

        # left subtree
        node_5 = Node(value=5, color=BLACK, parent=root,
                      left=NIL_LEAF, right=NIL_LEAF)

        # right subtree
        node_20 = Node(value=20, color=RED, parent=root,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_15 = Node(value=15, color=BLACK, parent=node_20,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_25 = Node(value=25, color=BLACK, parent=node_20,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_20.left = node_15
        node_20.right = node_25

        node_12 = Node(value=12, color=RED, parent=node_15,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_17 = Node(value=17, color=RED, parent=node_15,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_15.left = node_12
        node_15.right = node_17

        root.left = node_5
        root.right = node_20
        rb_tree.root = root
        rb_tree.add(19)

        """
                    ____10B____                           ____10B____
                   5B      __20R__                       5B      __20R__
                      __15B__   25B   --RECOLORS TO-->      __15R__   25B
                   12R      17R                          12B      17B
                       Add-->19R                                   19R


                                  ____10B____
    LR=>RL: Right rotation to   5B          ___15R___
                                         12B      __20R__
                                                17B      25B
                                                  19R


                                     ______15B_____
       Left rotation to           10R           __20R__
                                5B  12B     __17B__    25B
                                                  19R
        """
        expected_values = [5, 10, 12, 15, 17, 19, 20, 25]
        values = list(rb_tree)
        self.assertEqual(values, expected_values)

        node_19 = node_17.right

        self.assertEqual(node_19.value, 19)
        self.assertEqual(node_19.color, RED)
        self.assertEqual(node_19.left, NIL_LEAF)
        self.assertEqual(node_19.right, NIL_LEAF)
        self.assertEqual(node_19.parent, node_17)

        self.assertEqual(node_17.parent, node_20)
        self.assertEqual(node_17.color, BLACK)
        self.assertEqual(node_17.left, NIL_LEAF)
        self.assertEqual(node_17.right, node_19)

        self.assertEqual(node_20.parent, node_15)
        self.assertEqual(node_20.color, RED)
        self.assertEqual(node_20.left, node_17)
        self.assertEqual(node_20.right, node_25)

        self.assertEqual(rb_tree.root, node_15)
        self.assertIsNone(node_15.parent)
        self.assertEqual(node_15.left, node_10)
        self.assertEqual(node_15.right, node_20)
        self.assertEqual(node_15.color, BLACK)

        self.assertEqual(node_10.parent, node_15)
        self.assertEqual(node_10.color, RED)
        self.assertEqual(node_10.right, node_12)
        self.assertEqual(node_10.left, node_5)

        self.assertEqual(node_12.color, BLACK)
        self.assertEqual(node_12.parent, node_10)
        self.assertEqual(node_12.left, NIL_LEAF)
        self.assertEqual(node_12.right, NIL_LEAF)

    def test_right_rotation_after_recolor(self):
        rb_tree = RedBlackTree()
        root = Node(value=10, color=BLACK, parent=None,
                    left=NIL_LEAF, right=NIL_LEAF)
        node_10 = root
        # left subtree
        node_m10 = Node(value=-10, color=RED, parent=root,
                        left=NIL_LEAF, right=NIL_LEAF)
        node_6 = Node(value=6, color=BLACK, parent=node_m10,
                      left=NIL_LEAF, right=NIL_LEAF)
        node_m20 = Node(value=-20, color=BLACK, parent=node_m10,
                        left=NIL_LEAF, right=NIL_LEAF)
        node_m10.left = node_m20
        node_m10.right = node_6
        node_m21 = Node(value=-21, color=RED, parent=node_m20,
                        left=NIL_LEAF, right=NIL_LEAF)
        node_m19 = Node(value=-19, color=RED, parent=node_m20,
                        left=NIL_LEAF, right=NIL_LEAF)
        node_m20.left = node_m21
        node_m20.right = node_m19
        # right subtree
        node_20 = Node(value=20, color=BLACK, parent=root,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_15 = Node(value=15, color=RED, parent=node_20,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_25 = Node(value=25, color=RED, parent=node_20,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_20.left = node_15
        node_20.right = node_25

        root.left = node_m10
        root.right = node_20
        rb_tree.root = root
        rb_tree.add(-22)

        """

                    _____10_____                                               _____10_____
                   /            \                                             /            \
                -10R           20B                                         -10R           20B
               /    \          /   \                                      /   \          /    \
            -20B    6B       15R  25R     --RECOLOR TO-->              -20R    6B       15R  25R
            /   \                                                       /  \
          -21R -19R                                                   -21B -19B
           /                                                         /
 Add-> -22R                                                        22R



                                        ____-10B_____
                                       /             \
                                     -20R          __10R__
                                     /   \        /       \
        Right rotation to->       -21B  -19B     6B    __20B__
                                   /                  /       \
                                -22R                 15R     25R

        """
        expected_values = [-22, -21, -20, -19, -10, 6, 10, 15, 20, 25]
        values = list(rb_tree)
        self.assertEqual(values, expected_values)

        self.assertEqual(rb_tree.root, node_m10)
        self.assertEqual(node_m10.parent, None)
        self.assertEqual(node_m10.left, node_m20)
        self.assertEqual(node_m10.right, node_10)
        self.assertEqual(node_m10.color, BLACK)

        self.assertEqual(node_10.parent, node_m10)
        self.assertEqual(node_10.color, RED)
        self.assertEqual(node_10.left, node_6)
        self.assertEqual(node_10.right, node_20)

        self.assertEqual(node_m20.parent, node_m10)
        self.assertEqual(node_m20.color, RED)
        self.assertEqual(node_m20.left, node_m21)
        self.assertEqual(node_m20.right, node_m19)

        self.assertEqual(node_m21.color, BLACK)
        self.assertEqual(node_m21.left.value, -22)

        self.assertEqual(node_6.parent, node_10)
        self.assertEqual(node_6.color, BLACK)
        self.assertEqual(node_6.left, NIL_LEAF)
        self.assertEqual(node_6.right, NIL_LEAF)

        self.assertEqual(node_m19.color, BLACK)
        self.assertEqual(node_m19.parent, node_m20)
        self.assertEqual(node_m19.left, NIL_LEAF)
        self.assertEqual(node_m19.right, NIL_LEAF)

    # ***************TEST INSERTIONS***************

    # ***************TEST DELETIONS***************

    def test_deletion_root(self):
        rb_tree = RedBlackTree()
        root = Node(value=5, color=BLACK, parent=None,
                    left=NIL_LEAF, right=NIL_LEAF)
        left_child = Node(value=3, color=RED, parent=root,
                          left=NIL_LEAF, right=NIL_LEAF)
        right_child = Node(value=8, color=RED, parent=root,
                           left=NIL_LEAF, right=NIL_LEAF)
        root.left = left_child
        root.right = right_child
        """
      REMOVE--> __5__                     __8B__
               /     \     --Result-->   /
             3R      8R                3R
        """
        rb_tree.root = root
        rb_tree.remove(5)

        expected_values = [3, 8]
        values = list(rb_tree)
        self.assertEqual(values, expected_values)

        node_8 = rb_tree.root
        self.assertEqual(node_8.value, 8)
        self.assertEqual(node_8.color, BLACK)
        self.assertEqual(node_8.parent, None)
        self.assertEqual(node_8.left.value, 3)
        self.assertEqual(node_8.right, NIL_LEAF)
        node_3 = node_8.left
        self.assertEqual(node_3.color, RED)
        self.assertEqual(node_3.parent, node_8)
        self.assertEqual(node_3.left, NIL_LEAF)
        self.assertEqual(node_3.right, NIL_LEAF)

    def test_deletion_root_2_nodes(self):
        rb_tree = RedBlackTree()
        root = Node(value=5, color=BLACK, parent=None,
                    left=NIL_LEAF, right=NIL_LEAF)
        right_child = Node(value=8, color=RED, parent=root,
                           left=NIL_LEAF, right=NIL_LEAF)
        root.right = right_child
        rb_tree.root = root
        rb_tree.remove(5)
        """
                __5B__ <-- REMOVE        __8B__
                     \      Should become--^
                     8R
        """
        expected_values = [8]
        values = list(rb_tree)
        self.assertEqual(values, expected_values)

        root = rb_tree.root
        self.assertEqual(root.value, 8)
        self.assertEqual(root.parent, None)
        self.assertEqual(root.color, BLACK)
        self.assertEqual(root.left, NIL_LEAF)
        self.assertEqual(root.right, NIL_LEAF)

    def test_delete_single_child(self):
        rb_tree = RedBlackTree()
        root = Node(value=5, color=BLACK, parent=None,
                    left=NIL_LEAF, right=NIL_LEAF)
        left_child = Node(value=1, color=RED, parent=root,
                          left=NIL_LEAF, right=NIL_LEAF)
        right_child = Node(value=6, color=RED, parent=root,
                           left=NIL_LEAF, right=NIL_LEAF)
        root.left = left_child
        root.right = right_child
        rb_tree.root = root
        rb_tree.remove(6)
        """
           5                        5B
          / \   should become      /
        1R   6R                   1R
        """
        expected_values = [1, 5]
        values = list(rb_tree)
        self.assertEqual(values, expected_values)

        self.assertEqual(root.right, NIL_LEAF)
        self.assertEqual(root.value, 5)
        self.assertEqual(root.color, BLACK)
        self.assertEqual(root.parent, None)
        self.assertEqual(root.left.value, 1)
        node_1 = root.left
        self.assertEqual(node_1.left, NIL_LEAF)
        self.assertEqual(node_1.right, NIL_LEAF)

    def test_delete_single_deep_child(self):
        rb_tree = RedBlackTree()
        root = Node(value=20, color=BLACK, parent=None,
                    left=NIL_LEAF, right=NIL_LEAF)
        # left subtree
        node_10 = Node(value=10, color=BLACK, parent=None,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_5 = Node(value=5, color=RED, parent=node_10,
                      left=NIL_LEAF, right=NIL_LEAF)
        node_15 = Node(value=15, color=RED, parent=node_10,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_10.left = node_5
        node_10.right = node_15
        # right subtree
        node_38 = Node(value=38, color=RED, parent=root,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_28 = Node(value=28, color=BLACK, parent=node_38,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_48 = Node(value=48, color=BLACK, parent=node_38,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_38.left = node_28
        node_38.right = node_48
        # node_28 subtree
        node_23 = Node(value=23, color=RED, parent=node_28,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_29 = Node(value=29, color=RED, parent=node_28,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_28.left = node_23
        node_28.right = node_29
        # node 48 subtree
        node_41 = Node(value=41, color=RED, parent=node_48,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_49 = Node(value=49, color=RED, parent=node_48,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_48.left = node_41
        node_48.right = node_49

        root.left = node_10
        root.right = node_38
        rb_tree.root = root
        rb_tree.remove(49)
        """
                ______20______
               /              \
             10B           ___38R___
            /   \         /         \
          5R    15R      28B         48B
                        /  \        /   \
                      23R  29R     41R   49R    <--- REMOVE
        """
        expected_values = [5, 10, 15, 20, 23, 28, 29, 38, 41, 48]
        values = list(rb_tree)
        self.assertEqual(values, expected_values)

        self.assertEqual(node_48.right, NIL_LEAF)
        self.assertEqual(node_48.color, BLACK)
        self.assertEqual(node_48.left.value, 41)
        self.assertIsNone(rb_tree.find_node(49))  # assure its not in the tree

    def test_deletion_red_node_red_successor_no_children(self):
        """
        This must be the easiest deletion yet!
        """
        rb_tree = RedBlackTree()
        root = Node(value=10, color=BLACK, parent=None,
                    left=NIL_LEAF, right=NIL_LEAF)
        # Left subtree
        node_5 = Node(value=5, color=RED, parent=root,
                      left=NIL_LEAF, right=NIL_LEAF)
        node_m5 = Node(value=-5, color=BLACK, parent=root,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_7 = Node(value=7, color=BLACK, parent=node_5,
                      left=NIL_LEAF, right=NIL_LEAF)
        node_5.left = node_m5
        node_5.right = node_7

        # right subtree
        node_35 = Node(value=35, color=RED, parent=root,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_20 = Node(value=20, color=BLACK, parent=node_35,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_38 = Node(value=38, color=BLACK, parent=node_35,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_35.left = node_20
        node_35.right = node_38
        node_36 = Node(value=36, color=RED, parent=node_38,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_38.left = node_36

        root.left = node_5
        root.right = node_35
        rb_tree.root = root
        rb_tree.remove(35)

        """
                    10B
                  /     \
                5R       35R   <-- REMOVE THIS
               /  \     /   \
            -5B   7B   20B  38B   We get it's in-order successor, which is 36
                           /
                          36R     36 Is red and has no children, so we easily swap it's value with 35 and remove 36

                      10B
                    /     \
     RESULT IS    5R       36R
                 /  \     /   \
              -5B   7B   20B  38B
        """
        expected_values = [-5, 5, 7, 10, 20, 36, 38]
        values = list(rb_tree)
        self.assertEqual(values, expected_values)

        # Careful with reference equals
        node_36 = rb_tree.root.right
        self.assertEqual(node_36.value, 36)
        self.assertEqual(node_36.color, RED)
        self.assertEqual(node_36.parent, rb_tree.root)
        self.assertEqual(node_36.left.value, 20)
        self.assertEqual(node_36.right.value, 38)

        self.assertEqual(node_20.parent.value, 36)
        self.assertEqual(node_38.parent.value, 36)
        self.assertEqual(node_38.left, NIL_LEAF)

    def test_mirror_deletion_red_node_red_successor_no_children(self):
        """
        This must be the easiest deletion yet!
        """
        rb_tree = RedBlackTree()
        root = Node(value=10, color=BLACK, parent=None,
                    left=NIL_LEAF, right=NIL_LEAF)
        # Left subtree
        node_5 = Node(value=5, color=RED, parent=root,
                      left=NIL_LEAF, right=NIL_LEAF)
        node_m5 = Node(value=-5, color=BLACK, parent=root,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_7 = Node(value=7, color=BLACK, parent=node_5,
                      left=NIL_LEAF, right=NIL_LEAF)
        node_5.left = node_m5
        node_5.right = node_7
        node_6 = Node(value=6, color=RED, parent=node_7,
                      left=NIL_LEAF, right=NIL_LEAF)
        node_7.left = node_6

        # right subtree
        node_35 = Node(value=35, color=RED, parent=root,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_20 = Node(value=20, color=BLACK, parent=node_35,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_38 = Node(value=38, color=BLACK, parent=node_35,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_35.left = node_20
        node_35.right = node_38
        node_36 = Node(value=36, color=RED, parent=node_38,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_38.left = node_36

        root.left = node_5
        root.right = node_35
        rb_tree.root = root
        rb_tree.remove(5)

        """
                    10B
                  /     \
    REMOVE -->  5R       35R
               /  \     /   \
            -5B   7B   20B  38B   We get it's in-order successor, which is 6
                 /         /
               6R         36R      6 Is red and has no children,
                                    so we easily swap it's value with 5 and remove 6

                      10B
                    /     \
     RESULT IS    6R       35R
                 /  \     /   \
              -5B   7B   20B  38B
                             /
                            36R
        """
        expected_values = [-5, 6, 7, 10, 20, 35, 36, 38]
        values = list(rb_tree)
        self.assertEqual(values, expected_values)

        node_6 = rb_tree.root.left
        self.assertEqual(node_6.value, 6)
        self.assertEqual(node_6.color, RED)
        self.assertEqual(node_6.parent, rb_tree.root)
        self.assertEqual(node_6.left.value, -5)
        self.assertEqual(node_6.right.value, 7)
        node_7 = node_6.right
        self.assertEqual(node_7.color, BLACK)
        self.assertEqual(node_7.parent, node_6)
        self.assertEqual(node_7.left, NIL_LEAF)
        self.assertEqual(node_7.right, NIL_LEAF)

    def test_deletion_black_node_black_successor_right_red_child(self):
        """ fuck it i don't even know anymore """
        rb_tree = RedBlackTree()
        root = Node(value=10, color=BLACK, parent=None,
                    left=NIL_LEAF, right=NIL_LEAF)
        # left subtree
        node_5 = Node(value=5, color=BLACK, parent=root,
                      left=NIL_LEAF, right=NIL_LEAF)
        node_m5 = Node(value=-5, color=BLACK, parent=node_5,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_7 = Node(value=7, color=BLACK, parent=node_5,
                      left=NIL_LEAF, right=NIL_LEAF)
        node_5.left = node_m5
        node_5.right = node_7
        # right subtree
        node_30 = Node(value=30, color=BLACK, parent=root,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_20 = Node(value=20, color=BLACK, parent=node_30,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_38 = Node(value=38, color=RED, parent=node_30,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_30.left = node_20
        node_30.right = node_38
        # 38 subtree
        node_32 = Node(value=32, color=BLACK, parent=node_38,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_41 = Node(value=41, color=BLACK, parent=node_38,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_38.left = node_32
        node_38.right = node_41
        node_35 = Node(value=35, color=RED, parent=node_32,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_32.right = node_35

        root.left = node_5
        root.right = node_30

        rb_tree.root = root
        rb_tree.remove(30)
        """
                         ___10B___                                             ___10B___
                        /         \                                           /         \
                       5B         30B  <------- REMOVE THIS                  5B         32B  <----
                      /  \       /   \                                      /  \       /   \
                    -5B  7B    20B   38R                                  -5B  7B    20B   38R
                                    /   \                                                 /   \
                   successor ---> 32B    41B                                       -->  35B    41B
                                     \             30B becomes 32B
                                     35R           old 32B becomes 35B
        """
        expected_values = [-5, 5, 7, 10, 20, 32, 35, 38, 41]
        values = list(rb_tree)
        self.assertEqual(values, expected_values)

        node_32 = node_30
        self.assertEqual(node_32.value, 32)
        self.assertEqual(node_32.parent.value, 10)
        self.assertEqual(node_32.color, BLACK)
        self.assertEqual(node_32.left, node_20)
        self.assertEqual(node_32.right, node_38)

        node_35 = node_38.left
        self.assertEqual(node_35.value, 35)
        self.assertEqual(node_35.parent.value, 38)
        self.assertEqual(node_35.color, BLACK)
        self.assertEqual(node_35.left, NIL_LEAF)
        self.assertEqual(node_35.right, NIL_LEAF)

    def test_deletion_black_node_black_successor_no_child_case_4(self):
        rb_tree = RedBlackTree()
        root = Node(value=10, color=BLACK, parent=None,
                    left=NIL_LEAF, right=NIL_LEAF)
        # left subtree
        node_m10 = Node(value=-10, color=BLACK, parent=root,
                        left=NIL_LEAF, right=NIL_LEAF)
        # right subtree
        node_30 = Node(value=30, color=RED, parent=root,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_20 = Node(value=20, color=BLACK, parent=node_30,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_38 = Node(value=38, color=BLACK, parent=node_30,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_30.left = node_20
        node_30.right = node_38

        root.left = node_m10
        root.right = node_30
        rb_tree.root = root
        rb_tree.remove(10)

        """
                  ___10B___   <----- REMOVE THIS       ___20B___
                 /         \                          /         \
               -10B        30R                      -10B        30R
                          /   \                                /   \
         successor --> 20B    38B                double black DB  38B
                                                Case 4 applies, since the sibling is black, has no red children and
                                                the parent is RED
                                                So, we simply exchange colors of the parent and the sibling


                       ___20B___
                      /         \
                    -10B        30B        DONE
                                   \
                                  38R

        """
        expected_values = [-10, 20, 30, 38]
        values = list(rb_tree)
        self.assertEqual(values, expected_values)

        self.assertEqual(rb_tree.root.value, 20)
        self.assertEqual(rb_tree.root.color, BLACK)
        node_30 = rb_tree.root.right
        self.assertEqual(node_30.parent.value, 20)
        self.assertEqual(node_30.value, 30)
        self.assertEqual(node_30.color, BLACK)
        self.assertEqual(node_30.left, NIL_LEAF)
        self.assertEqual(node_30.right.value, 38)
        node_38 = node_30.right
        self.assertEqual(node_38.value, 38)
        self.assertEqual(node_38.color, RED)
        self.assertEqual(node_38.left, NIL_LEAF)
        self.assertEqual(node_38.right, NIL_LEAF)

    def test_deletion_black_node_no_successor_case_6(self):
        rb_tree = RedBlackTree()
        root = Node(value=10, color=BLACK, parent=None,
                    left=NIL_LEAF, right=NIL_LEAF)
        # left subtree
        node_m10 = Node(value=-10, color=BLACK, parent=root,
                        left=NIL_LEAF, right=NIL_LEAF)
        # right subtree
        node_30 = Node(value=30, color=BLACK, parent=root,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_25 = Node(value=25, color=RED, parent=node_30,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_40 = Node(value=40, color=RED, parent=node_30,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_30.left = node_25
        node_30.right = node_40

        root.left = node_m10
        root.right = node_30
        rb_tree.root = root
        rb_tree.remove(-10)

        """
                        ___10B___
                       /         \           Case 6 applies here, since
         REMOVE-->  -10B         30B         The parent's color does not matter
         Double Black           /   \        The sibling's color is BLACK
                              25R    40R     The sibling's right child is RED (in the MIRROR CASE - left child should be RED)
        Here we do a left rotation and change the colors such that
            the sibling gets the parent's color (30 gets 10's color)
            the parent(now sibling's left) and sibling's right become BLACK


                 ___30B___
                /         \
              10B         40B
            /    \
         NULL    25R
        -10B
        would be here
        but we're removing it
        """
        self.assertEqual(rb_tree.root.color, BLACK)
        self.assertEqual(rb_tree.root.value, 30)
        node_10 = rb_tree.root.left
        self.assertEqual(node_10.value, 10)
        self.assertEqual(node_10.color, BLACK)
        self.assertEqual(node_10.parent, rb_tree.root)
        self.assertEqual(node_10.left, NIL_LEAF)
        node_25 = node_10.right
        self.assertEqual(node_25.value, 25)
        self.assertEqual(node_25.color, RED)
        self.assertEqual(node_25.parent, node_10)
        self.assertEqual(node_25.left, NIL_LEAF)
        self.assertEqual(node_25.right, NIL_LEAF)
        node_40 = rb_tree.root.right
        self.assertEqual(node_40.value, 40)
        self.assertEqual(node_40.parent, rb_tree.root)
        self.assertEqual(node_40.color, BLACK)
        self.assertEqual(node_40.left, NIL_LEAF)
        self.assertEqual(node_40.right, NIL_LEAF)

    def test_mirror_deletion_black_node_no_successor_case_6(self):
        rb_tree = RedBlackTree()
        root = Node(value=10, color=BLACK, parent=None,
                    left=NIL_LEAF, right=NIL_LEAF)
        node_12 = Node(value=12, color=BLACK, parent=root,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_5 = Node(value=5, color=BLACK, parent=root,
                      left=NIL_LEAF, right=NIL_LEAF)
        node_1 = Node(value=1, color=RED, parent=node_5,
                      left=NIL_LEAF, right=NIL_LEAF)
        node_7 = Node(value=7, color=RED, parent=node_5,
                      left=NIL_LEAF, right=NIL_LEAF)
        node_5.left = node_1
        node_5.right = node_7
        root.left = node_5
        root.right = node_12
        rb_tree.root = root
        rb_tree.remove(12)
        """
                   __10B__                                           __5B__
                   /      \                                         /      \
                 5B       12B  <--- REMOVE                        1B        10B
                /  \              has no successors                        /
              1R   7R                                                    7R
                            case 6 applies, so we left rotate at 5b
        """
        node_5 = rb_tree.root
        self.assertEqual(node_5.value, 5)
        self.assertEqual(node_5.color, BLACK)
        self.assertEqual(node_5.parent, None)
        self.assertEqual(node_5.left.value, 1)
        self.assertEqual(node_5.right.value, 10)
        node_1 = node_5.left
        self.assertEqual(node_1.value, 1)
        self.assertEqual(node_1.parent, node_5)
        self.assertEqual(node_1.color, BLACK)
        self.assertEqual(node_1.left, NIL_LEAF)
        self.assertEqual(node_1.right, NIL_LEAF)
        node_10 = node_5.right
        self.assertEqual(node_10.value, 10)
        self.assertEqual(node_10.parent, node_5)
        self.assertEqual(node_10.color, BLACK)
        self.assertEqual(node_10.left.value, 7)
        self.assertEqual(node_10.right, NIL_LEAF)
        node_7 = node_10.left
        self.assertEqual(node_7.value, 7)
        self.assertEqual(node_7.parent, node_10)
        self.assertEqual(node_7.color, RED)
        self.assertEqual(node_7.left, NIL_LEAF)
        self.assertEqual(node_7.right, NIL_LEAF)

    def test_deletion_black_node_no_successor_case_3_then_1(self):
        """
        Delete a node such that case 3 is called, which pushes
        the double black node upwards into a case 1 problem
        """
        rb_tree = RedBlackTree()
        root = Node(value=10, color=BLACK, parent=None,
                    left=NIL_LEAF, right=NIL_LEAF)
        # left subtree
        node_m10 = Node(value=-10, color=BLACK, parent=root,
                        left=NIL_LEAF, right=NIL_LEAF)
        # right subtree
        node_30 = Node(value=30, color=BLACK, parent=root,
                       left=NIL_LEAF, right=NIL_LEAF)

        root.left = node_m10
        root.right = node_30
        rb_tree.root = root
        rb_tree.remove(-10)

        """                                             Double
                                                        Black
                    ___10B___                         __|10B|__
                   /         \     ---->             /         \
    REMOVE-->   -10B         30B                  REMOVED      30R  <--- COLORED RED

            We color the sibling red and try to resolve the double black problem in the root.
            We go through the cases 1-6 and find that case 1 is what we're looking for
            Case 1 simply recolors the root to black and we are done
                ___10B___
                         \
                         30R
        """
        node_10 = rb_tree.root
        self.assertEqual(node_10.color, BLACK)
        self.assertEqual(node_10.parent, None)
        self.assertEqual(node_10.left, NIL_LEAF)
        self.assertEqual(node_10.right.value, 30)
        node_30 = node_10.right
        self.assertEqual(node_30.value, 30)
        self.assertEqual(node_30.color, RED)
        self.assertEqual(node_30.parent, node_10)
        self.assertEqual(node_30.left, NIL_LEAF)
        self.assertEqual(node_30.right, NIL_LEAF)

    def test_deletion_black_node_no_successor_case_3_then_5_then_6(self):
        """
        We're going to delete a black node which will cause a case 3 deletion
        which in turn would pass the double black node up into a case 5, which
        will restructure the tree in such a way that a case 6 rotation becomes possible
        """
        rb_tree = RedBlackTree()
        root = Node(value=10, color=BLACK, parent=None,
                    left=NIL_LEAF, right=NIL_LEAF)
        # left subtree
        node_m30 = Node(value=-30, color=BLACK, parent=root,
                        left=NIL_LEAF, right=NIL_LEAF)
        node_m40 = Node(value=-40, color=BLACK, parent=node_m30,
                        left=NIL_LEAF, right=NIL_LEAF)
        node_m20 = Node(value=-20, color=BLACK, parent=node_m30,
                        left=NIL_LEAF, right=NIL_LEAF)
        node_m30.left = node_m40
        node_m30.right = node_m20
        # right subtree
        node_50 = Node(value=50, color=BLACK, parent=root,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_30 = Node(value=30, color=RED, parent=node_50,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_70 = Node(value=70, color=BLACK, parent=node_50,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_50.left = node_30
        node_50.right = node_70
        node_15 = Node(value=15, color=BLACK, parent=node_30,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_40 = Node(value=40, color=BLACK, parent=node_30,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_30.left = node_15
        node_30.right = node_40

        root.left = node_m30
        root.right = node_50
        rb_tree.root = root
        rb_tree.remove(-40)
        """
        In mirror cases, this'd be mirrored
        |node| - double black node
                    ___10B___                                 ___10B___
                   /         \               DOUBLE          /         \
                -30B         50B             BLACK-->   |-30B|        50B
               /    \       /   \                        /    \       /   \
  REMOVE-->|-40B|  -20B   30R   70B     --CASE 3--> REMOVED  -20R   30R   70B
                         /   \                                     /   \
                       15B   40B                                 15B   40B



      --CASE 5-->                              ___10B___
      parent is black        still double     /         \
      sibling is black         black -->  |-30B|        30B
      sibling.left is red                     \        /   \
      sibling.right is black                  -20R   15B   50R
      left rotation on sibling.left                       /   \
                                                        40B   70B


      What we've done here is we've simply
      restructured the tree to be eligible
      for a case 6 solution :)                              ___30B___
      --CASE 6-->                                          /         \
      parent color DOESNT MATTER                         10B         50B
      sibling is black                                  /   \       /   \
      sibling.left DOESNT MATTER                     -30B   15B   40B   70B
      sibling.right is RED                              \
      left rotation on sibling (30B on the above)       -20R
      where the sibling gets the color of the parent
          and the parent is now to the left of sibling and
          repainted BLACK
          the sibling's right also gets repainted black
        """
        node_30 = rb_tree.root
        self.assertEqual(node_30.value, 30)
        self.assertEqual(node_30.parent, None)
        self.assertEqual(node_30.color, BLACK)
        self.assertEqual(node_30.left.value, 10)
        self.assertEqual(node_30.right.value, 50)

        # test left subtree
        node_10 = node_30.left
        self.assertEqual(node_10.value, 10)
        self.assertEqual(node_10.color, BLACK)
        self.assertEqual(node_10.parent, node_30)
        self.assertEqual(node_10.left.value, -30)
        self.assertEqual(node_10.right.value, 15)
        node_m30 = node_10.left
        self.assertEqual(node_m30.value, -30)
        self.assertEqual(node_m30.color, BLACK)
        self.assertEqual(node_m30.parent, node_10)
        self.assertEqual(node_m30.left, NIL_LEAF)
        self.assertEqual(node_m30.right.value, -20)
        node_15 = node_10.right
        self.assertEqual(node_15.value, 15)
        self.assertEqual(node_15.color, BLACK)
        self.assertEqual(node_15.parent, node_10)
        self.assertEqual(node_15.left, NIL_LEAF)
        self.assertEqual(node_15.right, NIL_LEAF)
        node_m20 = node_m30.right
        self.assertEqual(node_m20.value, -20)
        self.assertEqual(node_m20.color, RED)
        self.assertEqual(node_m20.parent, node_m30)
        self.assertEqual(node_m20.left, NIL_LEAF)
        self.assertEqual(node_m20.right, NIL_LEAF)

        # test right subtree
        node_50 = node_30.right
        self.assertEqual(node_50.value, 50)
        self.assertEqual(node_50.color, BLACK)
        self.assertEqual(node_50.parent, node_30)
        self.assertEqual(node_50.left.value, 40)
        self.assertEqual(node_50.right.value, 70)
        node_40 = node_50.left
        self.assertEqual(node_40.value, 40)
        self.assertEqual(node_40.parent, node_50)
        self.assertEqual(node_40.color, BLACK)
        self.assertEqual(node_40.left, NIL_LEAF)
        self.assertEqual(node_40.right, NIL_LEAF)
        node_70 = node_50.right
        self.assertEqual(node_70.value, 70)
        self.assertEqual(node_70.color, BLACK)
        self.assertEqual(node_70.parent, node_50)
        self.assertEqual(node_70.left, NIL_LEAF)
        self.assertEqual(node_70.right, NIL_LEAF)

    def test_mirror_deletion_black_node_no_successor_case_3_then_5_then_6(self):
        """
        We're going to delete a black node which will cause a case 3 deletion
        which in turn would pass the double black node up into a case 5, which
        will restructure the tree in such a way that a case 6 rotation becomes possible
        """
        rb_tree = RedBlackTree()
        root = Node(value=50, color=BLACK, parent=None,
                    left=NIL_LEAF, right=NIL_LEAF)
        # left subtree
        node_30 = Node(value=30, color=BLACK, parent=root,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_20 = Node(value=20, color=BLACK, parent=node_30,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_35 = Node(value=35, color=RED, parent=node_30,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_30.left = node_20
        node_30.right = node_35
        node_34 = Node(value=34, color=BLACK, parent=node_35,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_37 = Node(value=37, color=BLACK, parent=node_35,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_35.left = node_34
        node_35.right = node_37
        # right subtree
        node_80 = Node(value=80, color=BLACK, parent=root,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_70 = Node(value=70, color=BLACK, parent=node_80,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_90 = Node(value=90, color=BLACK, parent=node_80,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_80.left = node_70
        node_80.right = node_90

        root.left = node_30
        root.right = node_80
        rb_tree.root = root
        rb_tree.remove(90)

        """
                            Parent is black
               ___50B___    Sibling is black                       ___50B___
              /         \   Sibling's children are black          /         \
           30B          80B        CASE 3                       30B        |80B|
          /   \        /   \        ==>                        /  \        /   \
        20B   35R    70B    90B <---REMOVE                   20B  35R     70R   X
              /  \                                               /   \
            34B   37B                                          34B   37B



    Case 5
    Parent is black                                 __50B__
    Sibling is black             CASE 5            /       \
    Closer sibling child is RED  =====>          35B      |80B|
        (right in this case,                    /   \      /
         left in mirror)                     30R   37B    70R
    Outer sibling child is blck             /  \
                                         20B  34B


    We have now successfully position our tree
    for a CASE 6 scenario
    The parent's color does not matter                           __35B__
    The sibling is black                                        /       \
    The closer sibling child             CASE 6               30R       50R
        's color does not matter         ====>               /   \     /   \
    The outer sibling child                                20B   34B 37B    80B
        (left in this case,                                                 /
         right in mirror)                                                  70R
         is RED!
        """
        expected_values = [20, 30, 34, 35, 37, 50, 70, 80]
        values = list(rb_tree)
        self.assertEqual(values, expected_values)

        node_35 = rb_tree.root
        self.assertEqual(node_35.value, 35)
        self.assertEqual(node_35.parent, None)
        self.assertEqual(node_35.color, BLACK)
        self.assertEqual(node_35.left.value, 30)
        self.assertEqual(node_35.right.value, 50)
        # right subtree
        node_50 = node_35.right
        self.assertEqual(node_50.value, 50)
        self.assertEqual(node_50.color, BLACK)
        self.assertEqual(node_50.parent, node_35)
        self.assertEqual(node_50.left.value, 37)
        self.assertEqual(node_50.right.value, 80)
        node_37 = node_50.left
        self.assertEqual(node_37.value, 37)
        self.assertEqual(node_37.color, BLACK)
        self.assertEqual(node_37.parent, node_50)
        self.assertEqual(node_37.left, NIL_LEAF)
        self.assertEqual(node_37.right, NIL_LEAF)
        node_80 = node_50.right
        self.assertEqual(node_80.value, 80)
        self.assertEqual(node_80.color, BLACK)
        self.assertEqual(node_80.parent, node_50)
        self.assertEqual(node_80.left.value, 70)
        self.assertEqual(node_80.right, NIL_LEAF)
        node_70 = node_80.left
        self.assertEqual(node_70.value, 70)
        self.assertEqual(node_70.color, RED)
        self.assertEqual(node_70.parent, node_80)
        self.assertEqual(node_70.left, NIL_LEAF)
        self.assertEqual(node_70.right, NIL_LEAF)
        # left subtree
        node_30 = node_35.left
        self.assertEqual(node_30.value, 30)
        self.assertEqual(node_30.parent, node_35)
        self.assertEqual(node_30.color, BLACK)
        self.assertEqual(node_30.left.value, 20)
        self.assertEqual(node_30.right.value, 34)
        node_20 = node_30.left
        self.assertEqual(node_20.value, 20)
        self.assertEqual(node_20.color, BLACK)
        self.assertEqual(node_20.parent, node_30)
        self.assertEqual(node_20.left, NIL_LEAF)
        self.assertEqual(node_20.right, NIL_LEAF)
        node_34 = node_30.right
        self.assertEqual(node_34.value, 34)
        self.assertEqual(node_34.color, BLACK)
        self.assertEqual(node_34.parent, node_30)
        self.assertEqual(node_34.left, NIL_LEAF)
        self.assertEqual(node_34.right, NIL_LEAF)

    def test_deletion_black_node_successor_case_2_then_4(self):
        rb_tree = RedBlackTree()
        root = Node(value=10, color=BLACK, parent=None,
                    left=NIL_LEAF, right=NIL_LEAF)
        # left subtree
        node_m10 = Node(value=-10, color=BLACK, parent=root,
                        left=NIL_LEAF, right=NIL_LEAF)
        node_m20 = Node(value=-20, color=BLACK, parent=node_m10,
                        left=NIL_LEAF, right=NIL_LEAF)
        node_m5 = Node(value=-5, color=BLACK, parent=node_m10,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_m10.left = node_m20
        node_m10.right = node_m5
        # right subtree
        node_40 = Node(value=40, color=BLACK, parent=root,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_20 = Node(value=20, color=BLACK, parent=node_40,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_60 = Node(value=60, color=RED, parent=node_40,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_40.left = node_20
        node_40.right = node_60
        node_50 = Node(value=50, color=BLACK, parent=node_60,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_80 = Node(value=80, color=BLACK, parent=node_60,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_60.left = node_50
        node_60.right = node_80

        root.left = node_m10
        root.right = node_40
        rb_tree.root = root
        rb_tree.remove(10)
        """

  REMOVE--->    ___10B___           parent is black             ___20B___
               /         \          sibling is red            /         \
            -10B         40B        s.children aren't red    -10B         60B
           /    \       /   \       --CASE 2 ROTATE-->      /    \       /   \
        -20B    -5B |20B|   60R       LEFT ROTATE         -20B  -5B    40R   80B
    SUCCESSOR IS 20----^   /   \      SIBLING 60                      /   \
                         50B    80B                       REMOVE--> 20    50B


    CASE 4                                         ___20B___
    20'S parent is RED                           /         \
    sibling is BLACK                            -10B         60B
    sibling's children are NOT RED             /    \       /   \
        so we push parent's                  -20B  -5B    40B   80B
        redness down to the sibling                      /   \
        and remove node                      REMOVED--> X    50R
        """
        expected_values = [-20, -10, -5, 20, 40, 50, 60, 80]
        values = list(rb_tree)
        self.assertEqual(values, expected_values)

        node_20 = rb_tree.root
        self.assertEqual(node_20.value, 20)
        self.assertEqual(node_20.parent, None)
        self.assertEqual(node_20.color, BLACK)
        self.assertEqual(node_20.left.value, -10)
        self.assertEqual(node_20.right.value, 60)
        # test left subtree
        node_m10 = node_20.left
        self.assertEqual(node_m10.value, -10)
        self.assertEqual(node_m10.color, BLACK)
        self.assertEqual(node_m10.parent, node_20)
        self.assertEqual(node_m10.left.value, -20)
        self.assertEqual(node_m10.right.value, -5)
        node_m20 = node_m10.left
        self.assertEqual(node_m20.value, -20)
        self.assertEqual(node_m20.color, BLACK)
        self.assertEqual(node_m20.parent, node_m10)
        self.assertEqual(node_m20.left, NIL_LEAF)
        self.assertEqual(node_m20.right, NIL_LEAF)
        node_m5 = node_m10.right
        self.assertEqual(node_m5.value, -5)
        self.assertEqual(node_m5.color, BLACK)
        self.assertEqual(node_m5.parent, node_m10)
        self.assertEqual(node_m5.left, NIL_LEAF)
        self.assertEqual(node_m5.right, NIL_LEAF)
        # test right subtree
        node_60 = node_20.right
        self.assertEqual(node_60.value, 60)
        self.assertEqual(node_60.color, BLACK)
        self.assertEqual(node_60.parent, node_20)
        self.assertEqual(node_60.left.value, 40)
        self.assertEqual(node_60.right.value, 80)
        node_80 = node_60.right
        self.assertEqual(node_80.value, 80)
        self.assertEqual(node_80.color, BLACK)
        self.assertEqual(node_80.parent, node_60)
        self.assertEqual(node_80.left, NIL_LEAF)
        self.assertEqual(node_80.right, NIL_LEAF)
        node_40 = node_60.left
        self.assertEqual(node_40.value, 40)
        self.assertEqual(node_40.color, BLACK)
        self.assertEqual(node_40.parent, node_60)
        self.assertEqual(node_40.left, NIL_LEAF)
        self.assertEqual(node_40.right.value, 50)
        node_50 = node_40.right
        self.assertEqual(node_50.value, 50)
        self.assertEqual(node_50.color, RED)
        self.assertEqual(node_50.parent, node_40)
        self.assertEqual(node_50.left, NIL_LEAF)
        self.assertEqual(node_50.right, NIL_LEAF)

    def test_mirror_deletion_black_node_successor_case_2_then_4(self):
        rb_tree = RedBlackTree()
        root = Node(value=20, color=BLACK, parent=None,
                    left=NIL_LEAF, right=NIL_LEAF)
        # left subtree
        node_10 = Node(value=10, color=BLACK, parent=root,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_8 = Node(value=8, color=RED, parent=node_10,
                      left=NIL_LEAF, right=NIL_LEAF)
        node_15 = Node(value=15, color=BLACK, parent=node_10,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_10.left = node_8
        node_10.right = node_15
        node_6 = Node(value=6, color=BLACK, parent=node_8,
                      left=NIL_LEAF, right=NIL_LEAF)
        node_9 = Node(value=9, color=BLACK, parent=node_8,
                      left=NIL_LEAF, right=NIL_LEAF)
        node_8.left = node_6
        node_8.right = node_9
        # right subtree
        node_30 = Node(value=30, color=BLACK, parent=root,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_25 = Node(value=25, color=BLACK, parent=node_30,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_35 = Node(value=35, color=BLACK, parent=node_30,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_30.left = node_25
        node_30.right = node_35

        root.left = node_10
        root.right = node_30
        rb_tree.root = root
        rb_tree.remove(15)

        """

                ___20B___        Parent is black               ___20B___
               /         \       Sibling is red               /         \
            10B          30B     s.children are black        8B        30B
           /   \        /   \    ======>                    /  \       /   \
         8R    15B    25B   35B   Case 2                  6B   10R   25B   35B
        /  \    ^----Remove    left rotate                    /   \
       6B  9B                     on 10                      9B   |15B|



       Parent is red                                  ___20B___
       Sibling is black      CASE 4                  /         \
       s.children are black   ===>                  8B        30B
        switch the colors of the parent            /  \       /   \
        and the sibling                          6B   10B   25B   35B
                                                     /   \
                                                   9R     X
        """
        node_20 = rb_tree.root
        self.assertEqual(node_20.value, 20)
        self.assertEqual(node_20.color, BLACK)
        self.assertEqual(node_20.parent, None)
        self.assertEqual(node_20.left.value, 8)
        self.assertEqual(node_20.right.value, 30)
        # right subtree
        node_30 = node_20.right
        self.assertEqual(node_30.value, 30)
        self.assertEqual(node_30.color, BLACK)
        self.assertEqual(node_30.parent, node_20)
        self.assertEqual(node_30.left.value, 25)
        self.assertEqual(node_30.right.value, 35)
        node_25 = node_30.left
        self.assertEqual(node_25.value, 25)
        self.assertEqual(node_25.color, BLACK)
        self.assertEqual(node_25.parent, node_30)
        self.assertEqual(node_25.left, NIL_LEAF)
        self.assertEqual(node_25.right, NIL_LEAF)
        node_35 = node_30.right
        self.assertEqual(node_35.value, 35)
        self.assertEqual(node_35.color, BLACK)
        self.assertEqual(node_35.parent, node_30)
        self.assertEqual(node_35.left, NIL_LEAF)
        self.assertEqual(node_35.right, NIL_LEAF)
        # left subtree
        node_8 = node_20.left
        self.assertEqual(node_8.value, 8)
        self.assertEqual(node_8.parent, node_20)
        self.assertEqual(node_8.color, BLACK)
        self.assertEqual(node_8.left.value, 6)
        self.assertEqual(node_8.right.value, 10)
        node_6 = node_8.left
        self.assertEqual(node_6.value, 6)
        self.assertEqual(node_6.color, BLACK)
        self.assertEqual(node_6.parent, node_8)
        self.assertEqual(node_6.left, NIL_LEAF)
        self.assertEqual(node_6.right, NIL_LEAF)
        node_10 = node_8.right
        self.assertEqual(node_10.value, 10)
        self.assertEqual(node_10.color, BLACK)
        self.assertEqual(node_10.parent, node_8)
        self.assertEqual(node_10.left, node_9)
        self.assertEqual(node_10.right, NIL_LEAF)
        node_9 = node_10.left
        self.assertEqual(node_9.value, 9)
        self.assertEqual(node_9.color, RED)
        self.assertEqual(node_9.parent, node_10)
        self.assertEqual(node_9.left, NIL_LEAF)
        self.assertEqual(node_9.right, NIL_LEAF)

    def test_delete_tree_one_by_one(self):
        rb_tree = RedBlackTree()
        root = Node(value=20, color=BLACK, parent=None,
                    left=NIL_LEAF, right=NIL_LEAF)
        # left subtree
        node_10 = Node(value=10, color=BLACK, parent=root,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_5 = Node(value=5, color=RED, parent=node_10,
                      left=NIL_LEAF, right=NIL_LEAF)
        node_15 = Node(value=15, color=RED, parent=node_10,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_10.left = node_5
        node_10.right = node_15
        # right subtree
        node_38 = Node(value=38, color=RED, parent=root,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_28 = Node(value=28, color=BLACK, parent=node_38,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_48 = Node(value=48, color=BLACK, parent=node_38,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_38.left = node_28
        node_38.right = node_48
        # node_28 subtree
        node_23 = Node(value=23, color=RED, parent=node_28,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_29 = Node(value=29, color=RED, parent=node_28,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_28.left = node_23
        node_28.right = node_29
        # node 48 subtree
        node_41 = Node(value=41, color=RED, parent=node_48,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_49 = Node(value=49, color=RED, parent=node_48,
                       left=NIL_LEAF, right=NIL_LEAF)
        node_48.left = node_41
        node_48.right = node_49

        root.left = node_10
        root.right = node_38
        """
                        ______20______
                       /              \
                     10B           ___38R___
                    /   \         /         \
                  5R    15R      28B         48B
                                /  \        /   \
                              23R  29R     41R   49R
        """
        rb_tree.root = root
        rb_tree.remove(49)
        rb_tree.remove(38)
        rb_tree.remove(28)
        rb_tree.remove(10)
        rb_tree.remove(5)
        rb_tree.remove(15)
        rb_tree.remove(48)
        """
            We're left with
                            __23B__
                           /       \
                         20B       41B
                                  /
                                 29R
        """
        node_23 = rb_tree.root
        self.assertEqual(node_23.value, 23)
        self.assertEqual(node_23.color, BLACK)
        self.assertEqual(node_23.parent, None)
        self.assertEqual(node_23.left.value, 20)
        self.assertEqual(node_23.right.value, 41)
        node_20 = node_23.left
        self.assertEqual(node_20.color, BLACK)
        self.assertEqual(node_20.parent, node_23)
        self.assertEqual(node_20.left, NIL_LEAF)
        self.assertEqual(node_20.right, NIL_LEAF)
        node_41 = node_23.right
        self.assertEqual(node_41.color, BLACK)
        self.assertEqual(node_41.parent, node_23)
        self.assertEqual(node_41.value, 41)
        self.assertEqual(node_41.left.value, 29)
        self.assertEqual(node_41.right, NIL_LEAF)
        node_29 = node_41.left
        self.assertEqual(node_29.value, 29)
        self.assertEqual(node_29.color, RED)
        self.assertEqual(node_29.left, NIL_LEAF)
        self.assertEqual(node_29.right, NIL_LEAF)
        rb_tree.remove(20)
        """
            _29B_
           /     \
          23B    41B
        """
        node_29 = rb_tree.root
        self.assertEqual(node_29.value, 29)
        self.assertEqual(node_29.color, BLACK)
        self.assertEqual(node_29.parent, None)
        self.assertEqual(node_29.left.value, 23)
        self.assertEqual(node_29.right.value, 41)
        node_23 = node_29.left
        self.assertEqual(node_23.parent, node_29)
        self.assertEqual(node_23.color, BLACK)
        self.assertEqual(node_23.left, NIL_LEAF)
        self.assertEqual(node_23.right, NIL_LEAF)
        node_41 = node_29.right
        self.assertEqual(node_41.parent, node_29)
        self.assertEqual(node_41.color, BLACK)
        self.assertEqual(node_41.left, NIL_LEAF)
        self.assertEqual(node_41.right, NIL_LEAF)
        rb_tree.remove(29)
        """
            41B
           /
         23R
        """
        node_41 = rb_tree.root
        self.assertEqual(node_41.value, 41)
        self.assertEqual(node_41.color, BLACK)
        self.assertEqual(node_41.parent, None)
        self.assertEqual(node_41.right, NIL_LEAF)
        node_23 = node_41.left
        self.assertEqual(node_23.value, 23)
        self.assertEqual(node_23.color, RED)
        self.assertEqual(node_23.parent, node_41)
        self.assertEqual(node_23.left, NIL_LEAF)
        self.assertEqual(node_23.right, NIL_LEAF)
        rb_tree.remove(41)
        """
            23B
        """
        node_23 = rb_tree.root
        self.assertEqual(node_23.value, 23)
        self.assertEqual(node_23.color, BLACK)
        self.assertEqual(node_23.parent, None)
        self.assertEqual(node_23.left, NIL_LEAF)
        self.assertEqual(node_23.right, NIL_LEAF)
        rb_tree.remove(23)
        self.assertEqual(rb_tree.root, None)

    # ***************TEST DELETIONS***************

    def test_add_delete_random_order(self):
        """
        What I add here I'll also add at a site for red black tree visualization
        https://www.cs.usfca.edu/~galles/visualization/RedBlack.html
        and then see if they're the same
        """
        rb_tree = RedBlackTree()
        rb_tree.add(90)
        rb_tree.add(70)
        rb_tree.add(43)
        rb_tree.remove(70)
        rb_tree.add(24)
        rb_tree.add(14)
        rb_tree.add(93)
        rb_tree.add(47)
        rb_tree.remove(47)
        rb_tree.remove(90)
        rb_tree.add(57)
        rb_tree.add(1)
        rb_tree.add(60)
        rb_tree.add(47)
        rb_tree.remove(47)
        rb_tree.remove(1)
        rb_tree.remove(43)
        rb_tree.add(49)
        """
        well, the results aren't the same, but I'll assume that the algorithms are different
        Nevertheless, what we're left with is a perfectly valid RedBlack Tree, and, I'd argue, even betterly
        balanced than the one from the visualization

                                    VISUALIZATION TREE
                                       ____24B____
                                      /           \
                                    14B           60R
                                                 /   \
                                               57B    93B
                                              /
                                            49R

                                       OUR TREE
                                       ______57B______
                                      /               \
                                  __24B__           __60B__
                                 /       \                 \
                               14R       49R               93R
        """
        expected_values = [14, 24, 49, 57, 60, 93]
        values = list(rb_tree)
        self.assertEqual(values, expected_values)

        node_57 = rb_tree.root
        self.assertEqual(node_57.value, 57)
        self.assertEqual(node_57.parent, None)
        self.assertEqual(node_57.color, BLACK)
        self.assertEqual(node_57.left.value, 24)
        self.assertEqual(node_57.right.value, 60)
        # right subtree
        node_60 = node_57.right
        self.assertEqual(node_60.value, 60)
        self.assertEqual(node_60.color, BLACK)
        self.assertEqual(node_60.parent, node_57)
        self.assertEqual(node_60.right.value, 93)
        self.assertEqual(node_60.left, NIL_LEAF)
        node_93 = node_60.right
        self.assertEqual(node_93.value, 93)
        self.assertEqual(node_93.color, RED)
        self.assertEqual(node_93.parent, node_60)
        self.assertEqual(node_93.left, NIL_LEAF)
        self.assertEqual(node_93.right, NIL_LEAF)
        # left subtree
        node_24 = node_57.left
        self.assertEqual(node_24.value, 24)
        self.assertEqual(node_24.parent, node_57)
        self.assertEqual(node_24.color, BLACK)
        self.assertEqual(node_24.left.value, 14)
        self.assertEqual(node_24.right.value, 49)
        node_14 = node_24.left
        self.assertEqual(node_14.value, 14)
        self.assertEqual(node_14.parent, node_24)
        self.assertEqual(node_14.color, RED)
        self.assertEqual(node_14.left, NIL_LEAF)
        self.assertEqual(node_14.right, NIL_LEAF)
        node_49 = node_24.right
        self.assertEqual(node_49.value, 49)
        self.assertEqual(node_49.parent, node_24)
        self.assertEqual(node_49.color, RED)
        self.assertEqual(node_49.left, NIL_LEAF)
        self.assertEqual(node_49.right, NIL_LEAF)

    def test_add_0_to_100_delete_100_to_0(self):
        rb_tree = RedBlackTree()
        for i in range(100):
            rb_tree.add(i)
            self.assertEqual(rb_tree.count, i+1)
        expected_values = list(range(100))
        values = list(rb_tree)
        self.assertEqual(values, expected_values)
        for i in range(99, -1, -1):
            self.assertTrue(rb_tree.contains(i))
            rb_tree.remove(i)
            self.assertFalse(rb_tree.contains(i))
            self.assertEqual(rb_tree.count, i)
        self.assertIsNone(rb_tree.root)

    def test_add_delete_0_to_100_delete_0_to_100(self):
        rb_tree = RedBlackTree()
        for i in range(100):
            rb_tree.add(i)
            self.assertEqual(rb_tree.count, i+1)
        expected_values = list(range(100))
        values = list(rb_tree)
        self.assertEqual(values, expected_values)
        for i in range(100):
            self.assertTrue(rb_tree.contains(i))
            rb_tree.remove(i)
            self.assertFalse(rb_tree.contains(i))
            self.assertEqual(rb_tree.count, 99-i)
        self.assertIsNone(rb_tree.root)

    # ***************TEST DELETIONS***************

    # ***************MISC TESTS***************

    def test_ceil(self):
        # add all the numbers 0-99 step 2
        # i.e 0, 2, 4
        rb_tree = RedBlackTree()
        for i in range(0, 100, 2):
            rb_tree.add(i)
        # then search for the ceilings, knowing theyre 1 up
        for i in range(1, 99, 2):
            self.assertEqual(rb_tree.ceil(i), i+1)

    def test_ceil_same_value(self):
        rb_tree = RedBlackTree()

        rb_tree.add(10)
        rb_tree.add(15)
        rb_tree.add(20)
        rb_tree.add(17)

        for i in range(11):
            self.assertEqual(rb_tree.ceil(i), 10)
        for i in range(11, 16):
            self.assertEqual(rb_tree.ceil(i), 15)
        for i in range(16, 18):
            self.assertEqual(rb_tree.ceil(i), 17)
        for i in range(18, 21):
            self.assertEqual(rb_tree.ceil(i), 20)

    def test_floor(self):
        # add all the numbers 0-99 step 2
        # i.e 0, 2, 4
        rb_tree = RedBlackTree()
        for i in range(0, 100, 2):
            rb_tree.add(i)
        # then search for the ceilings, knowing theyre 1 up
        for i in range(1, 99, 2):
            self.assertEqual(rb_tree.floor(i), i - 1)

    def test_floor_same_value(self):
        rb_tree = RedBlackTree()

        rb_tree.add(10)
        rb_tree.add(15)
        rb_tree.add(20)
        rb_tree.add(17)

        for i in range(11, 15):
            self.assertEqual(rb_tree.floor(i), 10)
        for i in range(15, 17):
            self.assertEqual(rb_tree.floor(i), 15)
        for i in range(17, 20):
            self.assertEqual(rb_tree.floor(i), 17)
        for i in range(20, 50):
            self.assertEqual(rb_tree.floor(i), 20)


# These tests take the bulk of the time for testing.
class RbTreePerformanceTests(unittest.TestCase):

    def test_addition_performance(self):
        """
        Add 25,000 elements to the tree
        """
        possible_values = list(range(-100000, 100000))
        elements = [random.choice(possible_values) for _ in range(25000)]
        start_time = datetime.now()
        tree = RedBlackTree()
        for el in elements:
            tree.add(el)
        time_taken = datetime.now()-start_time
        self.assertTrue(time_taken.seconds < 1)

    def test_deletion_performance(self):
        """
        Delete 25,000 elements from the tree
        """
        possible_values = list(range(-100000, 100000))
        elements = set([random.choice(possible_values) for _ in range(25000)])
        # fill up the tree
        tree = RedBlackTree()
        for el in elements:
            tree.add(el)
        start_time = datetime.now()
        for el in elements:
            tree.remove(el)
        time_taken = datetime.now()-start_time
        self.assertTrue(time_taken.seconds < 1)

    def test_deletion_and_addition_performance(self):
        possible_values = list(range(-500000, 500000))
        elements = list(set([random.choice(possible_values)
                             for _ in range(25000)]))
        first_part = elements[:len(elements)//2]
        second_part = elements[len(elements)//2:]
        deletion_part = first_part[len(first_part)//3:(len(first_part)//3)*2]
        tree = RedBlackTree()
        start_time = datetime.now()

        # fill up the tree 1/2
        for el in first_part:
            tree.add(el)
        # delete 1/2 of the tree
        for del_el in deletion_part:
            tree.remove(del_el)
        for el in second_part:
            tree.add(el)

        time_taken = datetime.now()-start_time
        self.assertTrue(time_taken.seconds < 1)


if __name__ == '__main__':
    unittest.main()
