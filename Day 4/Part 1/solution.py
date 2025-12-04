from sys import argv

def solution():
    with open(argv[1], "r") as file:
        contents = file.readlines()

        count = 0

        for line_index, line in enumerate(contents):
            line = line.strip()
            print(line)
            for char_index, character in enumerate(line):
                if character != '@':
                    continue
                surrounding = 0
                if char_index != 0:
                    surrounding += 1 if contents[line_index][char_index - 1] == '@' else 0
                if char_index != len(line) - 1:
                    surrounding += 1 if contents[line_index][char_index + 1] == '@' else 0

                if line_index != 0:
                    surrounding += 1 if contents[line_index - 1][char_index] == '@' else 0
                    if char_index != 0:
                        surrounding += 1 if contents[line_index - 1][char_index - 1] == '@' else 0
                    if char_index != len(line) - 1:
                        surrounding += 1 if contents[line_index - 1][char_index + 1] == '@' else 0

                if line_index != len(contents) - 1:
                    surrounding += 1 if contents[line_index + 1][char_index] == '@' else 0

                    if char_index != 0:
                        surrounding += 1 if contents[line_index + 1][char_index - 1] == '@' else 0

                    if char_index != len(line) - 1:
                        surrounding += 1 if contents[line_index + 1][char_index + 1] == '@' else 0


                if surrounding < 4:
                    count += 1

        print(count)                

if __name__ == "__main__":
    solution()
