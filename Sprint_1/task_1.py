time_string = '1h 45m,360s,25m,30m 120s,2h 60s'

times = time_string.split(',')

total_minutes = 0

for time in times:
    parts = time.split()

    for part in parts:
        if 'h' in part:
            total_minutes += int(part.replace('h', '')) * 60

        elif 'm' in part:
            total_minutes += int(part.replace('m', ''))

        elif 's' in part:
            total_minutes += int(part.replace('s', '')) // 60

print(total_minutes)