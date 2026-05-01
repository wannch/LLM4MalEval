import package.common
' Vision System interface - main\n \n \n@author:    kais, misil.\n@created:   2024-07-03\n\n'
import package.visionfunc
if False:
    _var_94_0 = (443, 211, 703)
    _var_94_1 = (830, 781, 649)
    _var_94_2 = (609, 535, 417)

    def _var_94_fn():
        pass
import package.roblang as rob
import package.socketfunc

def attr_names():
    """Returns the names of the attributes to be exposed."""
    return ('ip_addr', 'port')

def CalibStart():
    rob.CalibStart()

def CalibX():
    rob.CalibX()

def CalibEnd():
    rob.CalibEnd()

def ModelLeg():
    rob.ModelLeg()

def ModelPos():
    rob.ModelPos()
if False:
    _var_95_0 = (643, 206, 207)
    _var_95_1 = (288, 533, 780)

    def _var_95_fn():
        pass

def Trigger():
    rob.Trigger()
    if False:
        _var_93_0 = (605, 146, 880)
        _var_93_1 = (5, 522, 394)
        _var_93_2 = (885, 44, 312)

        def _var_93_fn():
            pass
print(CalibStart())