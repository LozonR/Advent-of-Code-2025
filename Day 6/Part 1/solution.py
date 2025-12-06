from sys import argv

def solution():
    total = 0
    lines_cleaned = []
    with open(argv[1], 'r') as file:
        for line in file.readlines():
            line_split = line.split(' ')
            line = []
            for thing in line_split:
                if thing.isspace() or thing == '' or thing is None:
                    continue
                line.append(thing)
            lines_cleaned.append(line)

    equations = [[[] for i in range(len(lines_cleaned[1]))] for i in range(len(lines_cleaned))][0]
    for line in lines_cleaned:
        for k, num in enumerate(line):
            equations[k].append(num)

    for equation in equations:
        operation = equation[-1]
        subtotal = 0 if operation == '+' else 1
        for num in equation[:-1]:
            subtotal = subtotal + int(num) if operation == '+' else subtotal * int(num)

        total += subtotal

    print(total)

if __name__ == "__main__":
    solution()
