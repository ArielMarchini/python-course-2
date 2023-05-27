import datetime


def gen_secs():
    """Generate seconds from 0 to 59."""
    for sec in range(0, 60):
        yield sec


def gen_minutes():
    """Generate minutes from 0 to 59."""
    for min in range(0, 60):
        yield min


def gen_hours():
    """Generate hours from 0 to 23."""
    for hour in range(0, 24):
        yield hour


def gen_time():
    """Generate time in the format HH:MM:SS."""
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, second)


def gen_years(start=datetime.date.today().year):
    """
    Generate years starting from the specified year.

    Args:
        start (int): The starting year. Defaults to the current year.

    Yields:
        int: The generated years.
    """
    yield start
    start += 1


def gen_months():
    """Generate months from 1 to 12."""
    for month in range(1, 13):
        yield month


def gen_days(month, leap_year=True):
    """
    Generate days for the specified month.

    Args:
        month (int): The month for which days are generated.
        leap_year (bool): Whether it is a leap year. Defaults to True.

    Returns:
        int: The number of days in the specified month.
    """
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and leap_year:
        return 28
    return days[month - 1]


def gen_date():
    """Generate date and time in the format DD/MM/YYYY HH:MM:SS."""
    for year in gen_years():
        for month in gen_months():
            for day in range(1, gen_days(month, year % 4 == 0 and year % 100 != 0)):
                for time in gen_time():
                    yield "{:02d}/{:02d}/{:04d} {}".format(day, month, year, time)


def main():
    """Print generated dates in the format DD/MM/YYYY HH:MM:SS."""
    gen = gen_date()
    next(gen)
    counter = 0

    while True:
        date = next(gen)
        counter += 1
        if counter % 1000000 == 0:
            print(date)


if __name__ == '__main__':
    main()