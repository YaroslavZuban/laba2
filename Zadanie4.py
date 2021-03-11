import matplotlib.pyplot
import numpy
from mpl_toolkits.mplot3d import Axes3D
from numpy.core.function_base import linspace

# Задание А
u, v = numpy.mgrid[0:2 * numpy.pi:20j, 0:numpy.pi:10j]
x = v ** 2 + numpy.sqrt(u)
y = u ** 2 + numpy.sqrt(v)
z = v * u
fig = matplotlib.pyplot.figure()
axes = Axes3D(fig)
axes.plot_surface(x, y, z)
matplotlib.pyplot.show()

# Задание B
matplotlib.pyplot.contour(z)
matplotlib.pyplot.show()

# Задание C
t = linspace(0, 4 * numpy.pi, 100)
x1 = numpy.tan(t)
y1 = numpy.sin(t)
z1 = t / (4 * numpy.pi)
fig1 = matplotlib.pyplot.figure()
ax = Axes3D(fig1)
ax.plot(x1, y1, z1)
matplotlib.pyplot.show()

