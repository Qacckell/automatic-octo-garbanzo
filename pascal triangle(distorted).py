def generate_pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        triangle.append(row)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
    # aligning each row to center of the triangle
    for i in range(n):
        spaces = " " * (n-i-1)
        triangle[i] = spaces + " ".join(map(str, triangle[i]))
    return triangle

n = int(input("Enter the number of rows for Pascal's triangle: "))
triangle = generate_pascal_triangle(n)
for row in triangle:
    print(row)
