"""
You are given an array of logs. Each log is a space-delimited string of words,
where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English
letters.  Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

The letter-logs come before all digit-logs.  The letter-logs are sorted
lexicographically by their contents. If their contents are the same, then sort
them lexicographically by their identifiers.  The digit-logs maintain their
relative ordering.  Return the final order of the logs.
"""

import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")


# def reorder_logs(logs: list[str]) -> list[str]:

#     # Split the labels
#     # Put digi first
#     # With letter:
#     #   sort with content

#     digi_logs = []
#     letter_logs = []
#     for log in logs:
#         if log[-1].isnumeric():
#             digi_logs.push(log)
#         else:
#             label, content = log.split(" ", 1)
#             letter_logs.push((label, content))

#     finished = 0
#     while finished < len(letter_logs):
#         for idx in range(len(letter_logs) - 1):
#             if letter_logs[idx][1] > letter_logs[idx + 1][1]:
#                 letter_logs[idx], letter_logs[idx + 1] = (
#                     letter_logs[idx + 1],
#                     letter_logs[idx],
#                 )
#         if letter_logs[idx][1] == letter_logs[idx + 1][1]:
#
# return letter_logs + digi_logs


def custom_sort(log: str) -> tuple:
    if log[-1].isnumeric():
        # No need to specify other elements since we leave digital labeled
        # alone.
        return (1,)
    label, content = log.split(" ", 1)
    # Since we want to order by the non-label content then label if content is
    # the same.
    return (0, content, label)


def reorder_optimal(logs: list[str]) -> list[str]:
    return sorted(logs, key=custom_sort)  # key= creates an ID to sort by.
