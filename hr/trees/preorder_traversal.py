
class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def preOrder(root):
    answer = []
    def pre_order(root):
        if root is None:
            return
        answer.append(root.data)
        pre_order(root.left)
        pre_order(root.right)
    pre_order(root)
    return answer
