def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params()
print("___________________")
print_params(b = 25)
print_params(c = [1,2,3])
print_params(3,'раза')
print("__________________________________________________")
values_list = [38,'попугаев', False]
values_dict = {'a':'полька', 'b':3, 'c':False}
print_params(*values_list)
print_params(**values_dict)
print("__________________________________________________")
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)



