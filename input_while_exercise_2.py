#肉店
meals = ['chicken', 'beef', 'duck', 'chicken', 'fish', 'snail', 'chicken']
finished_meals = []

while meals:
    meal = meals.pop()
    print("I have made you " + meal + ".")
    finished_meals.append(meal)

print("\nThese meals have been made:")
for finished_meal in finished_meals:
    print(finished_meal)

#鸡肉卖完了
meals = ['chicken', 'beef', 'duck', 'chicken', 'fish', 'snail', 'chicken']
print("\nChicken was sold out.")
while "chicken" in meals:
    meals.remove('chicken')

print(meals)

#梦想的度假胜地
dream_vacation = {}

polling_active = True

while polling_active:
    name = input("\nWhat's your name? ")
    place = input(
        "If you could visit one place in the world, where would you go? ")

    dream_vacation[name] = place

    repeat = input("would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("---- Survey Results ----")
for name, place in dream_vacation.items():
    print(name + "'s favorite place is " + place + ".")
