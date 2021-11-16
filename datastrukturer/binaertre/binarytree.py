from ..maler import TreeNode as Node


class BinaryTree:
    def __init__(self, *values) -> None:
        self.root = None

        for value in values:
            self.append(value)

    def append(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._append(value, self.root)

    def _append(self, value, node: Node):
        if value <= node.value:
            if node.left:
                self._append(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self._append(value, node.right)
            else:
                node.right = Node(value)

    def getDict(self, node: Node) -> dict:
        t = {node.value: []}
        if node.left:
            t[node.value].append(self.getDict(node.left))
        if node.right:
            t[node.value].append(self.getDict(node.right))
        return t
