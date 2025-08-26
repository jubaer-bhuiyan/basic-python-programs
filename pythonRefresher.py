age = int(input("Enter your age: "))

name = "Jubaer"

todayIsCold = True

print(f"Hello, my name is {name} and I am {age} years old.")

#If-Else Part
if age > 18 :
    print("You are an adult.")

else :
    print("You are not an adult.")

#User Defined Fynction
def hello(aString, age):
    return f"Hello {aString} you are {age} years old."

retType = hello("Jubaer", 23)

print(retType)

#List Part 
dogNames = ["Tommy", "Max", "Sam", "Rocky", True, False, 43, 5.6]

dogNames.insert(0, "Lucky")

dogNames[1] = "Buddy"

del(dogNames[3])

print(len(dogNames))

print(dogNames)

#FOr loop
dogNames = ["Tommy", "Max", "Sam", "Rocky"]

for dog in dogNames:
    print(dog)

for x in range(1,10):
    print(x)

#While loop
age = 0
while age < 18:
    print(age)
    age += 1

#Dictionary

dogs = {
    "Fido": 8,
    "Buddy": 5,
    "Rex": 2
}

del(dogs["Buddy"])

dogs["Sam"] = 4

dogs["Rex"] = 17

print(dogs)


#Classes
class Dog:

    dogInfo = "Hey dogs are cool"

    def __init__(self, name, age, furColor):
        self.name = name
        self.age = age
        self.furColor = furColor

    def bark(self, str):
        print("Bark " + str)

myDog = Dog("Rex", 3, "Brown")
print(myDog.age)

myDog.bark("Tommy")
myDog.name = "Tommy"
myDog.age = 5
print(f"My dog's name is {myDog.name} and he is {myDog.age} years old.")
Dog.dogInfo = "Dogs are awesome"
print(Dog.dogInfo)