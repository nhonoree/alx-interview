#!/usr/bin/python3
"""
Log parsing script
Reads stdin line by line and computes metrics:
- Total file size
- Count of status codes
"""

import sys
import signal

# Initialize metrics
total_size = 0
status_counts = {}
valid_status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
line_count = 0

def print_stats():
    """Prints the accumulated metrics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        print("{}: {}".format(code, status_counts[code]))

try:
    for line in sys.stdin:
        line_count += 1
        try:
            parts = line.strip().split()
            if len(parts) < 7:
                continue

            status_code = parts[-2]
            file_size = parts[-1]

            # Update file size
            total_size += int(file_size)

            # Update status code count
            if status_code in valid_status_codes:
                if status_code not in status_counts:
                    status_counts[status_code] = 1
                else:
                    status_counts[status_code] += 1

        except (IndexError, ValueError):
            continue

        # Print stats after every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

# Final output after input ends
print_stats()
