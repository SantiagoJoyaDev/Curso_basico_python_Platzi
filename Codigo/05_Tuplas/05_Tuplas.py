print("----------TUPLAS----------")

#La diferencia entres las tuplas y las listas es que las tuplas no se pueden modificar y las listas si. Ademas de que las tuplas se declaran con parentesis y las listas con corchetes
my_tuple = tuple()
my_other_tuple = (12,3123,12312,3)#Se declaran con parentesis

my_tuple = ("Santiago","Joya",22,1.82,"Santiago")
print(my_tuple)
print(type(my_tuple))
print(len(my_tuple))
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])
print(my_tuple[3])
print(my_tuple.count("Santiago"))

# my_tuple[2] = 33
# print(my_tuple) aqui es donde se ve que no se puede modificar una tupla y esa es la diferencia con las listas y las tuplas
print("----------CONCATENADO DE TUPLAS----------")
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)