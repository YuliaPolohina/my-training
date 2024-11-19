immutable_var = 5, 6, 7, True, "Rabbit"
print(immutable_var)
#immutable_var[0] = 100 #элемент внутри кортежа неизменяем из-за разных типов данных в спике
#print(immutable_var)
mutable_list =  5, 7, 8
print(mutable_list)
mutable_list = ([5, 6], 7)
print(mutable_list)
mutable_list[0][0] = 8
print(mutable_list)
