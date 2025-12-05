from sys import argv

def solution():
    fresh = 0
    with open(argv[1], 'r') as file:
        lines = file.readlines()
        intervals = [index := -1] and [(index := index + 1, int(line.split('-')[0].strip()), int(line.split('-')[1].strip())) for line in lines if '-' in line]
        ingrediants = [int(line.strip()) for line in lines[intervals[len(intervals) - 1][0] + 2:]]


        for ingrediant in ingrediants:
            prev_fresh = fresh
            for interval in intervals:
                if ingrediant >= interval[1] and ingrediant <= interval[2]:
                    fresh += 1
                if fresh > prev_fresh:
                    break

        print(fresh)
                    

if __name__ == "__main__":
    solution()
