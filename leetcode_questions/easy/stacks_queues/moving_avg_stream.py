"""
Given a stream of integers and a window size, calculate the moving average of
all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the
stream.
"""

from collections import deque


class MovingAvg:
    def __init__(self, size: int) -> None:
        self.size = size
        self.length = 0
        self.queue = deque()
        self.sum = 0

    def next(self, val: int) -> float:
        self.queue.append(val)

        if self.length < self.size:
            self.length += 1
        else:
            self.sum -= self.queue.popleft()

        self.sum += val

        return self.sum / self.length
