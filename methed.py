

my_list=[10,20,30,40,50]
my_list.append(60)
print(my_list)
my_list.clear()
print(type(my_list))
y=my_list
print(y)

my_list.remove(10)
print(my_list)
y=my_list.copy
print(y)
print(id(my_list))
print(id(y))
print(my_list.count(10))
print(my_list)

my_list1=[70,80]
my_list1.extend(my_list)
print(my_list1)
print(my_list)


my=[10,20,30,40,50]
print(my.insert(3,100))



