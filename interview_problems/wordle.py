"""Wordle interview question.

5 letter word in English where player has 6 tries.  Player gets clues when they 
attempt to guess the word.

Cases:
    Yellow: letter in word but wrong position 
    Grey: letter not in word 
    Green: letter in word and in correct position 

Words will be in a TXT file.  The output will be in G for green,
Y for yellow, and R for grey representing the colors.  
So if FOCUS is the answer word and player guesses SALTS, then 
function would return YRRRG.  

How to deal with repeated letters? 

"""

from collections import defaultdict


def main():
    assert get_letter("PRIZE", "PRZIM") == "GGYYR"
    assert get_letter("SALTS", "FOCUS") == "RRRRG"
    # assert get_letter("PRICE", "MICRO") == "RYYYR"


def get_letter(guess: str, answer: str) -> str:
    """Wordle function.

    Args:
        guess (str): Player's guess word.

    Returns:
        str: Combination of GRY. 
    """
    G: list = list(guess)
    A: list = list(answer)

    A_set: dict = defaultdict(int)
    for i in A:
        A_set[i] += 1

    r = wordle(G, A, A_set)
    print(r)
    return r


def wordle(G: list, A: list, A_set: dict):
    """Wordle.

    Returns:
        str
    """
    if not G or len(G) != len(A):
        return None

    result: str = ""
    for index in range(len(G)):

        if G[index] == A[index]:
            result += "G"

            # Remove instance of letter
            A_set[G[index]] -= 1

        elif A_set[G[index]] >= 1:
            result += "Y"

            # Remove instance of letter
            A_set[G[index]] -= 1

        else:
            result += "R"

    return result


if __name__ == "__main__":
    main()
