from pathlib import Path
Xy=True
Xn=print
from PIL import Image

def XQ(src_dir, size=(int("".join([chr(50),chr(48),chr(48)]))                         ,int("".join([chr(50),chr(48),chr(48)]))                              ), out_dir=("".join([chr(116),chr(104),chr(117),chr(109),chr(98),chr(110),chr(97),chr(105),chr(108),chr(115)]))                                                     ):
    Xj = Path(src_dir)
    XN = Xj / out_dir
    XN.mkdir(exist_ok=Xy)
    for p in Xj.iterdir():
        if p.is_file() and p.suffix.lower() in {("".join([chr(46),chr(106),chr(112),chr(103)]))                                                      ,("".join([chr(46),chr(106),chr(112),chr(101),chr(103)]))                                                               ,("".join([chr(46),chr(112),chr(110),chr(103)]))                                                                       ,("".join([chr(46),chr(103),chr(105),chr(102)]))                                                                               ,("".join([chr(46),chr(98),chr(109),chr(112)]))                                                                                       }:
            with Image.open(p) as im:
                im.thumbnail(size)
                XA = XN / p.name
                im.save(XA)
                Xn(("".join([chr(83),chr(97),chr(118),chr(101),chr(100),chr(58)]))                           , XA)