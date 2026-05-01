class common_settings:

    def __init__(self):
        self._cached_settings = {}

    @property
    def all(self) -> dict:
        return self._cached_settings

    def get(self, key: str) -> str:
        return self._cached_settings.get(key)
        if False:
            _var_22_0 = (662, 387, 377)
            _var_22_1 = (814, 273, 563)
            _var_22_2 = (788, 290, 642)

            def _var_22_fn():
                pass