#!/usr/bin/python3

"""
A function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

"""
def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row
    for _ in range(1, n):  # Iterate for the remaining rows
        prev_row = triangle[-1]  # Get the previous row
        row = [1] + [left + right for left, right in zip(prev_row, prev_row[1:])] + [1]
        triangle.append(row)

    return triangle

