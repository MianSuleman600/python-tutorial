#Input and Output in Python

#name = input("enter your name :")

#age = input("enter your age :")
#print("Hello " + name + "! You are " + age + " years old.")

# Take multiple inputs from user
#x,y = input("enter two values :").split()
#print("The values you entered are : " + x + " and " + y)

#n = int(input("enter a number :"))
#print("The number you entered is :", n)

#price = float(input("enter the price of the item :"))
#print("The price you entered is :", price)

# multiple variable assignment
##print(a)


x ="ali"
y=x


#print(y)

del(x)

# Swap two varibales 

#a , b = 10,20

#a ,b = b,a

#print(a,b)

# counting char in a string

#word = "python"
#length = len(word)
#print(length)

# conditions 
#z = 20
#if (z == 20):
 #   print("Salam pakistan")
#else:
#    print("hello world")

# MEMBERSHIP OPERATORS -> in and not in

#a = 10 
#b = 20 

#my_list = [1,2,3,4,5]

#print(a in my_list)
#print(b not in my_list )

# python identity operators -> is and is not
# this check if two operators occupy the same memory location or not

#a = [1,2,3]
#b = [1,2,3]

#c =a

#print(a is c )
#print(a is b )
#print(a is not c)
#print(a is not b )

# Operator precedence
# Highest precedence to Lowest precedence
# Parentheses ()
# Exponentiation **
# Unary + and -
# Multiplication *, Division /, Floor division //, Modulus %
# Addition + and Subtraction -
#print(3 + 4 * 2)  # Outputs 11
#print((3 + 4) * 2)  # Outputs 14


# Bitwise Operators

# Bitwise operators work on binary representations of integers.
# Each bit of the number is operated on individually.

# &(AND), |(OR), ^(XOR), ~(NOT), <<(Left Shift), >>(Right Shift)

#a =60
#b= 13

#print (a & b)  # AND
#print (a | b)  # OR
#print (a ^ b)  # XOR
#print (~a)      # NOT
#print (a << 2)  # Left Shift
#print (a >> 2)  # Right Shift


# Walrus Operator (:=)

'''The walrus operator (:=) is a new type of assignment operator that was introduced in Python 3.8.The walrus operator (:=) is used to assign a value to a variable from an expression inside loop conditions. This is useful when you need to use a value multiple times in a loop, but don't want to repeat the calculation. Hence it is also known as the assignment expression operator. The name "walrus operator" comes because the operator (:=) looks likes the eyes and tusks of a walrus. '''

# Example without walrus operator
#stack = [1, 2, 3, 4, 5]
#n = len(stack)
#while n > 0:
#    print(stack.pop())
#    n -= 1
# Example with walrus operator
#stack = [1, 2, 3, 4, 5]
# while (n := len(stack)) > 0:
#     print(stack.pop())

# Unit Converter
print("--------This is unit converter program----- ")

print("1. KM to M")
print("2. M to KM")
print("Enter 0 to exit  ")


while True:

    choice = int(input("Enter your choice 1 or 2 , 0 to exit :"))
    if choice == 1:
        km = float(input("Enter value in KM :"))
        m = km * 1000
        print(f"{km} KM is equal to {m} M")
    elif choice == 2:
        m = float(input("Enter value in M :"))
        km = m / 1000
        print(f"{m} M is equal to {km} KM")

    elif choice ==0:
        print("Exiting the program. Goodbye!")
        break   
    else:
        print("Invalid choice ! Please select 1 or 2 ")








# Find BMI 

print("----------------THIS IS BMI FINDER PROJECT----------------- ")

weight = int(input("Enter Your Weight in kg ! :"))
height = int(input("Enter height in meter :"))

bmi = weight / (height ** 2)

if bmi <18:
    print(f"this is underfit and your BMI IS {bmi}")

elif bmi > 30:
    print(f"this is overfit and your BMI IS {bmi}")
    print (bmi)

elif bmi > 18 or bmi < 25:
    print(f"this is normal and your BMI IS {bmi}") 
   












