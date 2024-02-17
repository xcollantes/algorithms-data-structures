"""Measure time taken by an algorithm independent of machine."""

import timeit
import inspect


class Stopwatch:
    def __init__(self, function_to_measure) -> None:
        self.function_to_measure = inspect.getsource(function_to_measure)
        self.function_to_measure += f"\n\n{function_to_measure.__name__}()"
        # self.variables = inspect.getsource(variables)
        self.results = None

    def run(self) -> None:
        self.results = timeit.timeit(
            stmt=self.function_to_measure)
        # Returns seconds as a float

    def print_results(self) -> None:
        print(f"TEST RESULTS: {self.results}")
