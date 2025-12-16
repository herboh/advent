def load_data(path):
    with open(path) as f:
        lines = [line.replace('\n', '') for line in f]

    cols = list(zip(*lines))
    return lines, cols

def solve_cephalopod(cols):
    print(f"________break_______")
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

def calculate(equation, operator):
    nums = [n for group in equation for n in group]

    if operator == '*':
        result = 1
        for n in nums:
            result *= n
        return result
    elif operator == '+':
        return sum(nums)
    return None

def main() -> None:
    lines, cols = load_data("input.txt")
    print(f"Loaded data Lines: {lines}")
    print(f"Loaded data Cols: {cols}")

    total = 0

    for i, (equation, operator) in enumerate(solve_cephalopod(cols), start=1):
        result = calculate(equation, operator)
        total += result
        print(f"Col {i} Results: {result} | operator={operator} | equation={equation}")

    print(f"\nTOTAL: {total}")

if __name__ == "__main__":
    main()
