# 比萨配料
toppings = ""
while toppings != "quit":
    toppings = input("What toppings would you like to have?")
    if toppings != "quit":
        print("We'll add " + toppings + " on your pizza.")

#电影票
active = True
while active:
    age = input("Would you mind tell me your age?")
    age = int(age)
    if age == 0:
        active = False
        continue
    elif age <= 3:
        print("Get out of here!")
    elif age >= 70:
        print("Get outta here!")
    else:
        print("shit")

#active = True
#while active:
#    print(666)