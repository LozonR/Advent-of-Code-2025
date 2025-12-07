from sys import argv

def solution():
    lines = None
    with open(argv[1], 'r') as file:
        lines = file.readlines()

    starting_pos = int(lines[0].find('S'))

    locations = {
        starting_pos: 1
    }


    for i in range(len(lines[0])):
        if i not in locations.keys():
            locations[i] = 0

    for line in lines[1:]:
        for location in locations.keys():
            if line[location] == '^':
                locations[location + 1] += locations.get(location)
                locations[location - 1 ] += locations.get(location)
                locations[location] = 0
                

    print(sum(locations.values()))

if __name__ == "__main__":
    solution()
