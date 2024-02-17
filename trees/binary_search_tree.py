from typing import Any
import random
from data_structures.tree import BinaryTree


def main():
    # n: list(int) = [random.randint(0, 20) for _ in range(10)]
    # print("Random range: ", n)

    o = [25, 2, 55, 0, 1, 30, 75]
    r = [1, 2, 4, 5, 3]
    print(o)

    b = BinaryTree()
    for i in r:
        b.insert(i)

    print("\nPRE ORDER ****")
    b.preorder()

    print("\nIN ORDER ****")
    b.inorder()


if __name__ == "__main__":
    main()
