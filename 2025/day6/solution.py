def load_data(path):
    with open(path, 'r') as f:
        return [line.rstrip('\n') for line in f]

def grab_equations (math_hw):
    equations = []
    operator_row = math_hw[3]

    operator_index = []
    for i, char in enumerate(operator_row):
            if char  != ' ':
                operator_index.append(i)

    for idx, start in enumerate(operator_index):
        if idx + 1 < len(operator_index):
            end = operator_index[idx+1] - 1
        else:
            end = len(operator_row)

        equation_block = [row[start:end] for row in math_hw[0:4]]
        equations.append(equation_block)
    return equations

def setup_cephalapod_math(equations):
    reversed_columns = []
    for eq in equations:
        reversed_eq = [row[::-1] for row in eq]
        reversed_columns.append(reversed_eq)

    results = []

    for block in reversed_columns:
        operator = None
        block_nums = []
        num_columns = len(block[0])

        for col_idx in range(len(block[0])):  # Iterate over character positions
            column = ''.join(row[col_idx] for row in block) 
            print(f"Column {col_idx}: '{column}'")

            if column[-1] in ['*', '+']:
                operator = column[-1]
                num_str = column[:-1].strip()
                if num_str:
                    block_nums.append(int(num_str))
            else:
                num_str = column.strip()
                if num_str:
                    block_nums.append(int(num_str))

        result = 0
        if operator == '*':
            result = 1
            for num in block_nums:
                result *= num
        elif operator == '+':
            result = sum(block_nums)

        print(f"  -> Result: {result}")
        results.append(result)

    return reversed_columns, results

def calculate_equations(column_str):
    operator = column_str[-1]  # Get sign
    numbers = []
    digits = [int(char) for char in column_str[:-1] if char.isdigit()]
    if operator == '*':
        result = 1
        for digit in digits:
            result *= digit
        return result
    elif operator == '+':
        result = sum(digits)
        return result
    else:
        print(f"Warning: Unknown operator '{operator}', returning 0")
        return 0

def main() -> None:
    math_hw = load_data("test_input.txt")
    #math_hw = load_data("input.txt")
    print(f"Loaded data:{math_hw}")

    problem = grab_equations(math_hw)
    print(f"These are the equations {problem}")

    reversed_data, results = setup_cephalapod_math(problem)  # Unpack the tuple
    print(f"Reversed data: {reversed_data}")

    print(f"------------------------------------------/n")
    print(f"Results: {results}")

    print(f"Sum of results: {sum(results)}")

if __name__ == "__main__":
    main()

