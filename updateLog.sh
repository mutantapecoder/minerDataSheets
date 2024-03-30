#!/bin/bash

#setup pm2 as a background process
(pm2 logs --lines 100 | grep -i "stake" >/root/logs/minerData.log) &

sleep 3

# Terminate background process
kill $!

exit
