import sys

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

line_count = 0

try:
    for line in sys.stdin:
        # Split the line into its components
        parts = line.split()

        if len(parts) != 7:
            continue  # Skip lines that don't match the input format

        # Extract status code and file size
        status_code = int(parts[5])
        file_size = int(parts[6])

        # Update metrics
        total_file_size += file_size
        status_code_counts[status_code] += 1

        line_count += 1

        # Check if it's time to print statistics
        if line_count % 10 == 0:
            print(f"File size: {total_file_size}")
            for code, count in sorted(status_code_counts.items()):
                if count > 0:
                    print(f"{code}: {count}")

except KeyboardInterrupt:
    pass

# Print final statistics
print(f"File size: {total_file_size}")
for code, count in sorted(status_code_counts.items()):
    if count > 0:
        print(f"{code}: {count}")

