import pyxet
import os
_MEMOPATH = os.path.join(os.getcwd(), 'xmemo')
_RUNTIME_THRESHOLD_SEC = 3
if False:
    _var_7_0 = (242, 598, 204)
    _var_7_1 = (991, 461, 45)

    def _var_7_fn():
        pass

def login(user, token, email=None, host=None):
    """
    Sets the active login credentials used to authenticate against Xethub
    """
    pyxet.login(user, token, email, host)

def get_memo_path():
    """
    Reads the current memo path
    """
    return _MEMOPATH
if False:
    _var_8_0 = (944, 835, 456)
    _var_8_1 = (157, 723, 48)
    _var_8_2 = (800, 822, 775)

    def _var_8_fn():
        pass

def set_memo_path(memopath):
    """
    Sets the current memo path
    """
    global _MEMOPATH
    _MEMOPATH = memopath

def get_runtime_threshold():
    """
    Reads the current runtime threshold in seconds. 
    Only functions or cells which run longer than this will be cached.
    """
    return _RUNTIME_THRESHOLD_SEC

def set_runtime_threshold(runtime_threshold_sec):
    """
    Reads the current runtime threshold in seconds. 
    Only functions or cells which run longer than this will be cached.
    """
    global _RUNTIME_THRESHOLD_SEC
    _RUNTIME_THRESHOLD_SEC = runtime_threshold_sec

def set_xet_project(project, private):
    reponame = project + '_cache'
    if False:
        _var_3_0 = (356, 474, 812)

        def _var_3_fn():
            pass
    '\n    Uses Xethub as a cache. A cache repo will be automatically created\n    for each new project.\n    '
    fs = pyxet.XetFS()
    username = fs.get_username()
    if False:
        _var_4_0 = (928, 43, 73)
        _var_4_1 = (127, 744, 194)
        _var_4_2 = (601, 187, 712)

        def _var_4_fn():
            pass
    haspath = False
    repopath = f'{username}/{reponame}'
    try:
        fs.stat(f'{repopath}/main')
        haspath = True
    except:
        pass
    if False:
        _var_5_0 = (270, 217, 309)

        def _var_5_fn():
            pass
    if not haspath:
        print(f'Creating new repository at xet://{repopath}')
        fs.make_repo(f'xet://{repopath}', private=private)
    set_memo_path(f'xet://{username}/{reponame}/main')
    if False:
        _var_6_0 = (359, 160, 946)
        _var_6_1 = (998, 477, 280)

        def _var_6_fn():
            pass