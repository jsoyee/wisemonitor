#!/usr/bin/python
import sys
import time
from datetime import datetime, timedelta


def force_print(msg):
    print >> sys.stderr, msg


def make_timestamp(datetime):
    return int(time.mktime(datetime))


def get_before(**kwargs):
    now = datetime.now()
    return now - timedelta(**kwargs)


def get_two_hours_ago():
    ago = get_before(seconds=7200)
    return make_timestamp(ago.timetuple())


def get_one_day_ago():
    ago = get_before(days=1)
    return make_timestamp(ago.timetuple())


def get_one_week_ago():
    ago = get_before(days=30)
    return make_timestamp(ago.timetuple())


def get_one_year_ago():
    ago = get_before(days=365)
    return make_timestamp(ago.timetuple())


if __name__ == '__main__':
    print get_two_hours_ago()
    print get_one_day_ago()
    print get_one_week_ago()
    print get_one_year_ago()
    