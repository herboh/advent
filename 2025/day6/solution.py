def load_data(path):
    with open(path) as f:
        lines = [line.replace('\n', '') for line in f]

    cols = list(zip(*lines))
    return lines, cols

def solve_cephalopod(cols):
    equation = []
    operator = None

    for col in cols:
        # stop at fully blank column
        if all(ch == ' ' for ch in col):
            if equation and operator:
                yield equation, operator
            equation = []
            operator = None
            continue

        if col[-1] != ' ':
            operator = col[-1]

        col_string = ''.join(col[:-1]).strip()
        nums = [int(n) for n in col_string.split()]
        equation.append(nums)

    if equation and operator:
        yield equation, operator

def solve_normal(lines):
    matrix = [line.split() for line in lines if line.strip()]
    cols = len(matrix[0]) if matrix else 0

    for col_idx in range(cols):
        column = [matrix[row][col_idx] for row in range(len(matrix))]
        operator = column[-1]
        if operator not in ['+', '*']:
            continue
        nums = [[int(x)] for x in column[:-1]]
        if nums:
            yield nums, operator

def calculate(equation, operator):
    nums = [n for group in equation for n in group]

    if operator == '*':
        result = 1
        for n in nums:
            result *= n
        return result
    elif operator == '+':
        return sum(nums)
    else:
        print(f"WARNING: Unknown operator '{operator}' in equation {equation}")
        return 0

def main() -> None:
    lines, cols = load_data("input.txt")
    solvers = [("Part 1: NORMAL (Row-wise)", "Row", solve_normal(lines)),
        ("Part 2: CEPHALOPOD (Column-wise)", "Col", solve_cephalopod(cols))]
    for title, label, solver in solvers:
        print(f"\n=== {title} ===")
        total = 0
        for i, (equation, operator) in enumerate(solver, start=1):
            result = calculate(equation, operator)
            total += result
            flat_nums = [n for group in equation for n in group]
            expression = f" {operator} ".join(str(n) for n in flat_nums)
            print(f"{label} {i} Results: {expression} = {result}")
        print(f"{title.split(':')[0].strip()} TOTAL: {total}")

if __name__ == "__main__":
    main()
