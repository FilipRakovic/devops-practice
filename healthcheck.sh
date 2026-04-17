#!/bin/bash
#
#==========================
# Server Health Check Script
# Author: Filip
#==========================
#
#
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'
echo "================================"
echo "   Server Health Check"
echo "   $(date)"
echo "================================"
echo ""

 #--- CPU Load ---
CPU_LOAD=$(top -bn1 | grep "load average" | awk '{print $12}' | tr -d ',')
echo "CPU Load (1 min avg): $CPU_LOAD"

 #--- Memory ---
MEM_TOTAL=$(free -m | awk 'NR==2{print $2}')
MEM_USED=$(free -m | awk 'NR==2{print $3}')
MEM_PERCENT=$(( MEM_USED * 100 / MEM_TOTAL ))

if [ $MEM_PERCENT -gt 85 ]; then
    echo -e "Memory Usage: ${RED}${MEM_PERCENT}% - WARNING${NC}"
elif [ $MEM_PERCENT -gt 60 ]; then
    echo -e "Memory Usage: ${YELLOW}${MEM_PERCENT}% - MODERATE${NC}"
else
    echo -e "Memory Usage: ${GREEN}${MEM_PERCENT}% - OK${NC}"
fi

# --- Disk ---
DISK_USAGE=$(df -h / | awk 'NR==2{print $5}' | tr -d '%')

if [ $DISK_USAGE -gt 85 ]; then
    echo -e "Disk Usage: ${RED}${DISK_USAGE}% - WARNING${NC}"
elif [ $DISK_USAGE -gt 60 ]; then
    echo -e "Disk Usage: ${YELLOW}${DISK_USAGE}% - MODERATE${NC}"
else
    echo -e "Disk Usage: ${GREEN}${DISK_USAGE}% - OK${NC}"
fi

# --- Connectivity ---
echo ""
echo "--- Connectivity ---"
for HOST in google.com github.com azure.microsoft.com; do
    if ping -c 1 -W 1 $HOST &> /dev/null; then
        echo -e "$HOST: ${GREEN}REACHABLE${NC}"
    else
        echo -e "$HOST: ${RED}UNREACHABLE${NC}"
    fi
done

# --- Top 3 processes by CPU ---
echo ""
echo "--- Top 3 Processes by CPU ---"
ps aux --sort=-%cpu | awk 'NR==2,NR==4{print $1, $2, $3"%", $11}'

echo ""
echo "================================"
echo "   Health check complete"
echo "================================"

