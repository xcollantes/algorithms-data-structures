"""735. Asteroid Collision

Medium

We are given an array asteroids of integers representing asteroids in a row. The
indices of the asteroid in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign
represents its direction (positive meaning right, negative meaning left). Each
asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet,
the smaller one will explode. If both are the same size, both will explode. Two
asteroids moving in the same direction will never meet.


Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.


Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.


Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.


Constraints:

2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
"""


def test_asteroids():
    """pytest asteroids.py"""
    assert asteroids([5, 10, -5]) == [5, 10]
    assert asteroids([8, -8]) == []
    assert asteroids([10, 2, -5]) == [10]


def asteroids(asteroids: list[int]) -> list[int]:
    """
    Simulate asteroid collisions using a stack.

    Algorithm:
    - Right-moving asteroids (positive) are always added to stack
    - Left-moving asteroids (negative) may collide with right-moving ones
    - Collision rules: smaller explodes, equal size both explode
    """
    stack = []

    for a in asteroids:

        # if pos
        if a > 0:

            # Right-moving asteroid, always add to stack
            stack.append(a)

        # if negative
        else:

            # Left-moving asteroid, check for collisions
            while stack and stack[-1] > 0 and stack[-1] < abs(a):

                # Right-moving asteroid is smaller, it explodes
                stack.pop()


            if stack and stack[-1] > 0 and stack[-1] == abs(a):

                # Equal size, both explode
                stack.pop()

            elif not stack or stack[-1] < 0:
                # No collision (empty stack or both moving left)

                stack.append(a)

            # If stack[-1] > abs(asteroid), left-moving asteroid explodes (do nothing)

    return stack
