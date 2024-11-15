my_list = []
#append the values
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#insert 15 at the second position
my_list.insert(1,15)

#extend my_list with another list
my_list2 = [50,60,70]
my_list.extend(my_list2)

#remove the last element from my_list
my_list.pop(-1)

#sort my_list in ascending order
my_list.sort()

#find and print the index of the value 30 in my_list
print(my_list.index(30))


print(my_list)