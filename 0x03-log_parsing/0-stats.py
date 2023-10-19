#!/usr/bin/python3
import sys

def print_statistics(total_size, status_codes):
    print("File size: {:d}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{:d}: {:d}".format(code, status_codes[code])

def main():
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    lines_processed = 0

    try:
        for line in sys.stdin:
            tokens = line.split()
            if len(tokens) == 7:
                status_code = int(tokens[6])
                if status_code in status_codes:
                    total_size += int(tokens[6])
                    status_codes[status_code] += 1
                    lines_processed += 1
            if lines_processed % 10 == 0:
                print_statistics(total_size, status_codes)
    except KeyboardInterrupt:
        pass

    print_statistics(total_size, status_codes)

if __name__ == "__main__":
    main()

