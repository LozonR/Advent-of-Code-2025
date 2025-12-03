print("Solution: " + str(sum([(lower := interval.split("-")[0], upper := interval.split("-")[1], sum([i for i in range(int(lower), int(upper) + 1) if __import__("re").match(r"^(?P<group>\d{1,100})(?P=group)+$", str(i))]))[2] for interval in open("input.txt", "r").readline().strip().split(",")])))
 
