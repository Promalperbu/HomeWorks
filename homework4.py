immutable_var = 1, 'go', 54, 'glot'
print(immutable_var)
#immutable_var [0] = 67# картеж нельзя изменить
#immutable_var.append ('jerty') # картеж нельзя изменить
print(immutable_var)
mutable_list = [1, 'go', 54, 'glot']
print(mutable_list)
mutable_list[0] = 67
mutable_list.append ('jerty')
print(mutable_list)