from datetime import datetime, timedelta

def next_three_days():
    dates = []
    for i in range(3):
        date = datetime.now() + timedelta(days=i+1)
        dates.append(date.strftime('%Y-%m-%d'))
    return dates
