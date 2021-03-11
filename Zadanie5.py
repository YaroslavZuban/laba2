from sympy import *

x, y = symbols('x y')
print("Нахождение производной: ")
print(diff(sin(x) + 0.5 * x ** 5))
print("Нахождение интегралла: ")
print(integrate(sin(x) + 0.5 * x ** 5))

from PIL import Image, ImageDraw

im = Image.new('RGB', (300, 100), color=('#FFFFFF'))
draw_text = ImageDraw.Draw(im)
draw_text.text((50, 50), 'sin(x) + 0.5 * x ** 5  ', fill='#1C0606')
im.show()
