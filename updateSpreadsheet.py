import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import re

# Google Sheets credentials & vars
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_file('/root/googleKey.json', scopes=scope)
client = gspread.authorize(creds)

sheet_id = '11CWcGyV95sPi0MO0ZD6NK40mFsUF_zXoSS443JVm-o8'
sheet = client.open_by_key(sheet_id).worksheet('miner1')

def extract_data(log_line):
    timestamp_match = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', log_line)
    stake_match = re.search(r'Stake: ([\d.]+)', log_line)

    if stake_match:
        timestamp = timestamp_match.group()
        stake = float(stake_match.group(1))
        incentive_match = re.search(r'Incentive: ([\d.]+)', log_line)
        trust_match = re.search(r'Trust: ([\d.]+)', log_line)

        if incentive_match:
            incentive = float(incentive_match.group(1))
        else:
            incentive = None

        if trust_match:
            trust = float(trust_match.group(1))
        else:
            trust = None

        return timestamp, stake, incentive, trust
    else:
        return None, None, None, None

def write_to_sheet():
    with open('/root/logs/minerData.log', 'r') as f:
        logs = f.readlines()
        latest_log = logs[-2]  # Assuming the latest log is at the end of the file
        timestamp, stake, incentive, trust = extract_data(latest_log)
        sheet.append_row([timestamp, stake, incentive, trust])

# Schedule the job to run every hour, at 20 past the hour
scheduler = BlockingScheduler()
scheduler.add_job(write_to_sheet, 'cron', minute=20, hour='*')
scheduler.start()

#write_to_sheet()