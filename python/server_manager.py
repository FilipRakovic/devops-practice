def server_lookup(name, ip, status):
    print(f"\n--- Server {name} ---")
    print(f"    IP: {ip}")
    print(f"    Status:{status}")
    if status == "online":
          print(f" Server is online")
    elif status == "offline":
          print(f" Warning! Server is offline")



servers = [
    {"name": "server1", "ip": "192.168.1.10", "status": "online"},
    {"name": "server2", "ip": "192.168.1.20", "status": "offline"},
    {"name": "server3", "ip": "192.168.1.30", "status": "offline"},
    {"name": "server4", "ip": "192.168.1.40", "status": "online"},
]

online_count = 0
offline_count = 0



for server in servers:
    server_lookup(server["name"], server["ip"], server["status"])
    if server["status"] == "online":
        online_count +=1
    elif server["status"] == "offline":
        offline_count +=1



print(f"Online servers: {online_count}")
print(f"Offline servers: {offline_count}")





