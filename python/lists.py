servers = ["web-01", "web-02", "db-01", "db-03"]

print(f"Totalt servers: {len(servers)}")
print(f"First server: {servers[0]}")
print(f"Last server: {servers[-1]}")

print ("\n--- Looping through all servers ---")
for server in servers:
    print(f" Pinging {server}...")

print("\n--- Adding a new server ---")
servers.append("cache-01")
print(servers)

print("\n--- Removing a server ---")
servers.remove("db-03")
print(servers)



