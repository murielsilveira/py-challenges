from unittest import TestCase
from reading_trees import Node, preOrder, postOrder


class ReadingTreesTests(TestCase):
    def setUp(self):
        '''
              3
           /    \
          5      2
         / \    /
        1   4  6
        '''
        self.data = Node(
            3,
            Node(
                5,
                Node(1),
                Node(4)
            ),
            Node(
                2,
                Node(6)
            )
        )

    def test_returns_an_array_with_the_values_in_pre_order(self):
        self.assertEqual([3, 5, 1, 4, 2, 6], preOrder(self.data))

    def test_returns_an_array_with_the_values_in_post_order(self):
        self.assertEqual([1, 4, 5, 6, 2, 3], postOrder(self.data))
