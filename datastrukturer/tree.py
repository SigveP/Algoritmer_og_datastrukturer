class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.branches = []

    def branch(self, value) -> None:
        self.branches.append(Node(value))


class Tree:
    def __init__(self, value) -> None:
        self.root = Node(value)  # hoved-node

    def add(self, branch: Node, value) -> None:
        branch.branch(value)

    def _getDict(self, node, values: dict) -> dict:
        new_values = []
        for branch in node.branches:
            new_values.append(self._get(branch, {}))
        values[str(node.value)] = new_values
        return values

    def getDict(self) -> dict:
        return self._get(self.root, {})
