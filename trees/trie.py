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
    def __init__(self):
        # Initialize the root as an empty dictionary
        self.root = {}
        # Special character to mark the end of a word
        self.end_symbol = '*'

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        # Mark the end of a word
        node[self.end_symbol] = True

    def search(self, word: str) -> bool:
        """
        Returns True if the word is in the trie, otherwise False.
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        # Check if the word is marked as complete
        return self.end_symbol in node

    def starts_with(self, prefix: str) -> bool:
        """
        Returns True if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True


# Example usage
if __name__ == "__main__":
    trie = Trie()

    # Insert words
    words = ["apple", "app", "approach", "boy", "book"]
    for word in words:
        trie.insert(word)

    # Search for words
    print(f"Search 'apple': {trie.search('apple')}")        # True
    print(f"Search 'app': {trie.search('app')}")            # True
    print(f"Search 'apples': {trie.search('apples')}")      # False
    print(f"Search 'boy': {trie.search('boy')}")            # True
    print(f"Search 'alphabet': {trie.search('alphabet')}")  # False

    # Check prefixes
    print(f"Prefix 'app': {trie.starts_with('app')}")       # True
    print(f"Prefix 'bo': {trie.starts_with('bo')}")         # True
    print(f"Prefix 'bat': {trie.starts_with('bat')}")       # False

