from sys import argv

def solution():
    lines = None
    with open(argv[1], 'r') as file:
        lines = file.readlines()

    operations = [operation.strip() for operation in lines[-1].split(' ') if not operation.isspace() and operation != '' and operation is not None]

    lines.pop(-1)

    rows = [[character for character in line if character != '\n'] for line in lines]

    cols = [[0 for row in range(len(rows))] for col in range(len(rows[0]))]

    for i, row in enumerate(rows):
        for j, spot in enumerate(row):
            cols[j][i] = rows[i][j]

    num_equations = 1
    
    for col in cols:
        if len(set(col)) == 1 and col[0] == ' ': # in between equations
            num_equations += 1

    answers = [(0 if operations[equation] == '+' else 1) for equation in range(num_equations)]

    answer_number = 0

    for col in cols:
        if len(set(col)) == 1 and col[0] == ' ':
            answer_number += 1
            continue

        num = ''.join(str(digit) for digit in col)

        if operations[answer_number] == '+':
            answers[answer_number] += int(num)
        else:
            answers[answer_number] *= int(num)
                

    print(sum(answers))

if __name__ == "__main__":
    solution()
