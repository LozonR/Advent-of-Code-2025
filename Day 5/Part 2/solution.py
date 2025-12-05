from sys import argv

def solution():
    with open(argv[1], 'r') as file:
        lines = file.readlines()
        intervals = [index := -1] and [(index := index + 1, int(line.split('-')[0].strip()), int(line.split('-')[1].strip())) for line in lines if '-' in line]

        combined_interval = [intervals[0][1], intervals[0][2]]

        subtract = []

        for interval in intervals[1:]:
            interval = interval[1:]
            if interval[1] < combined_interval[0]:
                subtract_add = [interval[1] + 1, combined_interval[0] - 1]
                subtract.append(subtract_add)
            combined_interval[0] = min(combined_interval[0], interval[0])

            if interval[0] > combined_interval[1]:
                subtract_add = [combined_interval[1] + 1, interval[0] - 1]
                subtract.append(subtract_add)
            combined_interval[1] = max(interval[1], combined_interval[1])

        for interval in intervals[1:]:
            interval = list(interval[1:])
            for subtract_subtract in subtract:
                if subtract_subtract[0] >= interval[0] and subtract_subtract[1] <= interval[1]: # sub_sub in int fully
                    subtract.remove(subtract_subtract)
                    continue
                if subtract_subtract[0] < interval[0] and subtract_subtract[1] > interval[1]: # int in sub_sub fully
                    subtract.remove(subtract_subtract)
                    new_subtracts = [[subtract_subtract[0], interval[0] - 1], [interval[1] + 1, subtract_subtract[1]]]
                    subtract.append(new_subtracts[0])
                    subtract.append(new_subtracts[1])
                    continue
                if interval[1] >= subtract_subtract[0] and interval[1] < subtract_subtract[1]:
                    subtract_subtract[0] = interval[1] + 1

                if interval[0] <= subtract_subtract[1] and interval[0] > subtract_subtract[0]:
                    subtract_subtract[1] = interval[0] - 1

        include_size = combined_interval[1] - combined_interval[0] + 1
        exclude_size = sum([(sub[1] - sub[0] + 1) for sub in subtract])

        print(include_size - exclude_size)
          
if __name__ == "__main__":
    solution()
