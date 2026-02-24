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
# height=float(height)
# height2=float(height2)
# dif=(height - height2)
# if height > height2:
#     print(f"{name} is taller than {name2} by {dif} cm")
# elif height2 > height:
#     print(f"{name2} is taller than {name} by {dif} cm")
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
# stock5=[ "vanilla","green tea", "lemon", "chocolate","aaam"].lower()

# stock6=input("please enter your favorate?:")

# if  stock6 in stock5  :
#     print(f"Yes, we have {stock6} in stock")
# else:
#     print(f"Sorry, we ran out of ?:{stock6}")
    
#########################################################################
# for i in range(1,4):
#     print(f" 🍦"* i)


# hearts=1;
# while hearts <= 5 :
#   print(f" ❤️ "*hearts)
#   hearts +=1

####@@@@########################################################################

# Task 1.3 (Home Assignment)

# After the 🔑
message = "    🚨🔍📱🔑secret_code✌️".strip() .upper()
idx=message.find("🔑")
print(message[idx+1:])
# Clue: find

# Output
# SECRET_CODE✌️
#############################################################################
# def msg(i,emoji):
#  for r in range(1,5):
#    print(msg(f"emoji"*r))
#    print(msg(2, "🍓"))
#    print(msg(6, "🍍"))
#    print(msg(4, "🥕"))
#    print(msg(3))
# Task  1.1 - With function

# emoji(2, "🍓")
# emoji(6, "🍍")
# emoji(4, "🥕")
# emoji(3)

# 🍓
# 🍓🍓
# 🍍
# 🍍🍍
# 🍍🍍🍍
# 🍍🍍🍍🍍
# 🍍🍍🍍🍍🍍
# 🍍🍍🍍🍍🍍🍍
# 🥕
# 🥕🥕
# 🥕🥕🥕
# 🥕🥕🥕🥕
# 🔥
# 🔥🔥
# 🔥🔥🔥
#######################################################################
flowers = ["💐", "🌷", "🌼", "🌷", "🌺"]
for i in range(len(flowers)):
    print(f"Flower {i + 1} - {flowers[i]}")

# Task 1.1 - Print all the flower using for loop
# Hint - range, len
## RANGE US JAGHA USE KRTE  HAI JNHA HAME INDEX VALUE IK JARURAT HOTI HAI
# Expected output
# Flower 1 - 💐
# Flower 2 - 🌷
# Flower 3 - 🌼
# Flower 4 - 🌷
# Flower 5 - 🌺
##########################################################################
# ## Task 1.4
# Find longer names (>= 6 letter)
## WITHOUT RANGE KE YE USE KRTE HAI 
characters = ["Hello kitty", "Goku", "Pikachu", "Luffy", "Yuji Itadori", "Levi"]
chai_hai=[]
for cha in characters :
    if len( cha)>=6:
     chai_hai.append(cha)

print(chai_hai)

# ### Expected Output
# ['Hello kitty', 'Pikachu', 'Yuji Itadori']
#######################################################################
# Task 1.3: Double the power
powers = [2000, 3000, 4000, 1500]
double_powers=[]
for power in powers:
   double_powers.append(power*2)
print(power)
print(double_powers)

# Output
# doubled_powers -> [4000, 6000, 8000, 3000]
# powers -> [2000, 3000, 4000, 1500]
