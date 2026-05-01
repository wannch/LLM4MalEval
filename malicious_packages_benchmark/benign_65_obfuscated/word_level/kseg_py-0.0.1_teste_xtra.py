import Kseg_new as kseg
yw=kseg.Kseg
import numpy as np
yU=np.concatenate
import matplotlib.pyplot as plt

yT =("".join([chr(70),chr(108),chr(97),chr(109),chr(101),chr(32),chr(78),chr(111),chr(114),chr(109)]))
import scipy.io as sio
df = sio.loadmat(("".join([chr(102),chr(108),chr(97),chr(109),chr(101),chr(95),chr(100),chr(97),chr(116),chr(97),chr(46),chr(109),chr(97),chr(116)]))                                 )
yz = df[("".join([chr(88)]))           ]
yf = df[("".join([chr(121)]))           ]
X = yU((yz, yf), axis =int("".join([chr(49)]))                         )

x = X[int("".join([chr(48)]))       :int("".join([chr(49),chr(48),chr(48),chr(48)]))            ,int("".join([chr(48)]))               :int("".join([chr(50)]))                 ]

fig, ax = plt.subplots(ncols=int("".join([chr(51)]))                              , nrows=int("".join([chr(49)]))                                       ,   dpi =int("".join([chr(55),chr(53)]))                                                   )

yc = yw(int("".join([chr(49)]))         ,int("".join([chr(49)]))            ,int("".join([chr(49)]))               ,int("".join([chr(49),chr(48),chr(48),chr(48)]))                     )
yc.fitCurve(x)
ax[int("".join([chr(48)]))    ].plot(x[:,int("".join([chr(48)]))                ], x[:,int("".join([chr(49)]))                        ],("".join([chr(111)]))                              , label =("".join([chr(32),chr(98),chr(97),chr(115),chr(101),chr(32),chr(100),chr(101),chr(32),chr(100),chr(97),chr(100),chr(111),chr(115)]))                                                        )
yc.plot_curve(ax[int("".join([chr(48)]))                  ])
ax[int("".join([chr(48)]))    ].legend()

yd = yw(int("".join([chr(51)]))         ,int("".join([chr(49)]))            ,int("".join([chr(49)]))               ,int("".join([chr(49),chr(48),chr(48),chr(48)]))                     )
yd.fitCurve(x)
ax[int("".join([chr(49)]))    ].plot(x[:,int("".join([chr(48)]))                ], x[:,int("".join([chr(49)]))                        ],("".join([chr(111)]))                              , label =("".join([chr(32),chr(98),chr(97),chr(115),chr(101),chr(32),chr(100),chr(101),chr(32),chr(100),chr(97),chr(100),chr(111),chr(115)]))                                                        )
yd.plot_curve(ax[int("".join([chr(49)]))                  ])
ax[int("".join([chr(49)]))    ].legend()

ys = yw(int("".join([chr(53)]))         ,int("".join([chr(49)]))            ,int("".join([chr(49)]))               ,int("".join([chr(49),chr(48),chr(48),chr(48)]))                     )
ys.fitCurve(x)
ax[int("".join([chr(50)]))    ].plot(x[:,int("".join([chr(48)]))                ], x[:,int("".join([chr(49)]))                        ],("".join([chr(111)]))                              , label =("".join([chr(32),chr(98),chr(97),chr(115),chr(101),chr(32),chr(100),chr(101),chr(32),chr(100),chr(97),chr(100),chr(111),chr(115)]))                                                        )
ys.plot_curve(ax[int("".join([chr(50)]))                  ])
ax[int("".join([chr(50)]))    ].legend()