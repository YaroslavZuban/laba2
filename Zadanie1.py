import numpy
from numpy import array

# Пункт 1
print("Матрица размером 3*3:")
A = array([[1, 2, 3], [2, 3, 6], [1, 3, 6]])
print(A, "\n")

print("Вектор свободных коэффициентов:")
b = array([[13], [23], [22]])
print(b, "\n")

# Пункт 2
x = numpy.linalg.solve(A, b)
print("Решение системы ли-нейных уравнений Ax = b: \n", x, "\n")

# Пункт 3
check = numpy.dot(numpy.linalg.inv(A), b)
print("Правильности решения путём подстановки: \n", check - x, "\n")
