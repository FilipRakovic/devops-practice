import subprocess
import json

def get_vm_status(resource_group, vm_name):
    result = subprocess.run(
            ["az", "vm", "get-instance-view",
             "--resource-group", resource_group,
             "--name", vm_name,
             "--query", "instanceView.statuses[1].displayStatus",
             "--output", "json"],
            capture_output=True,
            text=True
    )
    status = result.stdout.strip().replace('"', '')
    return status

def get_vm_ip(resource_group, vm_name):
    result = subprocess.run(
            ["az", "vm", "list-ip-addresses",
             "--resource-group", resource_group,
             "--name", vm_name,
             "--output", "json"],
            capture_output=True,
            text=True
    )
    data = json.loads(result.stdout)
    public_ip = data[0]["virtualMachine"]["network"]["publicIpAddresses"][0]["ipAddress"]
    return public_ip

def monitor_vm(resource_group, vm_name):
    print(f"\n=== Azure VM Monitor ===")
    print(f"Resource Group: {resource_group}")
    print(f"VM Name: {vm_name}")

    status = get_vm_status(resource_group, vm_name)
    ip = get_vm_ip(resource_group, vm_name)

    print(f"Status: {status}")
    print(f"Public IP: {ip}")

    if status == "VM running":
        print("Health: OK")
    else:
        print(f"Health: WARNING - VM is {status}")

monitor_vm("devops-lab", "devops-vm")

