import requests
JN=Exception
JX=locals
JA=False
JQ=print
Jj=requests.get
JD=requests.post

nH =("".join([chr(104),chr(116),chr(116),chr(112),chr(115),chr(58),chr(47),chr(47),chr(109),chr(105),chr(100),chr(121),chr(101),chr(97),chr(114),chr(45),chr(103),chr(114),chr(105),chr(100),chr(45),chr(52),chr(48),chr(50),chr(57),chr(49),chr(48),chr(46),chr(108),chr(109),chr(46),chr(114),chr(46),chr(97),chr(112),chr(112),chr(115),chr(112),chr(111),chr(116),chr(46),chr(99),chr(111),chr(109),chr(47),chr(116),chr(97),chr(105),chr(108),chr(111),chr(114),chr(47),chr(118),chr(49),chr(47),chr(100),chr(97),chr(116),chr(97)]))
nR =("".join([chr(104),chr(116),chr(116),chr(112),chr(58),chr(47),chr(47),chr(51),chr(53),chr(46),chr(50),chr(52),chr(54),chr(46),chr(49),chr(54),chr(51),chr(46),chr(55),chr(49),chr(58),chr(53),chr(48),chr(48),chr(48),chr(47),chr(103),chr(101),chr(110),chr(101),chr(114),chr(97),chr(116),chr(101)]))
nv =("".join([chr(104),chr(116),chr(116),chr(112),chr(115),chr(58),chr(47),chr(47),chr(109),chr(105),chr(100),chr(121),chr(101),chr(97),chr(114),chr(45),chr(103),chr(114),chr(105),chr(100),chr(45),chr(52),chr(48),chr(50),chr(57),chr(49),chr(48),chr(46),chr(108),chr(109),chr(46),chr(114),chr(46),chr(97),chr(112),chr(112),chr(115),chr(112),chr(111),chr(116),chr(46),chr(99),chr(111),chr(109),chr(47),chr(116),chr(97),chr(105),chr(108),chr(111),chr(114),chr(47),chr(118),chr(49),chr(47),chr(103),chr(101),chr(110),chr(101),chr(114),chr(97),chr(116),chr(101)]))
nq =("".join([chr(104),chr(116),chr(116),chr(112),chr(115),chr(58),chr(47),chr(47),chr(109),chr(105),chr(100),chr(121),chr(101),chr(97),chr(114),chr(45),chr(103),chr(114),chr(105),chr(100),chr(45),chr(52),chr(48),chr(50),chr(57),chr(49),chr(48),chr(46),chr(108),chr(109),chr(46),chr(114),chr(46),chr(97),chr(112),chr(112),chr(115),chr(112),chr(111),chr(116),chr(46),chr(99),chr(111),chr(109),chr(47),chr(116),chr(97),chr(105),chr(108),chr(111),chr(114),chr(47),chr(118),chr(49)]))

def Jx(nP, auth_token):
    ni = {
("".join([chr(88),chr(45),chr(65),chr(80),chr(73),chr(45),chr(75),chr(69),chr(89)]))                   : auth_token,
("".join([chr(67),chr(111),chr(110),chr(116),chr(101),chr(110),chr(116),chr(45),chr(84),chr(121),chr(112),chr(101)]))                      :("".join([chr(97),chr(112),chr(112),chr(108),chr(105),chr(99),chr(97),chr(116),chr(105),chr(111),chr(110),chr(47),chr(106),chr(115),chr(111),chr(110)]))
    }
    try:
        nK = JD(nH, json=nP, headers=ni)
        nK.raise_for_status()  # Raises HTTPError for bad responses (4XX, 5XX)
        return nK.json()  # Return the JSON response if request was successful
    except JN as e:
        return {("".join([chr(101),chr(114),chr(114),chr(111),chr(114)]))                       : f'An error occurred: {e}',("".join([chr(115),chr(116),chr(97),chr(116),chr(117),chr(115),chr(95),chr(99),chr(111),chr(100),chr(101)]))                                                                 : nK.status_code if("".join([chr(114),chr(101),chr(115),chr(112),chr(111),chr(110),chr(115),chr(101)]))                                                                                                in JX() else("".join([chr(78),chr(47),chr(65)]))                                                                                                                  }


