import matplotlib.pyplot as plt
import autograd.numpy as np

from Algorithms.Function import beale_function
from Algorithms.FunctionsConst import BEALE_FUNCTION_CONST
from matplotlib.colors import LogNorm



def plot_function():
    f  = lambda x, y: (1.5 - x + x*y)**2 + (2.25 - x + x*y**2)**2 + (2.625 - x + x*y**3)**2

    xmin, xmax, xstep = BEALE_FUNCTION_CONST
    ymin, ymax, ystep = BEALE_FUNCTION_CONST

    x, y = np.meshgrid(np.arange(xmin, xmax + xstep, xstep), np.arange(ymin, ymax + ystep, ystep))
    z = beale_function(x, y)
    minima = np.array([3., .5])
    f(*minima)
    minima_ = minima.reshape(-1, 1)
    minima_
    f(*minima_)
    fig = plt.figure(figsize=(8, 5))
    ax = plt.axes(projection='3d', elev=50, azim=-50)

    ax.plot_surface(x, y, z, norm=LogNorm(), rstride=1, cstride=1,
                    edgecolor='none', alpha=.8, cmap=plt.cm.jet)
    ax.plot(*minima_, f(*minima_), 'r*', markersize=10)

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$z$')

    ax.set_xlim((xmin, xmax))
    ax.set_ylim((ymin, ymax))

    plt.show()
