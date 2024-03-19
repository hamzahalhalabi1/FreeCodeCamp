def add_time(start, duration, *day):
    hour, minutes_period = start.split(':')
    hour = int(hour)
    minutes, period = minutes_period.split(' ')
    minutes = int(minutes)
    added_hours, added_minutes = map(int, duration.split(':'))

    new_hour = hour + added_hours
    new_minutes = minutes + added_minutes

    if new_minutes >= 60:
        new_hour += 1
        new_minutes -= 60

    if new_hour > 12:
        new_hour -= 12

    new_period = period

    if (hour + added_hours) // 12 % 2 == 1:
        if period == 'AM':
            new_period = 'PM'
        else:
            new_period = 'AM'

    new_time = f"{new_hour:02d}:{new_minutes:02d} {new_period}"

    if day:
        days = ', '.join(day)
        new_time += f", {days}"

    return new_time.strip()


print(add_time('11:55 AM', '3:12'))
