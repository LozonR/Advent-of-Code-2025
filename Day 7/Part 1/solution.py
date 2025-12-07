from sys import argv

def solution():
    count = 0
    lines = None
    with open(argv[1], 'r') as file:
        lines = file.readlines()

    starting_pos = int(lines[0].find('S'))

    locations = [starting_pos]

    for line in lines:
        for location in locations:
            if line[location] == '^':
                locations = set(locations)
                locations.remove(location)
                locations.add(location + 1)
                locations.add(location - 1)
                locations = list(locations)
                count += 1

    print(count)

if __name__ == "__main__":
    solution()
