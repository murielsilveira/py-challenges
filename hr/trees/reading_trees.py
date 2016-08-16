
class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def preOrder(root):
    def pre_order(root):
        if root is None:
            return
        answer.append(root.data)
        pre_order(root.left)
        pre_order(root.right)

    answer = []
    pre_order(root)
    return answer


def postOrder(root):
    def post_order(root):
        if root is None:
            return
        post_order(root.left)
        post_order(root.right)
        answer.append(root.data)

    answer = []
    post_order(root)
    return answer
