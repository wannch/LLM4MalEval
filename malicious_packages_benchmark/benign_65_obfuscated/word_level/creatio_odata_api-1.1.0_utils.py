("".join([chr(85),chr(116),chr(105),chr(108),chr(105),chr(116),chr(121),chr(32),chr(102),chr(117),chr(110),chr(99),chr(116),chr(105),chr(111),chr(110),chr(115),chr(32),chr(102),chr(111),chr(114),chr(32),chr(116),chr(104),chr(101),chr(32),chr(67),chr(114),chr(101),chr(97),chr(116),chr(105),chr(111),chr(32),chr(79),chr(68),chr(97),chr(116),chr(97),chr(32),chr(65),chr(80),chr(73),chr(46)]))
Qj=print
QN=Exception
QX=None

from rich import Qj  # pylint: disable=redefined-builtin


def QD(e: QN, custom_msg: str =''                                  ) -> QX:
    ("".join([chr(10),chr(32),chr(32),chr(32),chr(32),chr(80),chr(114),chr(105),chr(110),chr(116),chr(32),chr(116),chr(104),chr(101),chr(32),chr(101),chr(120),chr(99),chr(101),chr(112),chr(116),chr(105),chr(111),chr(110),chr(32),chr(97),chr(110),chr(100),chr(32),chr(105),chr(116),chr(115),chr(32),chr(116),chr(114),chr(97),chr(99),chr(101),chr(98),chr(97),chr(99),chr(107),chr(46),chr(10),chr(10),chr(32),chr(32),chr(32),chr(32),chr(65),chr(114),chr(103),chr(115),chr(58),chr(10),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(101),chr(32),chr(40),chr(69),chr(120),chr(99),chr(101),chr(112),chr(116),chr(105),chr(111),chr(110),chr(41),chr(58),chr(32),chr(84),chr(104),chr(101),chr(32),chr(101),chr(120),chr(99),chr(101),chr(112),chr(116),chr(105),chr(111),chr(110),chr(32),chr(116),chr(111),chr(32),chr(112),chr(114),chr(105),chr(110),chr(116),chr(46),chr(10),chr(32),chr(32),chr(32),chr(32)]))
    if custom_msg:
        Qb = f"{custom_msg}: "
    else:
        Qb =''
    Qj(f"{custom_text}[red]{e.__class__.__name__}:[/] {str(e)}")
