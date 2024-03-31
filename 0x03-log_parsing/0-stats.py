#!/usr/bin/python3
"""Check the stats of file"""
import sys
from signal import SIGINT
import re


def check_format(stringTocheckFor):
    """Check the formatting"""
    adrs = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    tmstp = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}'
    mtd = r'\w+'
    pth = r'[^"]+'
    c = r'\d{3}'
    byt = r'\d+'

    pattern = rf'^({adrs}) - \[({tmstp})\] "({mtd})\s({pth})" ({c}) ({byt})$'
    return re.match(pattern, stringTocheckFor)


def print_status_code(keyCodes, status_code_list):
    """Print status code"""
    for index, status_code in enumerate(status_code_list):
        print("{}: {}".format(status_code, keyCodes[status_code]))


if __name__ == "__main__":
    counter = 0
    keyCodes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    status_code_list = [200, 301, 400, 401, 403, 404, 405, 500]
    for line in sys.stdin:
        isValidFormat = check_format(line)
        if isValidFormat:
            counter += 1
            if counter < 10 and SIGINT:
                status_code = int(isValidFormat.group(5))
                if not isinstance(status_code, int) or not status_code:
                    pass
                file_size = isValidFormat.group(6)
                file_size += file_size
                try:
                    keyCodes[status_code] += 1
                except (IndexError) as e:
                    print('{}: The index is out of range'.format(e))
            if (counter == 10):
                counter = 0
                print_status_code(keyCodes, status_code_list)
                print("File size: {}".format(file_size))
