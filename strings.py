var1 = "hello world"
var2 = "python programming"

print(var1.title())
print(var2.title())

print(var1.upper())
print(var2.capitalize())
print(var1.lower())
print(var2.swapcase())
print(var1.replace("world", "there"))
print(var2.replace("python", "Java"))

print(var1.split())
print(var2.split(" "))

print("-".join(var1.split()))
print(" ".join(var2.split()))

print(var1.startswith("hello"))
print(var2.endswith("programming"))

print(var1.find("world"))
print(var2.index("programming"))

print(var1.count("o"))
print(var2.count("p"))

print(var1.isalpha())
print(var2.isalnum())
print(var1.isdigit())

print(var1.strip())
var3 = "   spaced out   "

print(var3.strip())
print(var3.lstrip())
print(var3.rstrip())
print(var3.replace(" ", ""))
print(var3.strip().upper())
print(var1.center(20))


print(var2[::-1])

print(var1[1:5])

print("updated string :-",var2[:6] + 'java')

