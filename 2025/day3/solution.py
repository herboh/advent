total_joltage = 0
counter = 0
num_digits=12

def get_digit(s, num_digits, start_index=0):
        # Base case: if we need 0 digits, return empty string
        if num_digits == 0:
            return ""

        # Get the last index we can select from, so that we are still making a 12 digit number
        end_index = len(s) - num_digits + 1

        sub = s[start_index:end_index]
        max_digit = max(sub)
        max_index = start_index + sub.index(max_digit)

        rest_of_digits = get_digit(s, num_digits -1, max_index + 1)

        return max_digit + rest_of_digits



with open('input.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        counter += 1

        # get digits
        digit_string = get_digit(line, num_digits)
        joltage = int(digit_string) 

        total_joltage += joltage

        print(f"bank={line}")
        print(f"joltage for bank {counter} = {joltage}")

print(f"Total Joltage = {total_joltage}")
