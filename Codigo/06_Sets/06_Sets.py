print("----------SETS----------")

#Los sets son conjuntos de datos que no tienen un orden y no se pueden repetir los datos
my_set = set()
my_other_set = {"Santiago","Joya",22,1.82,"Santiago"}#Se declaran con llaves

print(my_other_set)
print(type(my_other_set))
print(len(my_other_set))
#print(my_other_set[0])#No se puede acceder a los elementos de un set por indice
my_other_set.add("Python")#Se agrega un elemento al set
print(my_other_set)#Un set no es una estructura ordenada
print(len(my_other_set))

print("----------OPERACIONES CON SETS----------")
print("Santiago" in my_other_set)#Se puede verificar si un elemento esta en el set
print("Santiago" not in my_other_set)#Se puede verificar si un elemento no esta en el set
my_other_set.add("LA LA LA")#Se agrega un elemento al set
my_other_set.clear()#Se limpia el set
print(my_other_set)

print("----------CONCATENACION DE SETS----------")
my_set = {1,2,3,4,5}
my_other_set = {6,7,8,9,10}
my_set.update(my_other_set)#Se concatenan los sets
print(my_set)
my_both_sets = my_set.union(my_other_set)#Se concatenan los sets
print(my_both_sets)
#my_both_sets1 = my_set + my_other_set#No se pueden concatenar sets de esta manera