import os

log_file = "server_logs.txt"

print("--- Writing logs ---")
with open(log_file, "w") as f:
    f.write("web-01 status: online\n")
    f.write("web-02 status: maintenance\n")
    f.write("db-01 status: offline\n")
    f.write("db-02 status: online\n")
print(f"Wrote logs to {log_file}")

print("\n--- Reading entire file ---")
with open(log_file, "r") as f:
    content = f.read()
print(content)

print("--- reading line by line ---")
with open(log_file, "r") as f:
    for line in f:
        line = line.strip()
        if "offline" in line:
            print(f" WARNING: {line}")
        elif "maintenance" in line:
            print(f" NOTICE: {line}")
        else:
            print(f"    OK: {line}")

print("\n--- Appending a new log ---")
with open(log_file, "a") as f:
    f.write("cache-01 status: online\n")

print("\n--- File info ---")
size = os.path.getsize(log_file)
print(f"Log File Size: {size} bytes")
print(f"File exists: {os.path.exists(log_file)}")

print("\n--- Parsing log values ---")
with open(log_file, "r") as f:
    for line in f:
        line = line.strip()
        parts = line.split(" status: ")
        server = parts[0]
        status = parts[1]
        print(f"Server: {server:<12} Status: {status}")

