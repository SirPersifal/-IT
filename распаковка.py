def print_params (a = 1 , b = 'строка' , c = True ):
    print(a , b , c)

print_params()
print_params('Doctor who born in Earth' , 10 , False)
print_params(b = 25)
print_params(c = [1 , 2 , 3])

value_list = [4 , 'ever' , True]
value_dict = {'a' : 3 , 'b' : 2 , 'c' : 1}
print_params(*value_list)
print_params(**value_dict)

value_list2 = [22.5 , 'Диагональ']
print_params(*value_list2 , 'ноутбука')

