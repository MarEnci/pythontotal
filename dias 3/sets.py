mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)

repetidos = set([1,2,3,4,5,1,1,(6,7,8),1,1,2,2,2,])
print(repetidos)

set1 = {1,2,3,4,6,7,7}
print(len(set1))

print(2 in set1)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

ss = {1,2,3}
ss.add(4)
print(ss)

ss.remove(4)
print(ss)

ss.discard(1)
print(ss)

ss.pop()
print(ss)

ss.clear()
print(ss)

mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
mi_set_3 = mi_set_1.union(mi_set_2)
print(mi_set_3)
