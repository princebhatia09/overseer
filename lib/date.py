from datetime import datetime
import time


def get_current_datetime():
    today = datetime.today()
    current_time = today.strftime('%Y-%m-%d %H:%M:%S')
    return current_time


def get_time_diff(last_scan):
    current_time = get_current_datetime()

    fmt = '%Y-%m-%d %H:%M:%S'
    d1 = datetime.strptime(last_scan, fmt)  # '2018-11-09 6:00:00'
    d2 = datetime.strptime(current_time, fmt)

    # Convert to Unix timestamp
    d1_ts = time.mktime(d1.timetuple())
    d2_ts = time.mktime(d2.timetuple())

    # They are now in seconds, subtract and then divide by 60 to get minutes.
    time_difference = int(d2_ts - d1_ts) / 60  # Time difference in minutes

    return time_difference
