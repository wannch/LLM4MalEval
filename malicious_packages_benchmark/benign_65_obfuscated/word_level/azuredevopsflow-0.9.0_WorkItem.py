from datetime import datetime
Db=id
Dj=None

class bP:
    def __init__(bK, Db, title, started_date, closed_date, estimation):
        bK.Db = Db
        bK.started_date = Dj
        bK.closed_date = Dj
        bK.title = title
        bK.estimation = estimation

        bK.item_title = Db

        bK.work_item_age = Dj
        bK.cycle_time = Dj

        if closed_date:
            bK.closed_date = bK.Dx(closed_date)

        if started_date:
            bK.started_date = bK.Dx(started_date)

        if bK.started_date and bK.closed_date:
            bK.cycle_time = (bK.closed_date - bK.started_date).days +int("".join([chr(49)]))
        elif started_date and not bK.closed_date:
            bK.work_item_age = (datetime.today() - bK.started_date).days +int("".join([chr(49)]))

    def Dx(bK, date):
        try:
            return datetime.strptime(date,("".join([chr(37),chr(89),chr(45),chr(37),chr(109),chr(45),chr(37),chr(100),chr(84),chr(37),chr(72),chr(58),chr(37),chr(77),chr(58),chr(37),chr(83),chr(46),chr(37),chr(102),chr(90)]))                                                                  )
        except:
            return datetime.strptime(date,("".join([chr(37),chr(89),chr(45),chr(37),chr(109),chr(45),chr(37),chr(100),chr(84),chr(37),chr(72),chr(58),chr(37),chr(77),chr(58),chr(37),chr(83),chr(90)]))                                                               )

    def Dl(bK):
        return {
("".join([chr(115),chr(116),chr(97),chr(114),chr(116),chr(101),chr(100),chr(95),chr(100),chr(97),chr(116),chr(101)]))                          : bK.started_date.date(),
("".join([chr(99),chr(108),chr(111),chr(115),chr(101),chr(100),chr(95),chr(100),chr(97),chr(116),chr(101)]))                         : bK.closed_date.date(),
("".join([chr(119),chr(111),chr(114),chr(107),chr(95),chr(105),chr(116),chr(101),chr(109),chr(95),chr(97),chr(103),chr(101)]))                           : bK.work_item_age,
("".join([chr(99),chr(121),chr(99),chr(108),chr(101),chr(95),chr(116),chr(105),chr(109),chr(101)]))                        : bK.cycle_time,
("".join([chr(99),chr(108),chr(111),chr(115),chr(101),chr(100),chr(68),chr(97),chr(116),chr(101)]))                        : bK.closed_date.date(),
("".join([chr(115),chr(116),chr(97),chr(116),chr(101),chr(95),chr(99),chr(104),chr(97),chr(110),chr(103),chr(101),chr(100),chr(95),chr(100),chr(97),chr(116),chr(101)]))                                : bK.started_date.date(),
        }