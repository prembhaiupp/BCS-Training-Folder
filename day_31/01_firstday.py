print("Hello, 🌏 ")

print(type(42))  # <class 'int'>
print(type("Abc"))
print(type(True))
print(type(4.5))
print(type([40, 60, 70]))  # <class 'list'>

print(type((40, 60, 70)))  # <class 'tuple'>

full_name = "Tara Chand"

print(full_name)
print(type(full_name))

# + Concatenation
print("Welcome, " + full_name + "!🎉")
age=20
# Task with f-string
print("my age is," + str(age))
followers =2_00_000
print(f"My age is  {age} and my followers are {followers*2}")