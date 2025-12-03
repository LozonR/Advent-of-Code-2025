from sys import argv

def solution():
    sum = 0
    with open(argv[1], "r") as file:
        for line in file.readlines():
            i = 0
            num = 0
            digits = [0] * 12
            for k in range(11):
                for character in list(line.strip())[i:len(line.strip()) - 11 + k]:
                    if digits[k] < int(character):
                        digits[k] = int(character)
                        i = line.strip().find(character, i, len(line.strip()) - 11 + k) + 1

                num += (10**(12 - k - 1))*digits[k]

            for character in list(line.strip())[i:len(line.strip())]:
                    if digits[11] < int(character):
                        digits[11] = int(character)
                        i = line.strip().find(character, i, len(line.strip()))

            sum += num + digits[11]
        print(sum)
            
    print(f"Solution: {sum}")

if __name__ == "__main__":
    solution()
