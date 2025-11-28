list = [1,2,3,4,5]

list[1] = 11

list.append(6)

list.insert(3, 12)

list.remove(4)

#for item in list:
 #   print(item)

x = 0

list3 = [1,2,3,4,5,6,7,8,9]

list2 =sorted(list, reverse=True)

list2.extend(list3)


sets = {1,2,3,4,5,2,3,4,4}
sets2 = {4,5,6,7,8}

a = sets.union(sets2)
b = sets.intersection(sets2)
c = sets.difference(sets2)

print(a)
print(b)
print(c)

sets.add(6)
sets.remove(3)  

print(sets)


while x < len(list2):
     print(list2[x])
     x += 1
