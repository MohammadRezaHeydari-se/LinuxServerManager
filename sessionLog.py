"""
This class is used for recording session.
Every action should be recorded by add function to the list.
List will be added to the json file when the session of ssh connection would be close.
"""

import json
from datetime import datetime

# Class sessionlogger is use for recording evere sesstion into a json file 
class SessionLogger:
    def __init__(self):
        # Sesstion list
        self.records = []

    def add(self, message: str):
        # Adding a action to loger session 
        ts = datetime.now().isoformat(timespec='seconds')
        self.records.append({ts: message})

    def close(self, filename="log/session_log.json"):
        # Recording our loger session into a jeson file
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.records, f, ensure_ascii=False, indent=4)