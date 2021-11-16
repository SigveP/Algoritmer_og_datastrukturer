from ..maler.nodes import TreeNode
from ..stack import Stack


def iterative(node: TreeNode) -> list:
    result = []
    s = Stack()
    s.append(node)
    while len(s) != 0:
        node = s.pop()
        if isinstance(node, int):
            result.append(node)
            continue
        s.append(node.value)
        if node.right:
            s.append(node.right)
        if node.left:
            s.append(node.left)

    return result


def recursive(node: TreeNode) -> list:
    result = []
    if node.left:
        for i in recursive(node.left):
            result.append(i)
    if node.right:
        for i in recursive(node.right):
            result.append(i)
    result.append(node.value)
    return result
