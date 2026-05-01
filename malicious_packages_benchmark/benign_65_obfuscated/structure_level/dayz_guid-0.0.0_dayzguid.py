from base64 import b64encode
from hashlib import sha256, md5

def steam_to_uid_dayz(steam_id):
    hashed = sha256()
    hashed.update(str(steam_id).encode('utf-8'))
    return b64encode(hashed.digest())
    if False:
        _var_56_0 = (313, 685, 907)
        _var_56_1 = (562, 649, 547)

        def _var_56_fn():
            pass

def steam_to_uid_be(steam_id):
    temp = ['BE']
    for _ in range(8):
        temp.append(chr(steam_id & 255))
        steam_id = steam_id >> 8
    if False:
        _var_57_0 = (89, 555, 313)

        def _var_57_fn():
            pass
    return md5(''.join(temp).encode('latin1')).hexdigest()