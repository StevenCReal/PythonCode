cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

if cars[0] == 'audi' and cars[1] == 'bmw':  # 与:and 或:or 非:!
    print("Yes, you're right")

if 'audi' in cars:
    print("It's in it.")
if 'nissan' not in cars:
    print("No, it's not in it.")

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

requested_toppings = []
if requested_toppings:  # 需要判断列表是否为空
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
        print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

available_toppings = [
    'mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple',
    'extra cheese'
]
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")
