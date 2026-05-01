import os
from azure.kusto.data import KustoConnectionStringBuilder, KustoClient
if False:
    _var_144_0 = (305, 136, 462)
    _var_144_1 = (387, 803, 90)

    def _var_144_fn():
        pass
client = None

def get_client():
    global client
    if False:
        _var_141_0 = (989, 933, 901)
        _var_141_1 = (503, 736, 296)

        def _var_141_fn():
            pass
    if client is not None:
        return client
    if False:
        _var_142_0 = (781, 740, 156)
        _var_142_1 = (152, 671, 133)

        def _var_142_fn():
            pass
    connection = KustoConnectionStringBuilder.with_aad_application_key_authentication(os.getenv('ADX_CLUSTER_URI'), os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'), os.getenv('TENANT_ID'))
    client = KustoClient(connection)
    if False:
        _var_143_0 = (305, 511, 221)

        def _var_143_fn():
            pass
    return client