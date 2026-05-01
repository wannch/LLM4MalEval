from hashlib import sha256, md5
bv=str
bq=range
bi=chr
from base64 import b64encode

# Steam To Dayz GUID
def bH(bm):
    bu = sha256()
    bu.update(bv(bm).encode(("".join([chr(117),chr(116),chr(102),chr(45),chr(56)]))                                   ))

    return b64encode(bu.digest())


# Steam ID BE GUID
def bR(bm):
    bp = [("".join([chr(66),chr(69)]))              ]
    for _ in bq(int("".join([chr(56)]))                 ):
        bp.append(bi(bm &int("".join([chr(48),chr(120),chr(70),chr(70)]))                              ))
        bm = bm >>int("".join([chr(56)]))

    return md5(''                 .join(bp).encode(("".join([chr(108),chr(97),chr(116),chr(105),chr(110),chr(49)]))                                          )).hexdigest()