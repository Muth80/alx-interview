#!/usr/bin/python3

"""
A function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

"""
def pascal_triangle(n):
    """
    Generate Pascal's triangle of height n as a list of lists.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            # Each element is the sum of the two elements above it
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle

# Function to print the triangle (provided in the task description)
def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

# Main block for testing
if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
