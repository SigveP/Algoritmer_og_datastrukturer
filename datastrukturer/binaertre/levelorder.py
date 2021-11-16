from ..maler.nodes import TreeNode
from ..queue import Queue


def iterative(node: TreeNode) -> list:
    if node == None:
        return []

    result = []
    q = Queue()
    q.enqueue(node)

    while len(q) != 0:
        node = q.dequeue()
        if node.left:
            q.enqueue(node.left)
        if node.right:
            q.enqueue(node.right)

        result.append(node.value)

    return result


def recursive(node: TreeNode, layer: int) -> list:
    def func(node: TreeNode, layer: int) -> list:
        try:
            resultdict[layer].append(node.value)
        except KeyError:
            resultdict[layer] = [node.value]
        if node.left:
            func(node.left, layer + 1)
        if node.right:
            func(node.right, layer + 1)

    resultdict = {}
    func(node, layer)
    result = []
    for k, v in resultdict.items():
        for i in v:
            result.append(i)
    return result
