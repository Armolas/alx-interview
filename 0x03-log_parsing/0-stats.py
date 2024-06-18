#!/usr/bin/python3
'''log parsing'''
import sys
import signal
import re

# Initialize metrics
total_size = 0
status_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

# Regular expression to match the log line format
log_pattern = re.compile(
    r'^\d{1,3}(\.\d{1,3}){3} - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
)


def print_stats():
    """Print the current statistics."""
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")


def signal_handler(sig, frame):
    """Handle keyboard interruption."""
    print_stats()
    sys.exit(0)


# Set up signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

line_count = 0

try:
    for line in sys.stdin:
        match = log_pattern.match(line.strip())
        if not match:
            continue

        status_code = match.group(2)
        file_size = int(match.group(3))

        # Update total file size
        total_size += file_size

        # Update status code count
        if status_code in status_counts:
            status_counts[status_code] += 1

        line_count += 1

        if line_count == 10:
            print_stats()
            line_count = 0

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

# Print final stats if the loop ends
print_stats()
