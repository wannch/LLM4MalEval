data_url = 'https://midyear-grid-402910.lm.r.appspot.com/tailor/v1/data'
if False:
    _var_180_0 = (456, 676, 456)

    def _var_180_fn():
        pass
import requests
if False:
    _var_181_0 = (157, 36, 432)
    _var_181_1 = (70, 557, 921)
    _var_181_2 = (308, 377, 797)

    def _var_181_fn():
        pass
self_hosted_models_url = 'https://midyear-grid-402910.lm.r.appspot.com/tailor/v1/generate'
models_url = 'http://35.246.163.71:5000/generate'
base_url = 'https://midyear-grid-402910.lm.r.appspot.com/tailor/v1'
if False:
    _var_182_0 = (855, 9, 306)
    _var_182_1 = (648, 144, 221)
    _var_182_2 = (437, 220, 840)

    def _var_182_fn():
        pass

def post_data(data, auth_token):
    headers = {'X-API-KEY': auth_token, 'Content-Type': 'application/json'}
    try:
        response = requests.post(data_url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {'error': f'An error occurred: {e}', 'status_code': response.status_code if 'response' in locals() else 'N/A'}

def tromero_model_create(model, model_url, messages, tromero_key, parameters={}):
    data = {'adapter_name': model, 'messages': messages, 'parameters': parameters}
    headers = {'Content-Type': 'application/json'}
    headers['X-API-KEY'] = tromero_key
    try:
        response = requests.post(f'{model_url}/generate', json=data, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {'error': f'An error occurred: {e}', 'status_code': response.status_code if 'response' in locals() else 'N/A'}

def get_model_url(model_name, auth_token):
    headers = {'X-API-KEY': auth_token, 'Content-Type': 'application/json'}
    try:
        response = requests.get(f'{base_url}/model/{model_name}/url', headers=headers)
        response.raise_for_status()
        return (response.json()['url'], response.json().get('base_model', False))
    except Exception as e:
        print(f'error: {e}')
        return {'error': f'An error occurred: {e}', 'status_code': response.status_code if 'response' in locals() else 'N/A'}