lock_size = 100
current_position = 50 

positions = [current_position]
total_zero_clicks = 0

with open('input.txt', 'r') as f:
    for line in f:
        move = int(line.strip().replace('L', '-').replace('R', ''))
        clicks = abs(move)

        # Solve Part 1
        dial = current_position % lock_size
        positions.append(dial)

        # We know for sure we hit zero once per full spin
        full_spins = clicks // lock_size
        remainder = clicks % lock_size
        zero_clicks = full_spins

        # Solve Part 2
        if remainder > 0:
            if move > 0: # Right Turn
                # If we cross the 100 boundary
                if current_position + remainder >= lock_size:
                    zero_clicks+= 1
            else: # Left Turn
                # If we cross the 0 boundary and don't start at 0
                if current_position > 0 and current_position - remainder <= 0:
                    zero_clicks += 1

        total_zero_clicks += zero_clicks

        current_position = (current_position + move) % lock_size

print("Times landed on 0:")
print(positions.count(0))

print("Times passed 0:")
print(total_zero_clicks)
