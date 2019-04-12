#!/bin/bash
PATH=$PATH:/usr/sbin

set -e

if [ "$1" = "start" ]; then
  exec python /data/main.py
elif [ "$1" = "query" ]; then
  exec python /data/api.py
elif [ "$1" = "-b" ]; then
  exec /bin/bash
elif [ "$1" = "-t" ]; then
  (cd /data ; pytest -p no:warnings)
fi
