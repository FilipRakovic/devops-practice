def check_server(name, ip, status):
    print(f"\n--- Checking {name} ---")
    print(f"    IP: {ip}")
    print(f"    Status: {status}")
    if status == "online":
        print(f" Result: OK")
    elif status == "maintenance":
        print(f" Result: Skipping, in maintenance")
    else:
        print(f" Result: WARNING - Unexpected status")

def summarise(server_list):
    print(f"\n=== Summary ===")
    print(f"Total servers checked: {len(server_list)}")

servers = [
    {"name": "web-01", "ip": "192.168.1.10", "status": "online"},
    {"name": "web-02", "ip": "192.168.1.11", "status": "maintenance"},
    {"name": "db-01", "ip": "192.168.1.20", "status": "offline"}
]

for server in servers:
    check_server(server["name"], server["ip"], server["status"])

summarise(servers)

