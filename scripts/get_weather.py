#!/usr/bin/python

from __future__ import print_function

import dateutil.parser as dup
import datetime as dt
import requests
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="""
    
    python get_weather.py airport [date]
""")

    parser.add_argument('airport')
    parser.add_argument('--base-dir', help='The base directory where to store retrieved weather data')
    parser.add_argument('--date', help='Get the weather for a particular date (YYYY-MM-DD)')
    parser.add_argument('--until', help='Get every day between the specified date (or today) and this date (counting backwards)')
    #parser.add_argument('-u', '--useless', action='store_true', 
    #					 help='Another useless option')
    args = parser.parse_args()

    if args.date is not None:
        date = dup.parse(args.date)
    else:
        date = dt.datetime.now()

    if args.until is None:
        until = date
    else:
        until = dup.parse(args.until)

    while date >= until:
        url = ("https://www.wunderground.com/history/airport/"
               "{airport}/{year}/{month}/{day}/DailyHistory.html?"
               "reqdb.magic=1&reqdb.wmo=99999&format=1".format(airport=args.airport, 
                                                              year=date.year, 
                                                              month=date.month, 
                                                              day=date.day))
        print("url:", url)
        date -= dt.timedelta(days=1)


    

if __name__ == '__main__':
    main()


