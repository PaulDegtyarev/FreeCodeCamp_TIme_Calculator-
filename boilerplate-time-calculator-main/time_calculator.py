# Работает

def add_time(start, duration, start_day=None):

    # Переводим время начала в формат часов и минут
    start_hour, period = start.split()
    start_hour, start_minute = int(start_hour.split(':')[0]), int(start_hour.split(':')[1])

    duration_hour, duration_minute = map(int, duration.split(':'))

    new_hour = start_hour + duration_hour
    new_minute = start_minute + duration_minute

    if new_minute >= 60:
        new_hour += 1
        new_minute -= 60

    days_passed = new_hour // 24 if period == "AM" else round(new_hour / 24)
    new_hour %= 24
    new_period = period

    if new_hour >= 12:
        new_period = "PM" if period == "AM" else "AM"
        new_hour %= 12

    if new_hour == 0:
        new_hour = 12

    if start_day:
        days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        start_day = start_day.lower()
        start_day_index = days_of_week.index(start_day)
        new_day_index = (start_day_index + days_passed) % 7
        new_day = days_of_week[new_day_index].capitalize()
        new_time = f"{new_hour}:{new_minute:02} {new_period}, {new_day}"
    else:
        new_time = f"{new_hour}:{new_minute:02} {new_period}"

    if days_passed == 0:
        return new_time
    elif days_passed == 1:
        return f"{new_time} (next day)"
    else:
        return f"{new_time} ({days_passed} days later)"
