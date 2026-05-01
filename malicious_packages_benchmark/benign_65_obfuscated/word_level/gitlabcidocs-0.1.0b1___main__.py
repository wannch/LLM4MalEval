import sys
li=str
lK=False
lP=True
lH=sys.path
import pathlib
lR=pathlib.Path
lH.insert(int("".join([chr(48)]))           , li(lR(__file__).resolve().parent))

import argparse
lv=argparse.ArgumentParser
import docsgen
lq=docsgen.create_docs


def lm():
    lu = lv()
    lu.add_argument(("".join([chr(45),chr(45),chr(105),chr(110),chr(99),chr(108),chr(117),chr(100),chr(101),chr(45),chr(97),chr(108),chr(108),chr(45),chr(114),chr(117),chr(108),chr(101),chr(115)]))                                         , required=lK, default=lP, action=("".join([chr(115),chr(116),chr(111),chr(114),chr(101),chr(95),chr(116),chr(114),chr(117),chr(101)]))                                                                                       , help=("".join([chr(73),chr(102),chr(32),chr(116),chr(114),chr(117),chr(101),chr(44),chr(32),chr(100),chr(111),chr(99),chr(117),chr(109),chr(101),chr(110),chr(116),chr(32),chr(97),chr(108),chr(108),chr(32),chr(119),chr(111),chr(114),chr(107),chr(102),chr(108),chr(111),chr(119),chr(32),chr(114),chr(117),chr(108),chr(101),chr(115),chr(46),chr(32),chr(79),chr(116),chr(104),chr(101),chr(114),chr(119),chr(105),chr(115),chr(101),chr(32),chr(111),chr(110),chr(108),chr(121),chr(32),chr(114),chr(117),chr(108),chr(101),chr(115),chr(32),chr(119),chr(105),chr(116),chr(104),chr(32),chr(36),chr(67),chr(73),chr(95),chr(80),chr(73),chr(80),chr(69),chr(76),chr(73),chr(78),chr(69),chr(95),chr(83),chr(79),chr(85),chr(82),chr(67),chr(69),chr(61),chr(119),chr(101),chr(98),chr(124),chr(112),chr(105),chr(112),chr(101),chr(108),chr(105),chr(110),chr(101),chr(124),chr(97),chr(112),chr(105),chr(32),chr(97),chr(114),chr(101),chr(32),chr(105),chr(110),chr(99),chr(108),chr(117),chr(100),chr(101),chr(100)]))                                                                                                                                                                                                                 )
    lu.add_argument(("".join([chr(45),chr(45),chr(99),chr(105),chr(45),chr(102),chr(105),chr(108),chr(101)]))                               , required=lK, default=("".join([chr(46),chr(103),chr(105),chr(116),chr(108),chr(97),chr(98),chr(45),chr(99),chr(105),chr(46),chr(121),chr(109),chr(108)]))                                                                      , help=("".join([chr(80),chr(97),chr(116),chr(104),chr(32),chr(116),chr(111),chr(32),chr(103),chr(105),chr(116),chr(108),chr(97),chr(98),chr(45),chr(99),chr(105),chr(46),chr(121),chr(109),chr(108)]))                                                                                                    )
    lu.add_argument(("".join([chr(45),chr(45),chr(100),chr(111),chr(99),chr(45),chr(102),chr(105),chr(108),chr(101)]))                                , required=lK, default=("".join([chr(82),chr(69),chr(65),chr(68),chr(77),chr(69),chr(46),chr(109),chr(100)]))                                                                  , help=("".join([chr(80),chr(97),chr(116),chr(104),chr(32),chr(116),chr(111),chr(32),chr(116),chr(104),chr(101),chr(32),chr(102),chr(105),chr(108),chr(101),chr(32),chr(105),chr(110),chr(32),chr(116),chr(104),chr(101),chr(32),chr(100),chr(111),chr(99),chr(115),chr(32),chr(97),chr(114),chr(101),chr(32),chr(105),chr(110),chr(106),chr(101),chr(99),chr(116),chr(101),chr(100),chr(32),chr(116),chr(111)]))                                                                                                                       )
    return lu.parse_args()


if __name__ ==("".join([chr(95),chr(95),chr(109),chr(97),chr(105),chr(110),chr(95),chr(95)]))                         :
    lp = lm()

    lq(lp.ci_file, lp.doc_file, lp.include_all_rules)
