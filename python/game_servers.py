def game_servers(name, location, status):
    print(f"\n--- Server {name} ---")
    print(f"    Location: {location}")
    print(f"    status: {status}")
    if status == "Online":
        print("This server is operational")
    elif status == "Maintenance":
        print("This server is under Maintenance, back online soon!")
    elif status == "Offline":
        print("This server is currently offline, please try again soon")
    elif status == "Unknown":
        print("Warning, this server is unresponsive, please investigate")



servers = [
        {"name": "Sweden-Server", "location": "Stockholm", "status": "Online"},
        {"name": "England-Server", "location": "London", "status": "Maintenance"},
        {"name": "Germany-Server", "location": "Frankfurt", "status": "Offline"},
        {"name": "USA-Server", "location": "New York", "status": "Offline"},
        {"name": "Japan-Server", "location": "Tokyo", "status": "Unknown"},
        ]

servers.append({"name": "Norway-Server", "location": "Oslo", "status": "Online"},)
servers.remove({"name": "Japan-Server", "location": "Tokyo", "status": "Unknown"},)
x = len(servers)
print(f"Total servers: {x}")

print(f"First server: {servers[0]['name']}")
print(f"Last server: {servers[-1]['name']}")


for index, server in enumerate(servers, start=1):
    print(f"{index}. {server['name']} - {server['location']}")
    game_servers(server["name"], server["location"], server["status"])




