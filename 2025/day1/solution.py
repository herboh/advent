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
for line in lines:
    current_position= (current_position+line) % len(lock)
    positions.append(current_position)
    print(current_position)

print(positions.count(0))
