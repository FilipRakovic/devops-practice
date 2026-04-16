#!/bin/bash
# System report script - Written by Filip

NAME="DevOps VM"
DISK_USAGE=$(df -h / | awk 'NR==2 {print $5}')
DISK_NUM=$(echo $DISK_USAGE | tr -d '%')

echo "=== System Report: $NAME ==="
echo "Date: $(date)"
echo "Uptime: $(uptime -p)"
echo "Logged in as: $(whoami)"
echo "IP Address: $(hostname -I)"
echo "Disk usage: $DISK_USAGE"

if [ "$DISK_NUM" -gt 80 ]; then
    echo "WARNING: Disk usage is high!"
else
    echo "Disk usage is fine."
fi

echo ""
echo "=== Checking Connectivity ==="
for HOST in google.com github.com azure.microsoft.com; do
    if ping -c 1 -W 1 $HOST &> /dev/null; then
        echo "$HOST is reachable"
    else
        echo "$HOST is UNREACHABLE"
    fi
done
