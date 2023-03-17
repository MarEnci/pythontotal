mi_tuple = (1,2,3,4)
t = (5,6.7,'tupapa')
print(type(t))

print(t[1])

t1 = 4,5.6,(8,90)
print(t1[2][1])
t1 = list(t1)
print(type(t1))

print(t1.count(4))
print(t1.index(5.6))

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))

mi_tupla1 = (1, 2, 3, 4)
a, b, c, d = mi_tupla1
print(mi_tupla1)

