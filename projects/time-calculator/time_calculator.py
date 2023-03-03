""" def add_time(start_time, duration, start_day=None):
    # Convert start_time to 24-hour format
    start_time_parts = start_time.split()
    start_hour, start_minute = map(int, start_time_parts[0].split(':'))
    if start_time_parts[1] == 'PM' and start_hour != 24:
        start_hour += 24

    # Convert duration to hours and minutes
    duration_parts = duration.split(':')
    duration_hour, duration_minute = map(int, duration_parts)
    total_duration_minutes = duration_hour * 60 + duration_minute

    # Calculate end time
    end_minutes = (start_hour * 60 + start_minute + total_duration_minutes) % (24 * 60)
    end_hour, end_minute = divmod(end_minutes, 60)
    end_hour = end_hour if end_hour <= 12 else end_hour - 12
    end_period = 'AM' if end_hour < 12 else 'PM'

    # Format result time string
    result_time = '{:d}:{:02d} {}'.format(end_hour, end_minute, end_period)

    # Calculate number of days later
    num_days_later = (start_hour * 60 + start_minute + total_duration_minutes) // (24 * 60)

    # Add day of week if start_day is given
    if start_day:
        start_day = start_day.capitalize()
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        start_day_index = days_of_week.index(start_day)
        end_day_index = (start_day_index + num_days_later) % 7
        end_day = days_of_week[end_day_index]
        result_time += ', ' + end_day

    # Add number of days later to result string
    if num_days_later == 1:
        result_time += ' (next day)'
    elif num_days_later > 1:
        result_time += ' ({} days later)'.format(num_days_later)

    return result_time

print(add_time("3:30 PM", "2:12"))
print(add_time("11:55 AM", "3:12"))
print(add_time("9:15 PM", "5:30"))
print(add_time("11:40 AM", "0:25"))
print(add_time("2:59 AM", "24:00"))
print(add_time("11:59 PM", "24:05"))
print(add_time("8:16 PM", "466:02"))
print(add_time("5:01 AM", "0:00"))
print(add_time("3:30 PM", "2:12", "Monday"))
print(add_time("2:59 AM", "24:00", "saturDay"))
print(add_time("11:59 PM", "24:05", "Wednesday"))
print(add_time("8:16 PM", "466:02", "tuesday")) """


def add_time(start, duration, dayofweek = ""):
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    def period(time): return time.split()
    def time_split(time): return [int(i) for i in time.split(':')]

    period_switch = {
        'AM': 'PM',
        'PM': 'AM'
    }

    time, init_period = period(start)
    init_hours, minutes = time_split(time)
    add_h, add_m = time_split(duration)

    hours = init_hours + add_h
    minutes += add_m
    days_later = 0
    dow, dlater, new_period = [''] * 3

    if minutes >= 59:
        hours += (minutes // 60)
        minutes %= 60

    if hours >= 24:
        days_later += hours // 24
        hours %= 24

    if (init_hours <= 11) and (hours > 11):
        new_period = period_switch[init_period]
        if (init_period, new_period) == ('PM', 'AM'):
            days_later += 1

        if hours > 12:
            hours %= 12

    if dayofweek:
        dayofweek_idx = (days.index(
            dayofweek.lower()) + days_later) % len(days)
        dow = f", {days[dayofweek_idx].title()}"

    if days_later == 1:
        dlater = " (next day)"
    elif days_later > 1:
        dlater = f" ({days_later} days later)"

    new_time = f"{hours}:{str(minutes).rjust(2, '0')} {new_period or init_period}{dow}{dlater}"

    return new_time


if __name__ == "__main__":
    current = add_time("11:43 PM", "24:20", "tueSday")
    expected = "12:03 AM, Thursday (2 days later)"

    if current != expected:
        print(current)
    else:
        print("Well done!")