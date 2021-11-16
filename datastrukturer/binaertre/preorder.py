from ..maler.nodes import TreeNode
from ..stack import Stack


def iterative(node: TreeNode) -> list:
    result = []
    s = Stack()
    s.append(node)

    while len(s) != 0:
        node = s.pop()
        if node.right:
            s.append(node.right)
        if node.left:
            s.append(node.left)
        result.append(node.value)

    return result


def recursive(node: TreeNode) -> list:
    result = [node.value]
    if node.left:
        for i in recursive(node.left):
            result.append(i)
    if node.right:
        for i in recursive(node.right):
            result.append(i)
    return result
