def employee_print(employees: list[tuple[int, int, str]]):
    top: tuple[int, int, str] = None
    name_dict: dict[int, str] = {}
    relation_dict: dict[int, list[int]] = {}

    # Build the dictionaries
    for emp_id, man_id, name in employees:
        if emp_id == man_id:
            top = (emp_id, man_id, name)

        # Build manager to employees relationship
        if man_id in relation_dict:
            relation_dict[man_id].append(emp_id)
        else:
            relation_dict[man_id] = [emp_id]

        # Build employee ID to name mapping
        name_dict[emp_id] = name

    def print_hierarchy(emp_id: int, depth: int = 0):
        # Print current employee
        print("  " * depth + name_dict[emp_id])

        # Process subordinates if they exist
        if emp_id in relation_dict:
            for subordinate_id in relation_dict[emp_id]:
                print_hierarchy(subordinate_id, depth + 1)

    # Start from the top of the hierarchy
    print_hierarchy(top[0])

# Test the function
employee_print([
    (8, 8, "Alice"),
    (2, 8, "Bob"),
    (3, 2, "Emp3"),
    (4, 3, "Emp4"),
    (5, 4, "Emp5"),
    (6, 3, "Emp6"),
    (7, 8, "Emp7")
])