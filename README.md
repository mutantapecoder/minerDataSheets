# Miner Data for Google Sheets

- run `git clone https://github.com/mutantapecoder/minerDataSheets.git` in root of VM

- cd into minerDataSheets folder

- `chmod u+x installScript.sh` and run installScript.sh to get started.

- cd scripts folder

- run updateLogs.sh manually once so that log file has data in it

- crontab -e and delete comments in file and add `*/15 * * * * /root/scripts/updateLog.sh`

- nano updateSpreadsheet.py and change documentID and worksheet name

- in scripts folder run `pm2 start ./updateSpreadsheet.py --name GOOGLESHEETS --watch`
