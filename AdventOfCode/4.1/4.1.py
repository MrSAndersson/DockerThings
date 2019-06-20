class Guard:
    def __init__(self):
        self.sleep_times = []
        self.total_sleep = 0

def import_data():
    file = open("Input.txt")

    data = []
    for line in file:
        data.append(line.rstrip('\n'))
    data.sort()
    return data



data = import_data()

guards = {}

for line in data:
    if "begins shift" in line:
        guard_id = line.split('#', 1)[1].split(' ', 1)[0]
        if not guards.__contains__(guard_id):
            guards[guard_id] = Guard()
    elif "falls asleep" in line:
        start = int(line.split(':', 1)[1].split(']', 1)[0])
    else:
        end = int(line.split(':', 1)[1].split(']', 1)[0])
        guards[guard_id].sleep_times.append('{} {}'.format(start, end))
        guards[guard_id].total_sleep += end - start + 1