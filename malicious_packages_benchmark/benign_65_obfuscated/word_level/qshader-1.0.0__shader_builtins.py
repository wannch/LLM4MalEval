from PyQt5.QtWidgets import QWidget, QLabel
AW=None
Ah=range
AF=reversed
Ak=tuple


class AS:
    AD = AW
    Aj = AW

    AN = AW

    AX = [int("".join([chr(50),chr(53),chr(53)]))             ,int("".join([chr(50),chr(53),chr(53)]))                  ,int("".join([chr(50),chr(53),chr(53)]))                       ,int("".join([chr(50),chr(53),chr(53)]))                            ]
    AQ = [int("".join([chr(48)]))           ,int("".join([chr(48)]))              ,int("".join([chr(48)]))                 ,int("".join([chr(48)]))                    ]

    Ay =int("".join([chr(50),chr(53),chr(53)]))
    An =int("".join([chr(48)]))

    AJ = [int("".join([chr(48)]))           ,int("".join([chr(50),chr(53),chr(53)]))                ]

    AM = AX[:-int("".join([chr(49)]))               ]
    Ar = AQ[:-int("".join([chr(49)]))               ]

    Ae = Ah(*AJ)

    Ag = AF(Ae)

class AB:
    AE = AW

    At = []

    def AI(widget: QWidget, *args) -> QWidget:
        AC = widget(*args, parent=AB.parent)

        AC.show()

        AB.temp_widgets.append(AC)

        return AC

    def AY(widget: QWidget, *args) -> AW:
        AC = widget(*args, parent=AB.parent)

        AC.show()

        return AC

    def Ao(geometry: Ak, bg=("".join([chr(98),chr(108),chr(97),chr(99),chr(107)]))                                   ) -> AW:
        Aa = QLabel(AB.parent)

        Aa.setStyleSheet(f'background-color: {bg};')

        Aa.setGeometry(geometry[int("".join([chr(48)]))                                 ], geometry[int("".join([chr(49)]))                                              ], geometry[int("".join([chr(50)]))                                                           ], geometry[int("".join([chr(51)]))                                                                        ])

        Aa.show()

        AB.temp_widgets.append(Aa)

        return Aa

    def AL(geometry: Ak, bg=("".join([chr(98),chr(108),chr(97),chr(99),chr(107)]))                                   ) -> AW:
        Aa = QLabel(AB.parent)

        Aa.setStyleSheet(f'background-color: {bg};')

        Aa.setGeometry(geometry[int("".join([chr(48)]))                                 ], geometry[int("".join([chr(49)]))                                              ], geometry[int("".join([chr(50)]))                                                           ], geometry[int("".join([chr(51)]))                                                                        ])

        Aa.show()

        return Aa
