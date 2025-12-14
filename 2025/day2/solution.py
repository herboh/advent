import csv

matching_ids = []

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
                mid = len(id_str) // 2
                first_half = id_str[:mid]
                second_half = id_str[mid:]
                if first_half == second_half:
                    matching_ids.append(int(id))

print(f"List of Invalid IDs:{matching_ids}")
print(f"Sum of Invalid IDs:{sum(matching_ids)}")


