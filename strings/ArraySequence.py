"""Array Sequence Practice."""

import copy
import random


def main():
    print(
        "Anagram Check, Solution 1: %s"
        % AnagramCheck("clint eastwood", "old west action")
    )
    print(
        "Anagram Check, Solution 2: %s"
        % AnagramCheck2("clint eastwood", "old west action")
    )
    print("Array Pairs, Solution 1: %s" % ArrayPair([1, 3, 2, 2], 4))

    find_list = [1, 2, 3, 4, 5, 6, 7, 7, 7, 8, 9]
    shuffle = copy.deepcopy(find_list)
    random.shuffle(shuffle)
    shuffle = shuffle[1:]
    print("FinderBest: %s" % FinderBest(find_list, shuffle))
    print(find_list)
    print(shuffle)

    print("Sentence reversal: %s" % SentReverse("There is no try only do or do not.  "))


def Finder(list, shuffled_list):
    """Find the missing element in shuffled_list.

    Time complexity is O(n^2).
    Given two lists, the second a shuffled version of first, return
    the element missing in shuffled_list.

    list: Ordered list of non-negative numbers.
    shuffled_list: Randomized version of list with one element missing.

    Returns: The missing element not in shuffled_list but present
    in list.
    """
    if len(list) == len(shuffled_list) - 1:
        return "Error"

    for e in list:
        if e not in shuffled_list:
            return e


def FinderBest(list, list_shuffle):
    """Same as Finder but more efficient time complexity O(n).

    We iterate through each list once.
    """

    if len(list) == len(list_shuffle) - 1:
        return "Error"

    count = {}
    for e in list_shuffle:
        print("e ", e, count)
        if e in count:
            count[e] += 1
        else:
            count[e] = 1

    for s in list:
        print("s ", s, count)
        if s in count:
            count[s] -= 1
        else:
            return s

        if count[s] == 0:
            count.pop(s)


def SentReverse(sentence):
    """Reverse the words in a sentence.

    sentence: String in forward order.

    Returns: String sentence with reverse order words.
    """
    sentence = sentence.strip()
    sentence = sentence.split(" ")
    length = len(sentence)

    out = ""
    for word in sentence:
        out = word + " " + out
        print(out)

    return out


def ArrayPair(arr, sum):
    """Find the pairs in given array that sum up to the given sum."""
    eval = []
    for col in arr:
        for row in arr:
            if ((col + row) == sum) and ([col, row] not in eval):
                eval.append([col, row])

    return eval


def AnagramCheck(x, y):
    """Anagram Check:  Check to see if both inputs are anagrams of each other.
    Solution 1: Sort strings then compare since both should have the same
    number of letters.
    """
    x = x.replace(" ", "").lower()
    y = y.replace(" ", "").lower()

    return sorted(x) == sorted(y)


def AnagramCheck2(x, y):
    """Solution 2: Verify two inputs are anagrams."""
    x = x.replace(" ", "").lower()
    y = y.replace(" ", "").lower()

    if len(x) is not len(y):
        return False

    countDict = {}
    for a in x:  #  Loop first word
        if a in countDict:
            countDict[a] = countDict[a] + 1
        else:
            countDict[a] = 1

    print(countDict)

    for b in y:
        if b in countDict:
            countDict[b] = countDict[b] - 1
        else:
            return False

        if countDict[b] == 0:
            countDict.pop(b)
        if len(countDict) == 0:
            return True
        # print(countDict)
        # print(len(countDict))


if __name__ == "__main__":
    main()
