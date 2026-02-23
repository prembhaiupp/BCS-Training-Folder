# fahrenheit= float(input("please provide your fahrenheit:"))
# celsius = ( fahrenheit- 32)* 5/9
# print(f"The {fahrenheit}°F is {celsius}°C")
# Task 1.1
# Output (Assume PI - 3.14)
# Provide the radius of the circle: 4.2
# Area of circle is 55.3896
# radius=float(input("Provide the radius of the circle:"))
# PI=(3.14*radius*radius)
# print(f"Area of circle is {PI}*{radius}")
# l=["p","y","t","o","n","","r","o","c","k","s"]
# print(l[1:12:1])
# quote = "Dream is not something that you see in sleep, Dream is something that does not let you sleep"
# print(quote.count("Dream"))  # 2
# print(quote.find("something"))  # 13

# print(quote.replace("Dream", "🛌💭"))
secret_message = "   Programming in Python is not only powerful but also fun!   ".strip() .upper()
print(f"{secret_message[15:21]}-{secret_message[34:42]}")
# Task 1.1
# Expected Output
# "PYTHON-POWERFUL"


# name=input("tell me your name?:latha")
# year=input("tell me your birth year?:")
# print(year)
# year=int(year)
# current_year=2026
# current_year=(current_year)
# print(f"Hi{name} you are {current_year-year} years old")
# print(year)


# ####################@@@@ Task 1.1,2,3 @@@####################################
# Compare Two People’s Heights (Taller / Same Height)
# Hint - input
# Better - abs()
# Expected Output -
# Case 1:
# Please tell me the captain name?: Luffy
# Please tell me the vice captain name?: Zoro
# Please tell me the height of Luffy?: 173
# Please tell me the height of Zoro?: 163
# Luffy is taller than Zoro by 10cm
# name=input("please tell me the captain name?:")
# name2=input("please tell me the vice captain name2?:")
# height=input(f"please tell me the height of {name}?:")
# height2=input(f"Please tell me the height of {name2}?:")
# height=int(height)
# height2=int(height2)
# if height > height2:
#     print(f"{name} is taller than {name2} by {height - height2} cm")
# elif height2 > height:
#     print(f"{name2} is taller than {name} by {height2 - height} cm")
# else:
#     print(f"{name} and {name2} have the same height ")


###################################################################

# Task 1.2
# Clue - String methods
# Handle the extra space & letter case
# Case1:
# Please enter your fav 🍧?:      vaNillA
# Yes, we have vanilla in stock

# Case 2:
# Please enter your fav 🍧?:   pisTa
# Sorry, we ran out of pista
# stock5=[ "vanilla","green tea", "lemon", "chocolate","aaam"]

# stock6=input("please enter your favorate?:")

# if  stock6 in stock5  :
#     print(f"Yes, we have {stock6} in stock")
# else:
#     print(f"Sorry, we ran out of ?:{stock6}")
    
#########################################################################
# for i in range(1,6):
#     print(f" 🍦"* i)

#     hearts=1;
# while hearts <= 5 :
#   print(f" ❤️ "*hearts)
#   hearts +=1

####@@@@########################################################################

# Task 1.3 (Home Assignment)

# After the 🔑
message = "    🚨🔍📱🔑secret_code✌️".strip() .upper()
print(f"{message[-14:10]}{message[10:-1]}")
# Clue: find

# Output
# SECRET_CODE✌️