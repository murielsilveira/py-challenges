def getHeight(root):
    if root is None:
        return -1

    left_height = getHeight(root.left)
    right_height = getHeight(root.right)

    if left_height > right_height:
        return left_height + 1
    else:
        return right_height + 1
