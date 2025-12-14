import csv

matching_ids = []
mirrored_ids = []

def repeats(id_str):
    """Check if the ID has any repeating pattern."""
    length = len(id_str)

    # Check patterns of length > 2 and no more than half the number of total digits
    for chunk_size in range(1, length // 2 + 1):
        if length % chunk_size != 0:
            continue

        # split into chunks and check for matching chunks
        chunks = [id_str[i:i+chunk_size] for i in range(0, length, chunk_size)]
        if len(set(chunks)) == 1:
            return True 

    return False

with open('input.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        for id_range in row:
            # Create lists of ids for each range
            start, end = map(int, id_range.split('-'))
            for id in range(start, end + 1):
                id_str = str(id)
                if repeats(id_str):
                    #Part1
                    mid = len(id_str) // 2
                    if id_str[:mid] == id_str[mid:]:
                        mirrored_ids.append(id)

                    #Part 2
                    matching_ids.append(id)

#print(f"List of Invalid IDs:{matching_ids}")
print(f"Part2 - Sum of Invalid IDs:{sum(matching_ids)}")
print(f"Part1 - Sum of Mirror Invalid IDs:{sum(mirrored_ids)}")

