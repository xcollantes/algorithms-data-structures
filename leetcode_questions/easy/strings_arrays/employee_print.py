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


def employee_print(employees: list[tuple[int, int, str]]):
    top: tuple[int, int, str] = None

    name_dict: dict[int, str] = {}
    relation_dict: dict[int, list[int]] = {}

    for emp_id, man_id, name in employees:
        # Find starting point for parsing or top of hierarchy.
        if emp_id == man_id:
            top = (emp_id, man_id, name)

        # Relate manager to subordinates.

        # NOTE: Doesn't work since appending to array is in-place, returns None.
        #
        # `.append(emp_id)` returns None.
        # relations_dict[man_id] = relation_dict.get(man_id, None).append(emp_id)

        if man_id in relation_dict:
            # This is what I was trying to do earlier today with David.
            relation_dict[man_id].append(emp_id)
        else:
            relation_dict[man_id] = [emp_id]

        # Create emp ID to emp Name dict.
        name_dict[emp_id] = name

    print(f"Relation: {relation_dict}")
    print(f"ID-name: {name_dict}")

    def rec(emp_id: int, padding: int) -> None:
        """Recurse over the employees."""
        # print(f"rec: {emp_id}")

        # Traditional basecase doesn't work here.
        # if len(emp_ids) <= 0:
        #     return

        print(" " * padding, end="")
        print(f"{name_dict[emp_id]}")

        # If emp_id has subordinates.
        # If emp_id has no subordinates: Nothing since they already printed out.
        if emp_id in relation_dict:

            for e in relation_dict[emp_id]:

                # Case: Emp ID and Manager ID are the same.
                # From what I recall David said only one case of this: the top CEO
                # (Alice).
                # If unhandled, this will result in infinite loop.
                if emp_id != e:
                    rec(e, padding + 2)

    # Iterate over manager-employee hashmap.
    # for man_id, emp_ids in relation_dict.items():
    rec(top[1], 0)


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
