import requests
import time
from datetime import datetime

import os
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
CHECK_INTERVAL_SEC = int(os.getenv('CHECK_INTERVAL'))


def send_telegram_message(message):
    """Send message via Telegram bot."""
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    data = {'chat_id': TELEGRAM_CHAT_ID, 'text': message}
    response = requests.post(url, data=data)
    return response.json()

def get_public_ip():
    """Get the current public IP address."""
    response = requests.get('https://api.ipify.org?format=json')
    ip = response.json()['ip']
    return ip

def monitor_ip_change(interval):
    """Monitor IP changes indefinitely with a specified interval."""
    current_ip = get_public_ip()
    while True:
        time.sleep(interval)
        new_ip = get_public_ip()
        if new_ip != current_ip:
            message = f'IP change detected: {current_ip} to {new_ip}'
            send_telegram_message(message)
            current_ip = new_ip
        else:
            message = f'IP : {current_ip}'
            send_telegram_message(message)

if __name__ == '__main__':
    monitor_ip_change(interval=CHECK_INTERVAL_SEC)  # Monitor IP every 1 hour indefinitely
