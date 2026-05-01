# Copyright (C) 2024 RomanLabs, Rafael Roman Otero
Nz=None
Nf=str
Nc=int
# This file is part of API Pipe.
#
# API Pipe is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# API Pipe is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with API Pipe. If not, see <http://www.gnu.org/licenses/>.

("".join([chr(10),chr(32),chr(32),chr(32),chr(32),chr(108),chr(111),chr(103),chr(103),chr(101),chr(114),chr(46),chr(112),chr(121),chr(10)]))
import logging
NT=logging.Formatter
NO=logging.Logger
from rich.logging import RichHandler
from rich.traceback import install

from minishell import config

def Nh() -> Nz:
    ("".join([chr(10),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(69),chr(110),chr(97),chr(98),chr(108),chr(101),chr(32),chr(80),chr(114),chr(101),chr(116),chr(116),chr(121),chr(32),chr(84),chr(114),chr(97),chr(99),chr(101),chr(98),chr(97),chr(99),chr(107),chr(10),chr(10),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(85),chr(115),chr(101),chr(115),chr(32),chr(114),chr(105),chr(99),chr(104),chr(32),chr(116),chr(111),chr(32),chr(112),chr(114),chr(105),chr(110),chr(116),chr(32),chr(112),chr(114),chr(101),chr(116),chr(116),chr(121),chr(32),chr(116),chr(114),chr(97),chr(99),chr(101),chr(98),chr(97),chr(99),chr(107),chr(115),chr(10),chr(32),chr(32),chr(32),chr(32)]))
    install()

def NF(name: Nf, log_level: Nc) -> NO:
    ("".join([chr(10),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(83),chr(101),chr(116),chr(115),chr(32),chr(117),chr(112),chr(32),chr(97),chr(32),chr(108),chr(111),chr(103),chr(103),chr(101),chr(114),chr(32),chr(116),chr(104),chr(97),chr(116),chr(32),chr(108),chr(111),chr(103),chr(115),chr(32),chr(116),chr(111),chr(32),chr(115),chr(116),chr(100),chr(111),chr(117),chr(116),chr(10),chr(10),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(85),chr(115),chr(101),chr(115),chr(32),chr(82),chr(105),chr(99),chr(104),chr(72),chr(97),chr(110),chr(100),chr(108),chr(101),chr(114),chr(32),chr(116),chr(111),chr(32),chr(112),chr(114),chr(101),chr(116),chr(116),chr(121),chr(32),chr(112),chr(114),chr(105),chr(110),chr(116),chr(32),chr(108),chr(111),chr(103),chr(115),chr(10),chr(32),chr(32),chr(32),chr(32)]))
    NI = config.log_words_to_highlight

    NY = RichHandler(
        show_time=config.log_show_time,
        keywords=[w.lower() for w in NI] +                 [w.upper() for w in NI] +                 [w.capitalize() for w in NI]
    )

    No = NW(name)
    No.setLevel(log_level)
    NL = NT(config.log_formatter)
    NY.setFormatter(NL)
    No.addHandler(NY)

    return No

class NW(NO):
    ("".join([chr(10),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(69),chr(120),chr(116),chr(101),chr(110),chr(100),chr(115),chr(32),chr(116),chr(104),chr(101),chr(32),chr(108),chr(111),chr(103),chr(103),chr(105),chr(110),chr(103),chr(46),chr(76),chr(111),chr(103),chr(103),chr(101),chr(114),chr(32),chr(99),chr(108),chr(97),chr(115),chr(115),chr(10),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(119),chr(105),chr(116),chr(104),chr(32),chr(32),chr(99),chr(117),chr(115),chr(116),chr(111),chr(109),chr(32),chr(109),chr(101),chr(116),chr(104),chr(111),chr(100),chr(115),chr(10),chr(32),chr(32),chr(32),chr(32)]))
    def Nk(self) -> Nz:
        ("".join([chr(10),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(70),chr(108),chr(117),chr(115),chr(104),chr(10),chr(10),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(70),chr(108),chr(117),chr(115),chr(104),chr(101),chr(115),chr(32),chr(116),chr(104),chr(101),chr(32),chr(108),chr(111),chr(103),chr(103),chr(101),chr(114),chr(10),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32),chr(32)]))
        for NY in self.handlers:
            NY.Nk()

