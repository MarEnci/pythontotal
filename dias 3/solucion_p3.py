texto = input("Escribe un texto cualquiera: ")
letras = []

texto = texto.lower()

letras.append(input('Ingresa una letra cualquiera: ').lower())
letras.append(input('Ingresa otra letra: ').lower())
letras.append(input('Ingresa una ultima letra: ').lower())

print('\n')
print('CANTIDAD DE LETRAS')
cantidad_letras = texto.count(letras[0])
cantidad_letras1 = texto.count(letras[1])
cantidad_letras2 = texto.count(letras[2])

print(f'Hemos encontrado la letra {letras[0]} repetida {cantidad_letras} veces')
print(f'Hemos encontrado la letra {letras[1]} repetida {cantidad_letras1} veces')
print(f'Hemos encontrado la letra {letras[2]} repetida {cantidad_letras2} veces')

print('\n')
print('CANTIDAD DE PALABRAS')
palabras = texto.split()
print(f'Hemos encontrado {len(palabras)} palabras en tu texto')

print('\n')
print('LETRAS DE INICIO Y DE FIN')
letra_inicio = texto[0]
letras_final = texto[-1]
print(f'La letra inicial es "{letra_inicio}" y la letra final es "{letras_final}"')

print('\n')
print('TEXTO INVERTIDO')
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f'Si ordenamos tu texto al reves sera: "{texto_invertido}"')

print('\n')
print('BUSCANDO LA PALABRA PYTHON')
bucar_python = 'python' in texto
dic = {True:'si', False:'no'}
print(f'La palabra "python" {dic[bucar_python]} se encuentra en el texto.')