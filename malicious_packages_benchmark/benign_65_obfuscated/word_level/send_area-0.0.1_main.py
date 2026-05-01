from math import pi, sqrt
bC=round
ba=False
bS=range
bB=True
bI=print

class bg:
    def bE(self, radius):
        return bC(radius * pi,int("".join([chr(50)]))                                )
    def bt(self, a, b, c):
        p = (a + b + c) //int("".join([chr(50)]))
        br = sqrt(p*(p-a)*(p-b)*(p-c))
        be = ba
        for a in bS(int("".join([chr(51)]))                     ):
            for b in bS(int("".join([chr(51)]))                         ):
                for c in bS(int("".join([chr(51)]))                             ):
                    if a **int("".join([chr(50)]))                              == b **int("".join([chr(50)]))                                        + c **int("".join([chr(50)]))                                                :
                        be = bB
                    else:
                        continue
        bI(be)
        return br
