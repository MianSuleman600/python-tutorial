# Defining a simple function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2
x = add_numbers(5, 10)

print(x)


# NESTED FUNCTION
def outer_function(text):
    def inner_function():
        return text.upper()
    return inner_function()

result = outer_function("hello")
print(result)

# LAMBDA FUNCTION
multiply = lambda a, b: a * b
print(multiply(4, 5))

# FUNCTION WITH DEFAULT ARGUMENT

def add(*args):
    total =0
    for num in args:
        total += num 

    return total
print(add(1,2,3,4,5))

# FUNCTION WITH KEYWORD ARGUMENTS
def student(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

student(name="Ali", age=20, city="Karachi")

def showinfo(name , city ="lahore"):
    print("Name" , name)
    print("City" , city)
    return

showinfo(name="Ahmed", city="Islamabad")
showinfo(name="Sara")


# Keyword Aruguments and Positional Arguments
# in keyword args order not matter becasue we add with keyword but in positional args order matter 

# for example 

def greet(name , age ):
    print(f'Hello {name} your age is {age}')

greet(age=25 , name="Adeel") # keyword arguments
greet("Adeel" , 25) # positional arguments


#Arbitrary Positional Arguments
# if we don't know how many arguments will be passed we use *args in function definition
# args is just a tuple of arguments passed
def fruits(*args):
    for x in args:
        print(x)

fruits("apple" , "banana" , "mango")


# Arbitrary Keyword Arguments
# if we don't know how many keyword arguments will be passed we use **kwargs in function definition
# kwargs is just a dictionary of arguments passed

def details(**kwargs):
    for key , value in kwargs.items():
        print(f"{key} : {value}")

details(name="Adeel" , age=25 , city="Lahore")


# Function Annotations
# Function annotations are a way of associating metadata with function arguments and return values.

def add_numbers(a: int, b: int) -> int:
    return a + b
print(add_numbers(5, 10))
print(add_numbers.__annotations__)


# Function Packing and Unpacking
# Function packing is the process of collecting multiple arguments into a single parameter using *args or **kwargs.
# Function unpacking is the process of splitting a single parameter into multiple arguments using * or **

def pack_unpack(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
pack_unpack(1, 2, 3, name="Adeel", age=25)


# Recursive Function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120



