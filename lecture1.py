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
   












