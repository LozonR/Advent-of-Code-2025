from sys import argv

def solution():
    sum = 0
    with open(argv[1], "r") as file:
        for line in file.readlines():
            (digit1, digit2) = (0, 0)
            index = 0

            for i, character in enumerate(list(line.strip()[:len(line) - 2])):
                if digit1 < int(character):
                    digit1 = int(character)
                    index = i

            for character in list(line.strip()[index + 1:]):
                digit2 = max(digit2, int(character))

            num = 10*digit1 + digit2
            print(num)
            sum += num
            
    print(f"Solution: {sum}")

if __name__ == "__main__":
    solution()
