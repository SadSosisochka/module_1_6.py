my_dict={'хомячки':123,'кошки':456,'собаки':890}
print(my_dict)
print(my_dict.get('кошки','совы'))
my_dict.update({'рыбки':456,'улитки':678})
print(my_dict)
a=my_dict.pop('рыбки')
print(a)
print(my_dict.items())

my_set={1,5,2,2,1,5,6,'5'}
print(my_set)
print(my_set.add(8))
print(my_set.add(9))
print(my_set)
print(my_set.remove(1))
print(my_set)