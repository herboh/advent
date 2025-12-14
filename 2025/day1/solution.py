lock=list(range(100))
current_position=50
counter = 0

positions = [current_position]
times_past_0 = 0

with open('input.txt', 'r') as fd:
    for line in fd.readlines():
        number = int(line.replace('L', '-').replace('R', ''))
        #When R, and move is greater than distance
        if number > 0 and current_position + number >= len(lock): 
            times_past_0 = (current_position + number) // len(lock)
            counter += times_past_0
        elif number < 0 and current_position + number < 0:
            times_past_0 = abs((current_position + number ) // len(lock))
            counter += times_past_0
        current_position= (current_position+number) % len(lock)
        # if current_position == 0:
        #     counter += 1
        positions.append(current_position)
        print(current_position)

print("Times landeed on 0:")
print(positions.count(0))

print("Times passed 0:")
print(counter)
