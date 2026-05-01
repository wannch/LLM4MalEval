import re
Qi=int
QK=print
Qq=re.findall
from collections import Counter
from pathlib import Path

def Qv(filepath, top_n=int("".join([chr(50),chr(48)]))                         ):
    QG = Path(filepath).read_text(encoding=("".join([chr(117),chr(116),chr(102),chr(45),chr(56)]))                                                  , errors=("".join([chr(105),chr(103),chr(110),chr(111),chr(114),chr(101)]))                                                                   )
    Qu = Qq(("".join([chr(92),chr(98),chr(91),chr(97),chr(45),chr(122),chr(65),chr(45),chr(90),chr(39),chr(93),chr(43),chr(92),chr(98)]))                             , QG.lower())
    Qp = Counter(Qu)
    return Qp.most_common(top_n)

if __name__ ==("".join([chr(95),chr(95),chr(109),chr(97),chr(105),chr(110),chr(95),chr(95)]))                         :
    import argparse
    Qm = argparse.ArgumentParser(description=("".join([chr(83),chr(104),chr(111),chr(119),chr(32),chr(116),chr(111),chr(112),chr(32),chr(78),chr(32),chr(119),chr(111),chr(114),chr(100),chr(115),chr(32),chr(105),chr(110),chr(32),chr(97),chr(32),chr(116),chr(101),chr(120),chr(116),chr(32),chr(102),chr(105),chr(108),chr(101)]))                                                                              )
    Qm.add_argument(("".join([chr(102),chr(105),chr(108),chr(101)]))                          , help=("".join([chr(80),chr(97),chr(116),chr(104),chr(32),chr(116),chr(111),chr(32),chr(116),chr(101),chr(120),chr(116),chr(32),chr(102),chr(105),chr(108),chr(101)]))                                                    )
    Qm.add_argument(("".join([chr(45),chr(45),chr(116),chr(111),chr(112)]))                           , type=Qi, default=int("".join([chr(50),chr(48)]))                                                , help=("".join([chr(72),chr(111),chr(119),chr(32),chr(109),chr(97),chr(110),chr(121),chr(32),chr(116),chr(111),chr(112),chr(32),chr(119),chr(111),chr(114),chr(100),chr(115),chr(32),chr(116),chr(111),chr(32),chr(115),chr(104),chr(111),chr(119)]))                                                                                   )
    QH = Qm.parse_args()

    for QR, cnt in Qv(QH.file, QH.top):
        QK(f"{word:20} {cnt}")
