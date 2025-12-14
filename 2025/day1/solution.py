lock=list(range(100))
lines=[]
current_position=50

def parse_direction(value):
    direction = value[0]  # 'L' or 'R'
    number = int(value[1:])  # Extract the numeric part
    return -number if direction == 'L' else number

with open('input.txt', 'r') as fd:
    for line in fd:
        stripped = line.strip()
        if stripped:
            lines.append(parse_direction(stripped))

# print(lines)
# print(lock)

positions = [current_position]
times_past_0 = 0
for line in lines:
    clicks = abs(line)
    times_past_0 += clicks // len(lock)  # Full circles
    if line > 0:
        if current_position + (clicks % 100) > 100:
            times_past_0 += 1
    else:
        if current_position - (clicks % 100) < 0:
            times_past_0 += 1
    current_position = (current_position + line) % 100
    positions.append(current_position)
    print(current_position)

print(times_past_0)
print(positions.count(0))
final = times_past_0+positions.count(0)
print(final)
