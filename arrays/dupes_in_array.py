"""Check if array has duplicates."""

from typing import Set


def main():
    no_dupe: list(str) = ["amzn", "msft", "goog", "eth",
                          "doge", "soxl", "v"]
    dupes_first: list(str) = ["amzn", "amzn", "msft"]
    dupes_second: list(str) = ["msft", "msft", "msft", "msft"]
    assert check_dupes(no_dupe) is False, "ERROR: Dupes found"
    assert check_dupes(dupes_first) is True, "ERROR: No Dupes found"
    assert check_dupes(dupes_second) is True, "ERROR: No Dupes found"

    print("Use the more effecient Set function.")
    assert use_set_check_dupes(no_dupe) is False, "ERROR: Dupes found"
    assert use_set_check_dupes(dupes_first) is True, "ERROR: No Dupes found"
    assert use_set_check_dupes(dupes_second) is True, "ERROR: No Dupes found"


def check_dupes(stocks: list) -> bool:
    """Return True if at least one duplicate is found in list.

    Args:
        a: List of stocks as a string.

    Returns: 
        True if one or more string is the same.
    """
    if len(stocks) < 1:
        return True

    past: list(str) = []
    for stock in stocks:
        if stock in past:
            return True
        past.append(stock)
        print("Adding to past: ", stock)
    return False


def use_set_check_dupes(stocks: list) -> bool:
    """Same as check_dupes but with set function.

    Alternatively use Python set since sets do not allow
    duplicates.  Sets are unordered which is similar to 
    using a list in previous function. 

    Sets are significantly faster when checking if an element is present. 

    Lists are significantly faster when you want to only iterate 
    through values (See https://stackoverflow.com/a/17945009/8278075 for experiment). 

    Sets can also be combined with lists with `myset.update([...])`.

    Notes that once a set is create, you cannot modify 
    except add items.  If you `.add()` a duplicate item, the set 
    will not change. 
    https://www.w3schools.com/python/python_sets.asp
    """
    if len(stocks) < 1:
        return True

    past: Set(str) = set()
    for stock in stocks:
        if stock in past:
            return True
        past.add(stock)
        print("Adding to past: ", stock)
    return False


if __name__ == "__main__":
    main()
