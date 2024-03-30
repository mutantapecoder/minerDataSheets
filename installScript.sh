#!/bin/bash

# Make the script executable
# chmod +x "$0"

# Install required Python packages
pip install apscheduler
pip install google-auth
pip install gspread oauth2client

# Create directories
mkdir -p /root/logs /root/scripts

# Create minerData.log file
touch /root/logs/minerData.log

# Move files to scripts folder
mv /root/minerDataSheets/updateLog.sh /root/scripts/
mv /root/minerDataSheets/updateSpreadsheet.py /root/scripts/

# Exit the script
exit 0
