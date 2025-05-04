import json

words: list[str] = ["apple", "app", "approach", "boy", "book"]

trie = {}
for word in words:
    print(f"Adding {word} to {trie}")

    cur = trie  # Move cur to head for every word.
    for letter in word:
        # Option 1: Use the setdefault.
        # cur = cur.setdefault(letter, {})

        # Option 2: Manually add the trie.
        if not letter in cur:
            # If letter not in current level of dict, start new level.
            # When the letters diverge for a word, a new dictionary entry is
            # created.
            cur[letter] = {}

        # Iterate to the next level if continuing or if new level.
        cur = cur[letter]

    # Stop char.
    # The end character is a key to easily return the full word set as value.
    cur["#"] = word


# {
#     "a": {
#         "p": {
#             "p": {
#                 "l": {
#                     "e": {
#                         "#": "apple"
#                     }
#                 },
#                 "#": "app",
#                 "r": {
#                     "o": {
#                         "a": {
#                             "c": {
#                                 "h": {
#                                     "#": "approach"
#                                 }
#                             }
#                         }
#                     }
#                 }
#             }
#         }
#     },
#     "b": {
#         "o": {
#             "y": {
#                 "#": "boy"
#             },
#             "o": {
#                 "k": {
#                     "#": "book"
#                 }
#             }
#         }
#     }
# }

print(json.dumps(trie, indent=4))


def test_trie():
    assert trie == {
        "a": {
            "p": {
                "p": {
                    "l": {"e": {"#": "apple"}},
                    "#": "app",
                    "r": {"o": {"a": {"c": {"h": {"#": "approach"}}}}},
                }
            }
        },
        "b": {"o": {"y": {"#": "boy"}, "o": {"k": {"#": "book"}}}},
    }
