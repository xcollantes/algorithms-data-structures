"""Run-length encoding (RLE) is a string compression method that works by
replacing consecutive identical characters (repeated 2 or more times) with the
concatenation of the character and the number marking the count of the
characters (length of the run). 

For example, to compress the string "3322251" we
replace "33" with "23", replace "222" with "32", replace "5" with "15" and
replace "1" with "11". Thus the compressed string becomes "23321511". 

Given a positive integer n, return the nth element of the count-and-say
sequence.
"""


def countAndSay(n: int) -> str:
    curr_n: int = 0
    while curr_n <= n:
        pass
        # Find string

        # Append to larger string

        # Increment

def compress(s: str) -> str:
    if len(s) <= 1:
        return "1" + s
    
    # 3322251
    # count: 1
    #
    # 5
    # 2332
    
    
    result: str = ""
    count: int = 1
    for i in range(1, len(s)):
        print(f"s[i]: {s[i]}; count: {count} result: {result}")

        if s[i] == s[i - 1]:
            count += 1
        else:
            result += str(count) + s[i - 1]
            count = 1

    return result



# def countAndSay(self, n: int) -> str:
#     if n == 1:
#         return "1"
#     x = self.countAndSay(n - 1)
#     s = ""
#     y = x[0]
#     ct = 1
#     for i in range(1, len(x)):
#         if x[i] == y:
#             ct += 1
#         else:
#             s += str(ct)
#             s += str(y)
#             y = x[i]
#             ct = 1
#     s += str(ct)
#     s += str(y)
#     return s
