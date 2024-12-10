"""1291. Sequential Digits

An integer has sequential digits if and only if each digit in the number is one
more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that
have sequential digits.

Constraints:
10 <= low <= high <= 10^9
"""

import math


class XavierSolution:
    """Xavier answer."""

    def sequentialDigits(self, low: int, high: int) -> list[int]:
        result = []
        nums = "123456789"

        left = 0
        right = math.floor(math.log10(low)) + 1
        right_multiplier = 1

        print(f"left: {left}; right: {right}; nums[]: {nums[left: right]}")

        curr: int = int(nums[left:right])
        while curr <= high:
            print(f"left: {left}; right: {right}")

            result.append(curr)

            left += 1
            right += 1

            if right > len(nums):
                left = 0

                right = math.floor(math.log10(low)) + right_multiplier + 1
                right_multiplier += 1

            print(f"LEFT: {left} RIGHT: {right}")

            curr = int(nums[left:right])
            print(curr)

        return result


class SamSolution(object):
    """Sam Wang answer."""

    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        result = []
        starters = [1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789]
        for i in starters:
            if self.length(i) >= self.length(low) and i <= high:
                curr = i
                length = self.length(i)
                while self.length(curr) == length and curr <= high:
                    if curr >= low:
                        result.append(curr)
                    if curr % 10 != 9:
                        curr += int("1" * length)
                    else:
                        break

        return result

    def length(self, n):
        res = 0
        while n >= 1:
            res += 1
            n /= 10
        return res


class LeetcodeSolution:
    """Leetcode answer."""

    def sequentialDigits(self, low: int, high: int) -> list[int]:

        nums = "123456789"
        result = []

        for left in range(len(nums)):
            for right in range(left + 1, len(nums) + 1):
                print(f"left: {left}; right: {right}")

                current = int(nums[left:right])
                print(f"    current: {current}")

                if low <= current <= high:
                    result.append(current)

        print(sorted(result))
        return sorted(result)
