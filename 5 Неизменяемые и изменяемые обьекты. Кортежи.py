immutable_var = tuple = 1, 0.5, True, 'Hello'
print(type(immutable_var))  # вывела на печать тип данных
print(immutable_var)
# immutable_var[0] = 2  # кортеж не поддерживает обращение по элементам, неизменяемый тип данных
# print(immutable_var)
mutable_list = [1, 0.5, True, 'Hello']
print(type(mutable_list))  # вывела на печать тип данных
print(mutable_list)
mutable_list[0] = 5  # список поддерживает обращение по элементам, изменяемый тип данных
print(mutable_list)
