import numpy
import pandas

# Задание 2


array = [int(x.replace('\n', '')) for word in open('Книга1.csv') for x in word.split(';')]

arrayDuo = numpy.reshape(array, (5, -1))
print("Двухмерная матрица:\n", arrayDuo, "\n")

arrayDuo_inv = numpy.linalg.inv(arrayDuo)
print(arrayDuo_inv, "\n")

numpy.savetxt('Ответ.csv', arrayDuo_inv, delimiter=';')
print(pandas.read_csv('Ответ.csv', index_col=0, comment='#'))
