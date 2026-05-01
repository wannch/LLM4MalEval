import argparse
ya=len
yS=open
yB=reversed
yI=list
yY=IOError
yo=print
yE=argparse.ArgumentParser
import re
yC=re.DOTALL
yt=re.finditer


def yr(yQ, max_length):
    ("".join([chr(81),chr(117),chr(101),chr(98),chr(114),chr(97),chr(32),chr(117),chr(109),chr(97),chr(32),chr(250),chr(110),chr(105),chr(99),chr(97),chr(32),chr(108),chr(105),chr(110),chr(104),chr(97),chr(32),chr(113),chr(117),chr(101),chr(32),chr(101),chr(120),chr(99),chr(101),chr(100),chr(101),chr(32),chr(111),chr(32),chr(108),chr(105),chr(109),chr(105),chr(116),chr(101),chr(32),chr(100),chr(101),chr(32),chr(99),chr(111),chr(109),chr(112),chr(114),chr(105),chr(109),chr(101),chr(110),chr(116),chr(111),chr(46)]))
    if ya(yQ) <= max_length:
        return [yQ]
    else:
        # Encontra um espaço próximo ao limite de comprimento para quebrar a linha
        QP = yQ.rfind(("".join([chr(32)]))                         ,int("".join([chr(48)]))                            , max_length)
        if QP == -int("".join([chr(49)]))                   :  # Caso não encontre um espaço adequado
            QP = max_length
        return [yQ[:QP]] + yr(
            yQ[QP:].lstrip(), max_length
        )


def ye(input_file, max_line_length=int("".join([chr(55),chr(57)]))                                     ):
    ("".join([chr(10),chr(32),chr(32),chr(32),chr(32),chr(70),chr(111),chr(114),chr(109),chr(97),chr(116),chr(97),chr(32),chr(97),chr(115),chr(32),chr(97),chr(115),chr(112),chr(97),chr(115),chr(32),chr(116),chr(114),chr(105),chr(112),chr(108),chr(97),chr(115),chr(32),chr(101),chr(109),chr(32),chr(117),chr(109),chr(32),chr(97),chr(114),chr(113),chr(117),chr(105),chr(118),chr(111),chr(32),chr(80),chr(121),chr(116),chr(104),chr(111),chr(110),chr(32),chr(112),chr(97),chr(114),chr(97),chr(32),chr(113),chr(117),chr(101),chr(32),chr(111),chr(32),chr(116),chr(101),chr(120),chr(116),chr(111),chr(32),chr(99),chr(111),chr(109),chr(101),chr(99),chr(101),chr(32),chr(105),chr(109),chr(101),chr(100),chr(105),chr(97),chr(116),chr(97),chr(109),chr(101),chr(110),chr(116),chr(101),chr(10),chr(32),chr(32),chr(32),chr(32),chr(97),chr(112),chr(243),chr(115),chr(32),chr(97),chr(115),chr(32),chr(97),chr(115),chr(112),chr(97),chr(115),chr(32),chr(116),chr(114),chr(105),chr(112),chr(108),chr(97),chr(115),chr(32),chr(100),chr(101),chr(32),chr(97),chr(98),chr(101),chr(114),chr(116),chr(117),chr(114),chr(97),chr(32),chr(101),chr(32),chr(116),chr(101),chr(114),chr(109),chr(105),chr(110),chr(101),chr(32),chr(110),chr(97),chr(32),chr(108),chr(105),chr(110),chr(104),chr(97),chr(32),chr(97),chr(110),chr(116),chr(101),chr(114),chr(105),chr(111),chr(114),chr(32),chr(224),chr(115),chr(32),chr(97),chr(115),chr(112),chr(97),chr(115),chr(32),chr(116),chr(114),chr(105),chr(112),chr(108),chr(97),chr(115),chr(32),chr(100),chr(101),chr(32),chr(102),chr(101),chr(99),chr(104),chr(97),chr(109),chr(101),chr(110),chr(116),chr(111),chr(46),chr(10),chr(32),chr(32),chr(32),chr(32)]))
    try:
        with yS(input_file,("".join([chr(114)]))                               ) as f:
            yx = f.read()

        yl =("".join([chr(40),chr(34),chr(34),chr(34),chr(46),chr(42),chr(63),chr(34),chr(34),chr(34),chr(41)]))
        yb = yt(yl, yx, yC)

        for yD in yB(yI(yb)):
            yj = yD.group(int("".join([chr(48)]))                           )
            yN = yj[
int("".join([chr(51)]))                 :-int("".join([chr(51)]))
            ].strip()  # Remove as aspas triplas e espaços extras
            yX = yN.split(("".join([chr(10)]))                              )  # Separa o texto em linhas
            yA = []

            for yQ in yX:
                yA.extend(yr(yQ, max_line_length))

            yn =("".join([chr(34),chr(34),chr(34),chr(10)]))                         +("".join([chr(10)]))                               .join(yA) +("".join([chr(10),chr(34),chr(34),chr(34)]))
            yx = yx[: yD.start()] + yn + yx[yD.end() :]

        with yS(input_file,("".join([chr(119)]))                               ) as f:
            f.write(yx)

    except yY as e:
        yo(f"Erro ao abrir o arquivo: {e}")


def yg():
    yJ = yE(
        description=("".join([chr(70),chr(111),chr(114),chr(109),chr(97),chr(116),chr(97),chr(32),chr(97),chr(115),chr(32),chr(97),chr(115),chr(112),chr(97),chr(115),chr(32),chr(116),chr(114),chr(105),chr(112),chr(108),chr(97),chr(115),chr(32),chr(101),chr(109),chr(32),chr(117),chr(109),chr(32),chr(97),chr(114),chr(113),chr(117),chr(105),chr(118),chr(111),chr(32),chr(80),chr(121),chr(116),chr(104),chr(111),chr(110),chr(46)]))
    )
    yJ.add_argument(("".join([chr(105),chr(110),chr(112),chr(117),chr(116),chr(95),chr(102),chr(105),chr(108),chr(101)]))                                , help=("".join([chr(78),chr(111),chr(109),chr(101),chr(32),chr(100),chr(111),chr(32),chr(97),chr(114),chr(113),chr(117),chr(105),chr(118),chr(111),chr(32),chr(80),chr(121),chr(116),chr(104),chr(111),chr(110),chr(32),chr(97),chr(32),chr(115),chr(101),chr(114),chr(32),chr(102),chr(111),chr(114),chr(109),chr(97),chr(116),chr(97),chr(100),chr(111),chr(46)]))                                                                                )
    yM = yJ.parse_args()
    ye(yM.input_file)


if __name__ ==("".join([chr(95),chr(95),chr(109),chr(97),chr(105),chr(110),chr(95),chr(95)]))                         :
    yg()
