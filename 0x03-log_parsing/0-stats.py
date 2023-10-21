#!/usr/bin/python3
import sys

if __name__ == "__main__":
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    stats = {status: 0 for status in status_codes}
    size = 0
    try:
        for i, line in enumerate(sys.stdin, 1):
            split_line = line.split(' ')
            if len(split_line) < 2:
                continue
            if split_line[-2].isdigit():
                status = int(split_line[-2])
                if status in status_codes:
                    stats[status] += 1
            if split_line[-1].isdigit():
                size += int(split_line[-1])
            if i % 10 == 0:
                print("File size: {}".format(size))
                for status in sorted(stats.keys()):
                    if stats[status] > 0:
                        print("{}: {}".format(status, stats[status]))
    except KeyboardInterrupt:
        pass
    finally:
        print("File size: {}".format(size))
        for status in sorted(stats.keys()):
            if stats[status] > 0:
                print("{}: {}".format(status, stats[status]))
