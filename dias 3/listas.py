mi_lista = ['a','b','c']
otra_lista = ['hola',55,6.1]
largo = len(mi_lista)
indice = mi_lista[0:]
print(type(otra_lista))
print(largo)
print(indice)
continuacion = ['d','e']
print(mi_lista+continuacion)
tercer_lista = mi_lista+continuacion
print(tercer_lista)
tercer_lista[0] = 'alfa'
print(tercer_lista)
tercer_lista.append('f')
print(tercer_lista)
print(len(tercer_lista))
tercer_lista.pop()
print(tercer_lista)
tercer_lista.pop(0)
print(tercer_lista)
eliminados = tercer_lista.pop(0)+tercer_lista.pop()
print(eliminados)

lista1 = ['x','m','p','q']
lista1.sort()
print(lista1)

lista1.reverse()
print(lista1)
