class Guard:
    def __init__(self, id):
        self.sleep_times = []
        self.total_sleep = 0
        self.id = int(id)

    def sleepiest_minute(self):
        most_sleep = {'minute': 0, 'count': 0}
        for minute in range(59):
            mins_counter = 0
            for sleep in self.sleep_times:
                start = int(sleep.split(' ')[0])
                end = int(sleep.split(' ')[1])
                if start <= minute < end:
                    mins_counter += 1
            if most_sleep['count'] < mins_counter:
                most_sleep = {'minute': minute, 'count': mins_counter}
        return most_sleep


def import_data():
    file = open("Input.txt")

    data = []
    for line in file:
        data.append(line.rstrip('\n'))
    data.sort()
    return data


def prepare_data():

    data = import_data()
    guards = {}

    for line in data:
        if "begins shift" in line:
            guard_id = line.split('#', 1)[1].split(' ', 1)[0]
            if not guards.__contains__(guard_id):
                guards[guard_id] = Guard(guard_id)
        elif "falls asleep" in line:
            start = int(line.split(':', 1)[1].split(']', 1)[0])
        else:
            end = int(line.split(':', 1)[1].split(']', 1)[0])
            guards[guard_id].sleep_times.append('{} {}'.format(start, end))
            guards[guard_id].total_sleep += end - start
    return guards


def get_sleepiest_guard(guards):
    sleepiest_guard = Guard(0)
    for guard in guards:
        if sleepiest_guard.total_sleep < guards[guard].total_sleep:
            sleepiest_guard = guards[guard]
    return sleepiest_guard
