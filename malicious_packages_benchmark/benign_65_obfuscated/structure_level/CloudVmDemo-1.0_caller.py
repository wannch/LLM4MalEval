import requests
import json

def caller(token, api_call_url, method, params=None, data=None):
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json', 'Accept': 'application/json', 'cache-control': 'no-cache'}
    try:
        if params is None:
            params = {}
        if data is None:
            data = {}
        api_response = requests.request(method, api_call_url, headers=headers, params=params, data=json.dumps(data), verify=False)
        if api_response.ok:
            return api_response.text
        else:
            print(api_response.text)
            error_msg = get_error_message(api_response)
            return error_msg
    except Exception as ex:
        return str(ex)

def get_error_message(api_response):
    if api_response.text:
        error_data = json.loads(api_response.text)
        if 'message' in error_data:
            return error_data['message']
        elif 'message_list' in error_data:
            return error_data['message_list'][0]['message']
    return 'Error: Something went wrong!'
    if False:
        _var_92_0 = (423, 426, 938)
        _var_92_1 = (587, 123, 688)
        _var_92_2 = (841, 120, 393)

        def _var_92_fn():
            pass

def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True