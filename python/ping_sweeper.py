import subprocess

alive_ping = []
dead_ping = []

base_ip = "192.168.203."

for i in range(1, 255):
    ip = base_ip + str(i)
    print(ip)
    result = subprocess.run(
            ["ping", "-c", "1", "-W", "1", ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
    )
    result = result.returncode == 0
    if result == True: 
        alive_ping.append(ip)
    else:
        dead_ping.append(ip)

print(f"Alive hosts: {len(alive_ping)}")
print(f"Dead hosts: {len(dead_ping)}")
print(f"\nAlive hosts:")
for ip in alive_ping:
    print(f"    {ip}")


