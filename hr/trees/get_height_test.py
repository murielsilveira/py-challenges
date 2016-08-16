from unittest import TestCase
from node import Node
from get_height import getHeight


class GetHeightTests(TestCase):
    
    def test_empty_tree(self):
        self.assertEqual(-1, getHeight(None))

    def test_tree_with_a_single_node_has_height_zero(self):
        '''
            11
          /    \
        None  None
        '''
        self.assertEqual(0, getHeight(Node(11)))

    def test_tree_with_two_node_has_height_one(self):
        '''
             11            11
            /  \          /  \
           10  None     None  12
          /  \               /  \
        None None          None None
        '''
        self.assertEqual(1, getHeight(Node(11, left=Node(10))))
        self.assertEqual(1, getHeight(Node(11, right=Node(12))))

    def test_tree_with_height_two(self):
        '''
                11
             /      \
            9        12
           / \       / \
        None 10   None None
            /  \
          None None
        '''
        tree = Node(
            11,
            Node(
                9,
                right=Node(10)
            ),
            Node(12)
        )
        self.assertEqual(2, getHeight(tree))

    def test_tree_with_height_five(self):
        '''
                      10
                      / \
                     9  None
                    / \
                   8  None
                  / \
                 7  None
                / \
               6  None
             /  \
            5   None
           / \
        None None
        '''
        tree = Node(10, Node(9, Node(8, Node(7, Node(6, Node(5))))))
        self.assertEqual(5, getHeight(tree))
