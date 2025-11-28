#d1 = {"Fruits" : ["Apple", "Banana", "Cherry"], "Vegetables": ["Carrot", "Lettuce", "Spinach"]}
#d2 = {('pakistan , usa') : 'countries' , ('china , india') : 'countries'}


#print(type(d1))
#
# 
#print(d2)


sport_players = {
    "Cricket": ["Babar Azam", "Shaheen Afridi", "Fakhar Zaman"],
    "Football": ["Cristiano Ronaldo", "Lionel Messi", "Neymar Jr"],
    "Tennis": ["Roger Federer", "Rafael Nadal", "Novak Djokovic"]
                 
}


student_info = {
    'name' : 'ali',
    'age' : 20,
    'courses' : ['math', 'science', 'english']
}

student_info['city'] = 'karachi'

#for key  in student_info:
#    print(key)

#for key,value in student_info.items():
#    print(f"{key} : {value}")

# Dictionary view objects

#for key in sport_players.keys():
#    print(key)

#for value in sport_players.values():
#    print(value)


student = {"a" : 1 , "b":2}

keys = student.keys()

#print(keys)

student["c"] = 3

#print(keys)


d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}

d3 = d1.copy()

#print(d3 )

d4 = dict(d1)

#print(d4)


# Nested Dictionaries

student = {
    "1" : {'name': 'Ali', 'age': 20},
    "2" : {'name': 'Sara', 'age': 22},
    "3" : {'name': 'Omar', 'age': 21}
}

#print(student["2"]["name"])
import array as arr 

a = arr.array('i' , [1,2,3,4,5 ])
b = arr.array('i' , [6,7,8,9,10 ])

#for i in range(len(b)):
 #   a.append(b[i])

#x = a.tolist()
#y =b.tolist()

#z = x + y

#

a.extend(b)
    
for t in range(len(a)):
    print(a[t])





#print(type(a),a)



# array typecodes
#'b' : signed char
#'B' : unsigned char
#'u' : unicode char
#'h' : signed short
#'H' : unsigned short
#'i' : signed int
#'I' : unsigned int
#'l' : signed long
#'L' : unsigned long
#'f' : float
#'d' : double



#print(student_info["age"])
#print(student_info["courses"][2])

#print(sport_players["Cricket"][1])