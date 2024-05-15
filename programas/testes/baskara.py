# Equações do segundo grau
# -*- coding: utf-8 -*-
a = 1
b = 21
c = 73,5
x1 = ( -b + (b ** 2 - 4 * a * c) ** (0.5)) / (2 * a) 
x2 = ( -b - (b ** 2 - 4 * a * c) ** (0.5)) / (2 * a)
if (b ** 2 - 4 * a * c) < 0:
	print("a equação não tem solução real")
else:
	print(x1, ',', x2)
