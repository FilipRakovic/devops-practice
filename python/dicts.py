server = {
        "name": "web-01",
        "ip": "192.169.1.10",
        "status": "online",
        "cpu_percent": 45
}

print(f"Server name: {server['name']}")
print(f"IP Address: {server['ip']}")
print(f"Status: {server['status']}")

print("\n--- Updating a value ---")
server["status"] = "maintanence"
print(f"New status: {server['status']}")

print("\n--- Adding a new key ---")
server["location"] = "Stockholm"
print(server)

print("\n--- Looping through all keys and values ---")
for key, value in server.items():
    print(f"    {key}: {value}")


