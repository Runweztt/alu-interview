#!/usr/bin/python3
"""Generate Pascal's Triangle."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's Triangle of size n."""
    if n <= 0:
        return []

    triangle = []

    for row_number in range(n):
        row = [1]

        if row_number > 0:
            previous_row = triangle[-1]

            for index in range(1, row_number):
                value = previous_row[index - 1] + previous_row[index]
                row.append(value)

            row.append(1)

        triangle.append(row)

    return triangle
