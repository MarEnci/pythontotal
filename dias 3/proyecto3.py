texto = input('Introduce un texto cualquiera... ').lower()
letras = input('acontinuacion escribe una letra ').lower()
letra1 = input('Escribe otra ').lower()
letra2 = input('Una mas ').lower()
var1 = list(texto)
var3 = var1.count(letras)
var4 = var1.count(letra1)
var5 = var1.count(letra2)
resultado1 = (var3,var4,var5)
print('Este es el numero de veces que encontramos tus letras en el texto, respectivamente.')
print(resultado1)

print('\n')
print('CANTIDAD DE PALABRAS')
cantidad_palabras = texto.split()
print(f'tu texto tiene {len(cantidad_palabras)} palabras.')

print('\n')
print('TEXTO AL REVÉS')
cantidad_palabras.reverse()
texto_invertido = ' '.join(cantidad_palabras)
print(texto_invertido)

print('\n')
print('PRIEMRA Y ULTIMA LETRA DEL TEXTO')
letra_inicio = texto[0]
letra_fianal = texto[-1]
print(f'La primera letra de tu texto es "{letra_inicio}" y la ultima es "{letra_fianal}"')

print('\n')
print('Está la palabra python dentro de tu texto?')
palabra = 'python' in texto
dic = {True:'si',False:'no'}
print(f'La palabra "python" {dic[palabra]} esta en el texto')












