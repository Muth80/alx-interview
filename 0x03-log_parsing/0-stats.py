#!/usr/bin/python3
import sys
import signal

count_lines = 0
total_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

def print_stats():
    print("File size: {}".format(total_size))
    for status_code in sorted(status_codes.keys()):
        if status_codes[status_code] > 0:
            print("{}: {}".format(status_code, status_codes[status_code]))

def signal_handler(signal, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        try:
            ip, dash, date, request, status_code, file_size = line.split()
            file_size = int(file_size)
            if status_code in status_codes:
                total_size += file_size
                status_codes[status_code] += 1
        except ValueError:
            # Skip line if not in the correct format
            continue
        count_lines += 1
        if count_lines % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    raise

print_stats()
