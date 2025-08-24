age = int(input("Enter your age: "))

name = "Jubaer"

todayIsCold = True

print(f"Hello, my name is {name} and I am {age} years old.")

#Logical Part
if age > 18 :
    print("You are an adult.")

else :
    print("You are not an adult.")

def hello(aString, age):
    return f"Hello {aString} you are {age} years old."

retType = hello("Jubaer", 23)

print(retType)