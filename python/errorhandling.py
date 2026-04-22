import os

def read_log(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()
            print(f"Successfully read {filename}")
            return content
    except FileNotFoundError:
        print(f"ERROR: File '{filename}' not found")
        return None
    except PermissionError:
        print(f"ERROR: No permission to read '{filename}'")
        return None

def parse_status(line):
    try:
        parts = line.strip().split(" status: ")
        if len(parts) != 2:
            raise ValueError(f"Unexpected format: {line.strip()}")
        return parts[0], parts[1]
    except ValueError as e:
        print(f"WARNING: Could not parse line - {e}")
        return None, None


print("--- Test 1: Reading a file that exists ---")
content = read_log("server_logs.txt")

print("\n--- Test 2: Reading a file that doesn't exist ---")
content = read_log("missing_file.txt")

print("\n--- Test 3: Parsing valid lines ---")
valid_lines = [
        "web-01 status: online",
        "deb-01 status: offline",
]
for line in valid_lines:
    server, status = parse_status(line)
    if server:
        print(f" Parsed - Server: {server}, Status: {status}")

print("\n--- Test 4: Parsing a badly formatted line ---")
bad_lines = [
        "this is not a valid log line",
        "web-02 status: online",
]
for line in bad_lines:
    server, status = parse_status(line)
    if server:
        print(f" Parsed - Server: {server}, Status: {status}")

