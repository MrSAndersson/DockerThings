import tools


guards = tools.prepare_data()
sleeper = tools.get_sleepiest_guard(guards)
sleepiest_minute = sleeper.sleepiest_minute()

print(sleeper.id * sleepiest_minute['minute'])