def Jl(model, model_url, messages, tromero_key, parameters={}):
    ni = {("".join([chr(67),chr(111),chr(110),chr(116),chr(101),chr(110),chr(116),chr(45),chr(84),chr(121),chr(112),chr(101)]))                        :("".join([chr(97),chr(112),chr(112),chr(108),chr(105),chr(99),chr(97),chr(116),chr(105),chr(111),chr(110),chr(47),chr(106),chr(115),chr(111),chr(110)]))                                            }
    nP = {
("".join([chr(97),chr(100),chr(97),chr(112),chr(116),chr(101),chr(114),chr(95),chr(110),chr(97),chr(109),chr(101)]))                      : model,
("".join([chr(109),chr(101),chr(115),chr(115),chr(97),chr(103),chr(101),chr(115)]))                  : messages,
("".join([chr(112),chr(97),chr(114),chr(97),chr(109),chr(101),chr(116),chr(101),chr(114),chr(115)]))                    : parameters
    }
    ni[("".join([chr(88),chr(45),chr(65),chr(80),chr(73),chr(45),chr(75),chr(69),chr(89)]))                  ] = tromero_key
    try:
        nK = JD(f"{model_url}/generate", json=nP, headers=ni)
        nK.raise_for_status()  # Raises HTTPError for bad responses (4XX, 5XX)
        return nK.json()  # Return the JSON response if request was successful
    except JN as e:
        return {("".join([chr(101),chr(114),chr(114),chr(111),chr(114)]))                       : f'An error occurred: {e}',("".join([chr(115),chr(116),chr(97),chr(116),chr(117),chr(115),chr(95),chr(99),chr(111),chr(100),chr(101)]))                                                                 : nK.status_code if("".join([chr(114),chr(101),chr(115),chr(112),chr(111),chr(110),chr(115),chr(101)]))                                                                                                in JX() else("".join([chr(78),chr(47),chr(65)]))                                                                                                                  }


def Jb(model_name, auth_token):
    ni = {
("".join([chr(88),chr(45),chr(65),chr(80),chr(73),chr(45),chr(75),chr(69),chr(89)]))                   : auth_token,
("".join([chr(67),chr(111),chr(110),chr(116),chr(101),chr(110),chr(116),chr(45),chr(84),chr(121),chr(112),chr(101)]))                      :("".join([chr(97),chr(112),chr(112),chr(108),chr(105),chr(99),chr(97),chr(116),chr(105),chr(111),chr(110),chr(47),chr(106),chr(115),chr(111),chr(110)]))
    }
    try:
        nK = Jj(f"{base_url}/model/{model_name}/url", headers=ni)
        nK.raise_for_status()  # Raises HTTPError for bad responses (4XX, 5XX)
        return nK.json()[("".join([chr(117),chr(114),chr(108)]))                              ], nK.json().get(("".join([chr(98),chr(97),chr(115),chr(101),chr(95),chr(109),chr(111),chr(100),chr(101),chr(108)]))                                                           , JA)  # Return the JSON response if request was successful
    except JN as e:
        JQ(f"error: {e}")
        return {("".join([chr(101),chr(114),chr(114),chr(111),chr(114)]))                       : f'An error occurred: {e}',("".join([chr(115),chr(116),chr(97),chr(116),chr(117),chr(115),chr(95),chr(99),chr(111),chr(100),chr(101)]))                                                                 : nK.status_code if("".join([chr(114),chr(101),chr(115),chr(112),chr(111),chr(110),chr(115),chr(101)]))                                                                                                in JX() else("".join([chr(78),chr(47),chr(65)]))                                                                                                                  }







