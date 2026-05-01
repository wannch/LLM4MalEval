import matplotlib as mpl
jV=mpl.rcParams
jU=mpl.font_manager


def jd(font_path):
    ("".join([chr(83),chr(101),chr(116),chr(32),chr(102),chr(111),chr(110),chr(116),chr(115),chr(32),chr(102),chr(111),chr(114),chr(32),chr(109),chr(97),chr(116),chr(112),chr(108),chr(111),chr(116),chr(108),chr(105),chr(98),chr(32),chr(112),chr(108),chr(111),chr(116),chr(115),chr(10),chr(10),chr(32),chr(32),chr(32),chr(32),chr(65),chr(114),chr(103),chr(115),chr(58),chr(10),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(102),chr(111),chr(110),chr(116),chr(95),chr(112),chr(97),chr(116),chr(104),chr(32),chr(40),chr(115),chr(116),chr(114),chr(41),chr(58),chr(32),chr(112),chr(97),chr(116),chr(104),chr(32),chr(116),chr(111),chr(32),chr(46),chr(116),chr(105),chr(102),chr(102),chr(32),chr(102),chr(111),chr(110),chr(116),chr(10),chr(32),chr(32),chr(32),chr(32)]))
    jz = jU.FontEntry(fname=font_path, name=("".join([chr(109),chr(121),chr(95),chr(102),chr(111),chr(110),chr(116)]))                                                     )
    jU.fontManager.ttflist.append(jz)

    jV.update(
        {
("".join([chr(102),chr(111),chr(110),chr(116),chr(46),chr(102),chr(97),chr(109),chr(105),chr(108),chr(121)]))                         : jz.name,
        }
    )


def js():
    ("".join([chr(115),chr(101),chr(116),chr(32),chr(114),chr(101),chr(116),chr(105),chr(110),chr(97),chr(32),chr(100),chr(105),chr(115),chr(112),chr(108),chr(97),chr(121),chr(32),chr(115),chr(117),chr(112),chr(112),chr(111),chr(114),chr(116),chr(32),chr(105),chr(110),chr(32),chr(73),chr(80),chr(121),chr(116),chr(104),chr(111),chr(110),chr(32),chr(110),chr(111),chr(116),chr(101),chr(98),chr(111),chr(111),chr(107),chr(115),chr(10),chr(32),chr(32),chr(32),chr(32)]))
    from IPython import get_ipython

    get_ipython().run_line_magic(("".join([chr(109),chr(97),chr(116),chr(112),chr(108),chr(111),chr(116),chr(108),chr(105),chr(98)]))                                             ,("".join([chr(105),chr(110),chr(108),chr(105),chr(110),chr(101)]))                                                       )
    from IPython.display import set_matplotlib_formats

    set_matplotlib_formats(("".join([chr(114),chr(101),chr(116),chr(105),chr(110),chr(97)]))                                   )


def jw(subplots=(int("".join([chr(49)]))                  ,int("".join([chr(49)]))                     )):
    ("".join([chr(83),chr(101),chr(116),chr(32),chr(115),chr(105),chr(122),chr(101),chr(32),chr(102),chr(111),chr(114),chr(32),chr(115),chr(117),chr(98),chr(112),chr(108),chr(111),chr(116),chr(115),chr(10),chr(10),chr(32),chr(32),chr(32),chr(32),chr(65),chr(114),chr(103),chr(115),chr(58),chr(10),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(115),chr(117),chr(98),chr(112),chr(108),chr(111),chr(116),chr(115),chr(32),chr(40),chr(116),chr(117),chr(112),chr(108),chr(101),chr(44),chr(32),chr(111),chr(112),chr(116),chr(105),chr(111),chr(110),chr(97),chr(108),chr(41),chr(58),chr(32),chr(110),chr(117),chr(109),chr(98),chr(101),chr(114),chr(32),chr(111),chr(102),chr(32),chr(40),chr(114),chr(111),chr(119),chr(44),chr(99),chr(111),chr(108),chr(41),chr(32),chr(115),chr(117),chr(98),chr(112),chr(108),chr(111),chr(116),chr(115),chr(46),chr(32),chr(68),chr(101),chr(102),chr(97),chr(117),chr(108),chr(116),chr(115),chr(32),chr(116),chr(111),chr(32),chr(40),chr(49),chr(44),chr(32),chr(49),chr(41),chr(46),chr(10),chr(10),chr(32),chr(32),chr(32),chr(32),chr(82),chr(101),chr(116),chr(117),chr(114),chr(110),chr(115),chr(58),chr(10),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(116),chr(117),chr(112),chr(108),chr(101),chr(58),chr(32),chr(115),chr(105),chr(122),chr(101),chr(32),chr(111),chr(102),chr(32),chr(115),chr(117),chr(98),chr(112),chr(108),chr(111),chr(116),chr(115),chr(10),chr(32),chr(32),chr(32),chr(32)]))

    jf = jV[("".join([chr(102),chr(105),chr(103),chr(117),chr(114),chr(101),chr(46),chr(102),chr(105),chr(103),chr(115),chr(105),chr(122),chr(101)]))                            ][int("".join([chr(48)]))                               ]
    jc = jV[("".join([chr(102),chr(105),chr(103),chr(117),chr(114),chr(101),chr(46),chr(102),chr(105),chr(103),chr(115),chr(105),chr(122),chr(101)]))                            ][int("".join([chr(49)]))                               ] * (subplots[int("".join([chr(48)]))                                              ] / subplots[int("".join([chr(49)]))                                                            ])

    return (jf, jc)
