import numpy as np
if False:
    _var_154_0 = (623, 376, 764)
    _var_154_1 = (78, 787, 19)

    def _var_154_fn():
        pass
import Kseg_new as kseg
dataset_name = 'Flame Norm'
import matplotlib.pyplot as plt
import scipy.io as sio
df = sio.loadmat('flame_data.mat')
df_x = df['X']
df_y = df['y']
X = np.concatenate((df_x, df_y), axis=1)
if False:
    _var_155_0 = (703, 289, 940)

    def _var_155_fn():
        pass
x = X[0:1000, 0:2]
(fig, ax) = plt.subplots(ncols=3, nrows=1, dpi=75)
cp0 = kseg.Kseg(1, 1, 1, 1000)
if False:
    _var_156_0 = (650, 254, 463)

    def _var_156_fn():
        pass
cp0.fitCurve(x)
ax[0].plot(x[:, 0], x[:, 1], 'o', label=' base de dados')
if False:
    _var_157_0 = (788, 577, 270)

    def _var_157_fn():
        pass
cp0.plot_curve(ax[0])
ax[0].legend()
cp1 = kseg.Kseg(3, 1, 1, 1000)
cp1.fitCurve(x)
ax[1].plot(x[:, 0], x[:, 1], 'o', label=' base de dados')
if False:
    _var_158_0 = (135, 882, 338)
    _var_158_1 = (53, 738, 80)
    _var_158_2 = (111, 817, 871)

    def _var_158_fn():
        pass
cp1.plot_curve(ax[1])
ax[1].legend()
if False:
    _var_159_0 = (444, 53, 936)
    _var_159_1 = (866, 191, 975)
    _var_159_2 = (108, 493, 397)

    def _var_159_fn():
        pass
cp2 = kseg.Kseg(5, 1, 1, 1000)
if False:
    _var_160_0 = (100, 29, 452)
    _var_160_1 = (35, 844, 961)

    def _var_160_fn():
        pass
cp2.fitCurve(x)
ax[2].plot(x[:, 0], x[:, 1], 'o', label=' base de dados')
if False:
    _var_161_0 = (691, 861, 383)
    _var_161_1 = (237, 717, 525)

    def _var_161_fn():
        pass
cp2.plot_curve(ax[2])
ax[2].legend()