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