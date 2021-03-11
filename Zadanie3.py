# Задание 3
import numpy
import matplotlib.pyplot
from numpy.polynomial import Polynomial as P

# Пункт А
mass = [1, 4, 4, 3]
y = lambda x: (mass[3] * x ** 3 + mass[2] * x ** 2 + mass[1] * x + mass[0])
fig = matplotlib.pyplot.subplots()
x = numpy.linspace(-3, 3, 100)
matplotlib.pyplot.plot(x, y(x))
matplotlib.pyplot.show()

# Пункт B
p = P(mass)
print("Решение полинома: ", p.roots())

# Пункт C
y = lambda x: numpy.sin(x)
y1 = lambda x1: numpy.cos(x1)
fig = matplotlib.pyplot.subplots()
x = numpy.linspace(-3, 3, 100)
x1 = numpy.linspace(-5, 3, 100)
matplotlib.pyplot.plot(x, y(x), x1, y1(x1))
matplotlib.pyplot.show()

# Пункт D
dx = []
dy = []
for i in range(600):
    t = i / 10 * numpy.pi
    dx.append(t * numpy.cos(t))
    dy.append(t * numpy.sin(t))

matplotlib.pyplot.plot(dx, dy)
matplotlib.pyplot.show()

# Пункт Е
circle = numpy.arange(0., 2., 1. / 180.) * numpy.pi
matplotlib.pyplot.polar(circle, 2 - 2 * numpy.sin(circle) + numpy.sin(circle) * numpy.sqrt(
    numpy.abs(numpy.cos(circle) / (numpy.sin(circle) + 1.4))))
matplotlib.pyplot.show()