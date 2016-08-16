from unittest import TestCase
from reading_trees import Node, preOrder


class PreOrderTests(TestCase):

    def test_return_a_array_with_the_values_in_pre_order(self):
        '''
              3
           /    \
          5      2
         / \    /
        1   4  6
        '''
        data = Node(
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

        self.assertEqual([3, 5, 1, 4, 2, 6], preOrder(data))
