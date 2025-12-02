from sys import argv

STARTING_POINT = 50

def solution():
  location = STARTING_POINT
  count = 0

  with open(argv[1], "r") as file:
    for line in file.readlines():
      dir = 1 if line[0] == 'R' else -1
      amount = int(line[1:])

      # Greatest one-liner of all time
      count += (1 if (location % 100 != 0 and (-1)*dir*(location + dir*(amount % 100)) <= (0 if dir == -1 else -100)) else 0) + amount // 100

      location = (location + amount*dir) % 100
    print(f"Solution: {count}")

if __name__ == "__main__":
  solution()
