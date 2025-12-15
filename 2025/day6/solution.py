with open('input.txt', 'r') as f:
    matrix = [line.strip().split() for line in f]
    print(matrix)

rows = len(matrix)
cols = len(matrix[0])
total = []

for col in range(cols):
    column = [row[col] for row in matrix]
    operator = column[-1]
    numbers = [int(x) for x in column[:-1]]
    result = 1 if operator == '*' else 0

    if operator == '*':
        for val in numbers:
            result = result * val

    elif operator == '+':
        for val in numbers:
            result = result + val

    total.append(result)
    print(f"{numbers} {operator} = {result}")
print(f"Total = {sum(total)}")
