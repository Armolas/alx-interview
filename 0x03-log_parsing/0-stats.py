#!/usr/bin/python3
'''log parsing'''
import sys
import signal

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

def print_stats():
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 9:
            continue
        
        ip = parts[0]
        status_code = parts[8]
        file_size = parts[9]
        
        try:
            file_size = int(file_size)
            total_size += file_size
        except ValueError:
            continue

        if status_code in status_counts:
            status_counts[status_code] += 1
        
        line_count += 1
        
        if line_count == 10:
            print_stats()
            line_count = 0

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
