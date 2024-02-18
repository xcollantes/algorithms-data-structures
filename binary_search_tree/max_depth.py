"""Find max depth of tree."""


class Node:
    def __init__(self, data) -> None:
        self.data: any = data
        self.left: Node = None
        self.right: Node = None


def main():
    root: Node = build_tree([2, 1, 88, 3, 12, 11, 4, 8])
    print("Max depth of tree is: ", max_depth(root))


def max_depth(root: Node) -> int:
    """Find longest path in tree."""
    return _max_depth(root)


def _max_depth(current_node: Node) -> int:
    """Recursively travel tree and return longest path."""
    if current_node:
        print("CUR NODE: ", current_node.data)

    if current_node is None:
        return 0
    else:
        left_return: int = _max_depth(current_node.left)
        right_return: int = _max_depth(current_node.right)
        print(f"LEFT return: {left_return}  RIGHT return: {right_return}")

        return max(left_return, right_return) + 1


def build_tree(values: list[int]) -> Node:
    """Build tree and return root node of entire tree."""
    root: Node = Node(values[0])
    for value in values[1:]:
        _add_node(root, value)
    return root


def _add_node(node: Node, value: int) -> Node:
    """Recursively build tree."""
    print("currently on node: ", node.data)
    if value < node.data:
        if node.left:
            _add_node(node.left, value)
        else:
            print("left inserted ", value)
            node.left = Node(value)
    else:
        if node.right:
            _add_node(node.right, value)
        else:
            print("right inserted ", value)
            node.right = Node(value)


if __name__ == "__main__":
    main()
