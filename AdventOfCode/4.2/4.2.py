import tools


guards = tools.prepare_data()
sleepiest_minute = tools.get_sleepiest_guard_minute(guards)
print(sleepiest_minute['guard'] * sleepiest_minute['minute'])
