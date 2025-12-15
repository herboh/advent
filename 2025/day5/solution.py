# Part 1 Solution
def check_freshness(ranges, ids):
    valid_ids = []
    # for given ID, check if its within each range, end and repeat once found
    for id_num in ids:
        for start, end in ranges:
            if start <= id_num <= end:
                valid_ids.append(id_num)
                break
    return valid_ids

# Part 2 Solution - total number of valid IDs
def count_fresh_ids(ranges):
    def get_start(range_tuple):
        return range_tuple[0]

    # Sorts by start, then creates a working list
    sorted_ranges = sorted(ranges, key=get_start)
    merged = [sorted_ranges[0]]

    # Uses last piece of working list, checks if next is overlapping or adjacent
    for start, end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end +1:
            merged[-1] = (last_start, max(last_end, end))
        # appends as a new range tuple since it isnt touching
        else:
            merged.append((start, end))

    # calculates the total count of values in our ranges
    total = sum(end - start + 1 for start, end in merged)
    return total

# Split the data on line break into ranges and IDs
def load_data(file):
    with open(file, 'r') as f:
        data = f.read().strip()
        fresh, item = data.split('\n\n')

        ranges = []
        for line in fresh.splitlines():
            start, end = map(int, line.split('-'))
            ranges.append((start, end))

        ids = [int(line) for line in item.splitlines()]

        return ranges, ids

ranges, ids = load_data("input.txt")
total_ids = len(ids)
valid_ids = check_freshness(ranges, ids)
fresh_count = count_fresh_ids(ranges)

print(f"Fresh IDs: {valid_ids}")
print(f"Total Inventory: {total_ids}")
print(f"Total matches: {len(valid_ids)}") # Part 1 Answer
print(f"Total Fresh IDs: {fresh_count}") # Part 2 Answer
