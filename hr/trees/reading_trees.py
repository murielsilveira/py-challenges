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


def inOrder(root):
    def in_order(root):
        if root is None:
            return
        in_order(root.left)
        answer.append(root.data)
        in_order(root.right)

    answer = []
    in_order(root)
    return answer
