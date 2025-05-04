"""A trie is a tree-like data structure that stores a dynamic set of strings.

Tries are used to represent a dictionary. Each node in the trie represents a single
character of a string. The path from the root to a particular node forms a prefix
of one or more strings in the dictionary.

Example:

Input:
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    trie.insert("approach")

    trie.search("apple")    # returns True
    trie.search("app")      # returns True
    trie.search("apples")   # returns False

    trie.starts_with("app") # returns True (matches "apple", "app", "approach")
    trie.starts_with("bat") # returns False
"""


class Trie:

    def __init__(self) -> None:
        self.root = {}
        self.ending_char = "#"

    def insert(self, word: str) -> None:
        cur = self.root

        for letter in word:
            if not letter in cur:
                cur[letter] = {}

            cur = cur[letter]

        cur["#"] = word

    def search(self, word: str) -> bool:
        cur = self.root
        for letter in word + "#":
            print(f"letter: {letter} cur: {cur}")

            if not letter in cur:
                print(f"NOT FOUND: {letter} in {word}")
                return False

            if cur.get("#") == word:
                return True

            cur = cur[letter]

        return False

    def starts_with(self, s: str) -> bool:
        cur = self.root
        for letter in s:

            if not letter in cur:
                return False

            cur = cur[letter]

        return True


import pytest


@pytest.fixture
def setup_trie():
    """Setup function that creates and returns a Trie with test data."""
    trie = Trie()
    words = ["apple", "app", "approach", "boy", "book"]
    for word in words:
        trie.insert(word)
    return trie


def test_search(setup_trie):
    """pytest trie.py."""
    trie = setup_trie

    assert trie.search("apple") == True
    assert trie.search("app") == True
    assert trie.search("apples") == False
    assert trie.search("boy") == True
    assert trie.search("alphabet") == False


def test_starts_with(setup_trie):
    """pytest trie.py."""
    trie = setup_trie

    assert trie.starts_with("app") == True
    assert trie.starts_with("bo") == True
    assert trie.starts_with("bat") == False


if __name__ == "__main__":
    trie = Trie()

    # Insert words
    words: list[str] = ["apple", "app", "approach", "boy", "book"]
    for word in words:
        trie.insert(word)

    # Search for words
    print(f"Search 'apple': {trie.search('apple')}")  # True
    print(f"Search 'app': {trie.search('app')}")  # True
    print(f"Search 'apples': {trie.search('apples')}")  # False
    print(f"Search 'boy': {trie.search('boy')}")  # True
    print(f"Search 'alphabet': {trie.search('alphabet')}")  # False

    # Check prefixes
    print(f"Prefix 'app': {trie.starts_with('app')}")  # True
    print(f"Prefix 'bo': {trie.starts_with('bo')}")  # True
    print(f"Prefix 'bat': {trie.starts_with('bat')}")  # False

    # Search for words
    print(f"Search 'apple': {trie.search('apple')}")  # True
    print(f"Search 'app': {trie.search('app')}")  # True
    print(f"Search 'apples': {trie.search('apples')}")  # False
    print(f"Search 'boy': {trie.search('boy')}")  # True
    print(f"Search 'alphabet': {trie.search('alphabet')}")  # False

    # Check prefixes
    print(f"Prefix 'app': {trie.starts_with('app')}")  # True
    print(f"Prefix 'bo': {trie.starts_with('bo')}")  # True
    print(f"Prefix 'bat': {trie.starts_with('bat')}")  # False
