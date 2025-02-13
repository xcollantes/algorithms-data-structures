"""Snapchat interview for Solutions Engineer on Feb 12,2025.

Employee ID, Manager ID, Employee Name
8, 8, "Alice"
2, 8, "Bob"
3, 2, "Emp3"
4, 3, "Emp4"
5, 4, "Emp5"
6, 3, "Emp6"
7, 8, "Emp7"


Output:
Alice
  Bob
    Emp3
      Emp4
        Emp5
      Emp6
  Emp7
"""

from io import StringIO
import sys
import textwrap
import unittest

from leetcode_questions.easy.strings_arrays.employee_print import employee_print


class TestEmployeePrint(unittest.TestCase):
    def test_employee_print(self):
        """Test prints."""
        captured_output = StringIO()
        sys.stdout = captured_output
        employee_print(
            [
                (2, 8, "Bob"),
                (8, 8, "Alice"),
                (3, 2, "Emp3"),
                (4, 3, "Emp4"),
                (5, 4, "Emp5"),
                (6, 3, "Emp6"),
                (7, 8, "Emp7"),
            ]
        )
        sys.stdout = sys.__stdout__

        expected_print = """
          Alice
            Bob
              Emp3
                Emp4
                  Emp5
                Emp6
            Emp7
        """

        self.assertEqual(
            textwrap.dedent(captured_output.getvalue()),
            textwrap.dedent(expected_print),
        )
