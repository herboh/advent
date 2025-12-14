import csv

matching_ids = []

def repeats(id_str):
    """Check if the ID has any repeating pattern."""
    length = len(id_str)

    # Check patterns of length > 2 and no more than half the number of total digits
    for chunk_size in range(1, length // 2 + 1):
        # check if str is divisible by chunk size
        if length % chunk_size != 0:
            continue
        # split
        chunks = [id_str[i:i+chunk_size] for i in range(0, length, chunk_size)]
        # check if repeat
        if len(set(chunks)) == 1:
            matching_ids.append(int(id))
            return True # Found Pattern and Added to List
    return False # No pattern

with open('input.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        for id_range in row:
            # Create lists of ids for each range
            start, end = map(int, id_range.split('-'))
            ids = list(range(start, end + 1))
            # Load each value as a string, split, and compare the halves
            for id in ids:
                id_str = str(id)
                repeats(id_str)

print(f"List of Invalid IDs:{matching_ids}")
print(f"Sum of Invalid IDs:{sum(matching_ids)}")

