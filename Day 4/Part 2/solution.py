from sys import argv

def solution():
    with open(argv[1], "r") as file:
        contents = file.readlines()

        count = 0

        while True:
            removed = 0

            for line_index, line in enumerate(contents):
                line = line.strip()
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
                        removed += 1
                        contents = [list(line) for line in contents]
                        contents[line_index][char_index] = 'x'
                        contents = [''.join(line) for line in contents]
            if removed == 0:
                break

        print(count)                

if __name__ == "__main__":
    solution()
