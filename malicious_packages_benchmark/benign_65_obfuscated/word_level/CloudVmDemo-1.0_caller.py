import json
Nj=None
NX=False
NA=print
NQ=Exception
Ny=str
Nn=ValueError
NJ=True
Nb=json.loads
Nl=json.dumps
import requests
ND=requests.request

def jK(token, api_call_url, method, params=Nj, data=Nj):
    jm = {
("".join([chr(65),chr(117),chr(116),chr(104),chr(111),chr(114),chr(105),chr(122),chr(97),chr(116),chr(105),chr(111),chr(110)]))                       : f'Bearer {token}',
("".join([chr(67),chr(111),chr(110),chr(116),chr(101),chr(110),chr(116),chr(45),chr(84),chr(121),chr(112),chr(101)]))                      :("".join([chr(97),chr(112),chr(112),chr(108),chr(105),chr(99),chr(97),chr(116),chr(105),chr(111),chr(110),chr(47),chr(106),chr(115),chr(111),chr(110)]))                                          ,
("".join([chr(65),chr(99),chr(99),chr(101),chr(112),chr(116)]))                :("".join([chr(97),chr(112),chr(112),chr(108),chr(105),chr(99),chr(97),chr(116),chr(105),chr(111),chr(110),chr(47),chr(106),chr(115),chr(111),chr(110)]))                                    ,
("".join([chr(99),chr(97),chr(99),chr(104),chr(101),chr(45),chr(99),chr(111),chr(110),chr(116),chr(114),chr(111),chr(108)]))                       :("".join([chr(110),chr(111),chr(45),chr(99),chr(97),chr(99),chr(104),chr(101)]))
    }

    try:
        if params is Nj:
            params = {}
        if data is Nj:
            data = {}

        jv = ND(method, api_call_url, headers=jm, params=params, data=Nl(data), verify=NX)

        if jv.ok:

            return jv.text
        else:
            NA(jv.text)
            jq = jP(jv)
            return jq

    except NQ as ex:
        return Ny(ex)

def jP(jv):
    if jv.text:
        ji = Nb(jv.text)
        if("".join([chr(109),chr(101),chr(115),chr(115),chr(97),chr(103),chr(101)]))                     in ji:
            return ji[("".join([chr(109),chr(101),chr(115),chr(115),chr(97),chr(103),chr(101)]))                               ]
        elif("".join([chr(109),chr(101),chr(115),chr(115),chr(97),chr(103),chr(101),chr(95),chr(108),chr(105),chr(115),chr(116)]))                            in ji:
            return ji[("".join([chr(109),chr(101),chr(115),chr(115),chr(97),chr(103),chr(101),chr(95),chr(108),chr(105),chr(115),chr(116)]))                                    ][int("".join([chr(48)]))                                       ][("".join([chr(109),chr(101),chr(115),chr(115),chr(97),chr(103),chr(101)]))                                                  ]
    return("".join([chr(69),chr(114),chr(114),chr(111),chr(114),chr(58),chr(32),chr(83),chr(111),chr(109),chr(101),chr(116),chr(104),chr(105),chr(110),chr(103),chr(32),chr(119),chr(101),chr(110),chr(116),chr(32),chr(119),chr(114),chr(111),chr(110),chr(103),chr(33)]))

def Nx(myjson):
    try:
        Nb(myjson)
    except Nn:
        return NX
    return NJ

