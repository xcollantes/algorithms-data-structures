from typing import Any


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def youknowthething(self, current_node: Node):
        print("LEFT: ", current_node.left, " | CURRENT: ",  current_node.value,
              " | RIGHT: ", current_node.right)


    def insert(self, value):
        self._insert_node(self.root, value)

    def _insert_node(self, current_node, value):
        print("starting insert: ", value)
        if self.root is None:
            self.root = Node(value)
        else:
            if value <= current_node.value:
                if current_node.left is None:
                    current_node.left = Node(value)
                else:
                    return self._insert_node(current_node.left, value)
            else:
                if current_node.right is None:
                    current_node.right = Node(value)
                else:
                    return self._insert_node(current_node.right, value)

        return

    def preorder(self):
        self._preorder_traverse(self.root)

    def _preorder_traverse(self, current_node):
        self.youknowthething(current_node)
        if current_node.left:
            self._preorder_traverse(current_node.left)
        if current_node.right:
            self._preorder_traverse(current_node.right)
        if current_node.left is None and current_node.right is None:
            print("leaf node")

    def inorder(self):
        self._inorder_traverse(self.root)

    def _inorder_traverse(self, current_node: Node):
        if current_node.left:
            self._preorder_traverse(current_node.left)

        self.youknowthething(current_node)

        if current_node.right:
            self._preorder_traverse(current_node.right)

        if current_node.left is None and current_node.right is None:
            print("leaf node")

    def postorder(self):
        pass
