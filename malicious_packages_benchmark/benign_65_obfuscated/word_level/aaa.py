import json
QY=False
Qo=enumerate
QL=print
QW=len
Qh=True
QI=json.dumps
QB=json.loads
from pathlib import Path

DB = Path(("".join([chr(116),chr(111),chr(100),chr(111),chr(115),chr(46),chr(106),chr(115),chr(111),chr(110)]))                      )

def Qg():
    if DB.exists():
        return QB(DB.read_text(encoding=("".join([chr(117),chr(116),chr(102),chr(45),chr(56)]))                                               ))
    return []

def QE(Qr):
    DB.write_text(QI(Qr, indent=int("".join([chr(50)]))                                 ), encoding=("".join([chr(117),chr(116),chr(102),chr(45),chr(56)]))                                                    )

def Qt(text):
    Qr = Qg()
    Qr.append({("".join([chr(116),chr(97),chr(115),chr(107)]))                     : text,("".join([chr(100),chr(111),chr(110),chr(101)]))                                   : QY})
    QE(Qr)

def QC():
    for i, t in Qo(Qg(),int("".join([chr(49)]))                          ):
        Qe =("".join([chr(10003)]))                 if t.get(("".join([chr(100),chr(111),chr(110),chr(101)]))                                ) else("".join([chr(32)]))
        QL(f"{i}. [{mark}] {t.get('task')}")

def Qa(index):
    Qr = Qg()
    ifint("".join([chr(49)]))         <= index <= QW(Qr):
        Qr.pop(index -int("".join([chr(49)]))                        )
        QE(Qr)

def QS(index):
    Qr = Qg()
    ifint("".join([chr(49)]))         <= index <= QW(Qr):
        Qr[index -int("".join([chr(49)]))                    ][("".join([chr(100),chr(111),chr(110),chr(101)]))                            ] = Qh
        QE(Qr)