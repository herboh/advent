lock=100
current_position=50

positions = [current_position]
total_zero = 0

with open('input.txt', 'r') as f:
    for line in f:
        move = int(line.replace('L', '-').replace('R', ''))
        previous_position = current_position
        current_position += move

        #Solve Part 1
        dial = current_position % lock
        positions.append(dial)

        # Solve Part 2
        clicks_at_zero = 0 
        if move > 0: 
            clicks_at_zero = (current_position // lock) - (previous_position // lock)
        elif move < 0:
            clicks_at_zero = (previous_position - 1) // lock - (current_position - 1) // lock
        total_zero += clicks_at_zero


print("Times landeed on 0:")
print(positions.count(0))

print("Times passed 0:")
print(total_zero)
