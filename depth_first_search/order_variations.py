from typing import Any


class Node():
    def __init__(self, data) -> None:
        self.payload: Any = data
        self.left: Node = None
        self.right: Node = None


def run_orders() -> None:
    root_tree = Node(10)
    root_tree.left = Node(5)
    root_tree.right = Node(11)

    print("PRE")
    pre_order(root_tree)

    print("IN")
    in_order(root_tree)

    print("POST")
    post_order(root_tree)


def pre_order(current_node: Node):
    if not current_node:
        return

    print(current_node.payload)
    pre_order(current_node.left)
    pre_order(current_node.right)


def in_order(current_node: Node):
    if not current_node:
        return

    in_order(current_node.left)
    print(current_node.payload)
    in_order(current_node.right)


def post_order(current_node: Node):
    if not current_node:
        return

    post_order(current_node.left)
    post_order(current_node.right)
    print(current_node.payload)


if __name__ == "__main__":
    run_orders()
