from sys import argv
import re


def solution():
    pattern = r"^(?P<group>\d{1,100})(?P=group)+$"

    sum = 0
    with open(argv[1], "r") as file:
        contents = file.readline().strip()
        for interval in contents.split(","):
            for i in range(int(interval.split("-")[0]), int(interval.split("-")[1]) + 1):
                mat = re.match(pattern, str(i))
                if mat:
                    sum += int(i)
    print(sum)

if __name__ == "__main__":
    solution()
    
