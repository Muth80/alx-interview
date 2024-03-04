#!/usr/bin/python3
import sys

status_codes_count = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
total_size = 0
lines_processed = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7 or '"' not in line:
            continue
        status_code = parts[-2]
        file_size = parts[-1]

        # Try to parse the file size and update metrics if successful
        try:
            total_size += int(file_size)
            if status_code in status_codes_count:
                status_codes_count[status_code] += 1
        except ValueError:
            # Skipping the line if file_size is not a number, as per requirements
            continue
        
        lines_processed += 1
        if lines_processed % 10 == 0:
            print("File size: {}".format(total_size))
            for code in sorted(status_codes_count.keys()):
                if status_codes_count[code] > 0:
                    print("{}: {}".format(code, status_codes_count[code]))

except KeyboardInterrupt:
    # This will handle the Ctrl + C interruption and print the metrics
    print("File size: {}".format(total_size))
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print("{}: {}".format(code, status_codes_count[code]))
    raise

# Finally, print the metrics before the program exits naturally
print("File size: {}".format(total_size))
for code in sorted(status_codes_count.keys()):
    if status_codes_count[code] > 0:
        print("{}: {}".format(code, status_codes_count[code]))
