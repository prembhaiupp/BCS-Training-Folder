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
# secret_message = "   Programming in Python is not only powerful but also fun!   ".strip() .upper()
# print(f"{secret_message[15:21]}-{secret_message[34:42]}")
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
# message = "    🚨🔍📱🔑secret_code✌️".strip() .upper()
# idx=message.find("🔑")
# print(message[idx+1:])
# Clue: find

# Output
# SECRET_CODE✌️
#############################################################################
# def msg(i,emoji="🔥"):
#  for r in range(0,i+1):
#   print(f"{emoji}"*r)
# (msg(2, "🍓"))
# (msg(6, "🍍"))
# (msg(4, "🥕"))
# (msg(3))
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
# flowers = ["💐", "🌷", "🌼", "🌷", "🌺"]
# for i in range(len(flowers)):
#     print(f"Flower {i + 1} - {flowers[i]}")

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
# characters = ["Hello kitty", "Goku", "Pikachu", "Luffy", "Yuji Itadori", "Levi"]
# chai_hai=[]
# for cha in characters :
#     if len( cha)>=6:
#      chai_hai.append(cha)

# print(chai_hai)

# ### Expected Output
# ['Hello kitty', 'Pikachu', 'Yuji Itadori']
#######################################################################
# Task 1.3: Double the power
# powers = [2000, 3000, 4000, 1500]
# double_powers=[]
# for power in powers:
#    double_powers.append(power*2)
# print(power)
# print(double_powers)

# Output
# doubled_powers -> [4000, 6000, 8000, 3000]
# powers -> [2000, 3000, 4000, 1500]
##########################################################################
# Mix Data types
# pirate = {
#     "name": "Moneky D. Luffy",
#     "age": 25,
#     "crew_name": "Straw hat pirates",
#     "crew_members": ["Zoro", "Sanji", "Nami", "Chopper"],
#     "position": "captain",
# }


# print(pirate["crew_members"][1])
# pirate["age"]+=1
# print(pirate)

# Increase age by 1,,programing paradigms-function,oop,matlab,procedural
###########################################################################
books = [
    {"title": "Infinite Jest", "rating": 4.5, "genre": "Fiction"},
    {"title": "The Catcher in the Rye", "rating": 3.9, "genre": "Fiction"},
    {"title": "Sapiens", "rating": 4.9, "genre": "History"},
    {"title": "A Brief History of Time", "rating": 4.8, "genre": "Science"},
    {"title": "Clean Code", "rating": 4.7, "genre": "Technology"},
]

title_tit=[]
for book in books : 
      title_tit.append(book["title"])
print(title_tit)

title_tite=[]
for book in books : 
     if (book["genre"]=="Fiction"):
      title_tite.append(book["title"])
print(title_tite)

title_titee=[]
for book in books : 
     if (book["rating"]>=4.7):
      title_titee.append(book["title"])
print(f"Highest rated books are {title_titee[0]},{title_titee[1]} and {title_titee[2]}")
title_titeei=[]
for book in books : 
      if (book["rating"]+4.9):
       title_titeei.append(book["title"])
print(f"The book available is {title_titeei[2]}")

title_titeeii=[]
for book in books : 
      if book["rating"]>5:
       title_titeeii.append(book["title"])
print(f"There no books available at this rating 😅")




    
############################################################################
# ## Tata
# - Wheels - 4
# - Engine - v4
# - Model - Harrier
# - Doors - 4
class Car:
   def __init__(self, Wheels,Engine, Model, Doors):
    self.Wheels=Wheels
    self.Engine=Engine
    self.Model=Model
    self.Doors=Doors

   def horn(self):
    return "Vroom Vroom!"
   def accelater(self):
     return "100km/h"
   
tata = Car(4, "v4", "Harrier" ,5)
defainder=Car(4,"v8", "hamari",4)
print(tata.horn())
print(tata.accelater())
print(defainder.horn())
print(tata.Wheels)
###########################################################################
# ### Account
# 1. acc_no
# 2. name
# 3. balance
class Account:
  def __init__(self,acc_no,name,balance):
    self.acc_no=acc_no
    self.name=name
    self.balance=balance
  def branch(self):
    return "Aligarh Uttar pradesh"

account_holder=Account(12345678,"nk",50_000)
account_holder1=Account(123456789,"rishi",3_00_000)
account_holder2=Account(1234567890,"pushpa",10_00_000)
print(account_holder.acc_no)
print(account_holder1.name,account_holder1.branch())
print(account_holder2.name,account_holder2.balance,account_holder2.branch())