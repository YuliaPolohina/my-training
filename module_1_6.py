my_dict = {'Mama': 123, 'Papa': 456, 'Sister': 789}
print(my_dict)
print(my_dict.get('Mama'))
print(my_dict.get('Brother'))
my_dict.update({'Grandmother': 147,
                'Grandfather': 258})
print(my_dict)
my_dict.pop('Sister')
print(my_dict)
