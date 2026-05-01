from azure.kusto.data import KustoConnectionStringBuilder, KustoClient
QM=None
import os
QJ=os.getenv

QA = QM


def Qn():
    global QA

    if QA is not QM:
        return QA

    Qy = KustoConnectionStringBuilder.with_aad_application_key_authentication(
        QJ(("".join([chr(65),chr(68),chr(88),chr(95),chr(67),chr(76),chr(85),chr(83),chr(84),chr(69),chr(82),chr(95),chr(85),chr(82),chr(73)]))                            ),
        QJ(("".join([chr(67),chr(76),chr(73),chr(69),chr(78),chr(84),chr(95),chr(73),chr(68)]))                      ),
        QJ(("".join([chr(67),chr(76),chr(73),chr(69),chr(78),chr(84),chr(95),chr(83),chr(69),chr(67),chr(82),chr(69),chr(84)]))                          ),
        QJ(("".join([chr(84),chr(69),chr(78),chr(65),chr(78),chr(84),chr(95),chr(73),chr(68)]))                      ),
    )
    QA = KustoClient(Qy)

    return QA
