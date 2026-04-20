#!/bin/bash
#
#=========================
# Log Cleanup Script
# Author: Filip
#
LOG_DIR=~/devops-practice/fake_logs
ARCHIVE_DIR=~/devops-practice/archives
SCRIPT_LOG=~/devops-practice/cleanup.log
DAYS_DELETE=7
DAYS_ARCHIVE=30

echo "================================" >> $SCRIPT_LOG
echo "Log cleanup started: $(date)" >> $SCRIPT_LOG
echo "================================" >> $SCRIPT_LOG

# --- Step 1: Create directories if the don't exist ---
mkdir -p $LOG_DIR
mkdir -p $ARCHIVE_DIR

# --- Step 2: Delete files older than 7 days ---
echo "Archiving files older than $DAYS_ARCHIVE days..." >> $SCRIPT_LOG
find $LOG_DIR -mtime +$DAYS_ARCHIVE -type f | while read FILE; do
	mv "$FILE" $ARCHIVE_DIR/
	echo "Archived: $FILE" >> $SCRIPT_LOG
done


# --- Step 3: Archive files older than 30 days ---
echo "Deleting files older than $DAYS_DELETE days..." >> $SCRIPT_LOG
find $LOG_DIR -mtime +$DAYS_DELETE -type f | while read FILE; do
	rm "$FILE"
	echo "Deleted: $FILE" >> $SCRIPT_LOG
done


# --- Step 4: Report what was done ---
REMAINING=$(find $LOG_DIR -type f | wc -l)
ARCHIVED=$(find $ARCHIVE_DIR -type f | wc -l)

echo "Files remaining in log dir: $REMAINING" >> $SCRIPT_LOG
echo "Files in archive: $ARCHIVED" >> $SCRIPT_LOG
echo "Cleanup complete: $(date)" >> $SCRIPT_LOG

#Also print in Terminal
echo "============================"
echo "Log cleanup complete"
echo "Remaining logs: $REMAINING"
echo "Archived logs: $ARCHIVED"
echo "Full log: $SCRIPT_LOG"
echo "============================"
