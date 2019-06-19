class Guard:
    sleep_times = []
    total_sleep = 0


file = open("Input.txt")

data = []
for line in file:
    data.append(line.rstrip('\n'))
data.sort()

guards = {}

for line in data:
    if "begins shift" in line:
        guard_id = line.split('#', 1)[1].split(' ', 1)[0]
        guards[guard_id] = Guard()
    elif "falls asleep" in line:
        start = int(line.split(':', 1)[1].split(']', 1)[0])
    else:
        end = int(line.split(':', 1)[1].split(']', 1)[0])
        guards[guard_id].total_sleep += end - start
