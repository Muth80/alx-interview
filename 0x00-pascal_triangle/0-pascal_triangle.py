#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)

    return triangle

# Test your function
if __name__ == "__main__":
    triangle = pascal_triangle(5)
    for row in triangle:
        print(row)

