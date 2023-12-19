#!/usr/bin/python3
"""Input stats"""
import sys

stats = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

total_size = 0


def print_stats():
    print(f'File size: {total_size}')
    for status_code, count in sorted(stats.items()):
        if count:
            print(f'{status_code}: {count}')


try:
    for i, line in enumerate(sys.stdin, start=1):
        matches = line.rstrip().split()
        try:
            status_code = matches[-2]
            file_size = matches[-1]
            if status_code in stats.keys():
                stats[status_code] += 1
            total_size += int(file_size)
        except Exception:
            # ignore lines that don't match the format
            pass
        if i % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
