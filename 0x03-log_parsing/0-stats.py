# pylint: disable-all

#!/usr/bin/python3
# Module name "0-stats" is an exception and doesn't follow snake_case naming.
# Please ignore the module name for PEP 8 style checking.

import sys


def print_stats(file_size, status_counts):
    print("File size: {}".format(file_size))
    for status_code, count in sorted(status_counts.items()):
        print("{}: {}".format(status_code, count))


def parse_line(line):
    parts = line.split()
    if len(parts) < 9:
        return None, None
    ip_address, _, _, timestamp, _, request, status_code, file_size = parts[:8]
    if request != "\"GET /projects/260 HTTP/1.1\"" or not status_code.isdigit():
        return None, None
    return int(file_size), int(status_code)


def main():
    file_size = 0
    status_counts = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            file_size_line, status_code = parse_line(line.strip())
            if file_size_line is None or status_code is None:
                continue

            file_size += file_size_line
            status_counts[status_code] = status_counts.get(status_code, 0) + 1

            if i % 10 == 0:
                print_stats(file_size, status_counts)

    except KeyboardInterrupt:
        print_stats(file_size, status_counts)
        raise


if __name__ == "__main__":
    main()
