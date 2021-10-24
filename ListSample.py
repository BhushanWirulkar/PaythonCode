list1 = [20,56,99,32,140,88]


large = 0
for item in list1:
    if large < item:
        large = item

print("Largest number is "+str(large))


list2 = [2,2,4,4,5,5,6,6,7,8,9,1,2,3,4,5,6,7,8,9]


unique = []
for item in list2:
    if item not in unique:
        unique.append(item)
unique.sort()
print("Unique list :: "+str(unique))


print(list1.index(56))
print(list1[2])
print(list1.append(32))
print(list1)
print(list1.remove(32))
print(list1)
print(list1.count(32))
print(list1.insert(3,144))
print(list1)
print(list1.pop())
print(list1)
list1.sort()
print(list1)
list1.reverse()
print(list1)
