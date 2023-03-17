diccionario = {'c1':'valor1','c2':'valor'}
print(type(diccionario))
print(diccionario)

resultado = diccionario['c1']
print(resultado)

cliente = {'edad':'33', 'nombre':'jesus','peso':70,'talla':7.2}
consulta = cliente['peso']
print(consulta)

dic = {'c10':45,'c20':[10,20,30],'c30':{'s1':100,'s2':300}}
print(dic['c20'][1])
print(dic['c30']['s2'])

dic1 = {'c1':['a','b','c'],'c2':['d','e','f']}
print(dic1['c2'][1].upper())

dic2 = {1:'a',2:'b'}
dic2[3] = 'c'
print(dic2)

dic2[2] = 'B'

print(dic2)

print(dic2.keys())
print(dic2.values())
print(dic2.items())

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic['pais'] = 'Colombia'
mi_dic['edad'] = 36
mi_dic["ocupacion"] = 'Editora'
print(mi_dic)