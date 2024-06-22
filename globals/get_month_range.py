from datetime import datetime, timedelta

def get_month_range(year, month):
    first_day = datetime(year, month, 1)
    next_month = first_day.replace(day=28) + timedelta(days=4)  # this will never fail
    last_day = next_month - timedelta(days=next_month.day)
    return first_day, last_day