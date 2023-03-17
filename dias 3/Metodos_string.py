frase = 'Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar'
print(frase.upper())
print(frase[6].upper())
print(frase.lower())
print(frase[0].lower())
print(frase.split())
print(frase.split('e'))
print(frase.find('ú'))
print(frase.replace('escritura enteramente en mayúsculas','exclamación'))

a = 'sisas'
b = 'capo'
c = 'saya'
d = 'man'
e =' '.join([a,b,c,d])
print(e)
print(e[::-1])

lista_palabras = ["La","legibilidad","cuenta."]
print(' '.join(lista_palabras))

fragmento = 'Si la implementación es difícil de explicar, puede que sea una mala idea.'
print(fragmento.replace('difícil','fácil').replace('mala','buena'))