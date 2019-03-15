name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")

age = input("How old are you? ")
if int(age) >= 18:  #need 'int()' to convert the input to number
    print("You're an adult now! ")

value = 0
while value <= 5:
    print(str(value) + " is not big enough!")
    value += 1
print(value)

mirror = ""
prompt = "I'll repeat your word."
prompt += "\nIf you don't want to continue, enter 'quit'."
print(prompt)
while mirror != 'quit':
    mirror = input()
    if mirror != 'quit':
        print(mirror)

# 标志
active = True
prompt = "I'll repeat your word."
prompt += "\nIf you don't want to continue, enter 'quit'."
print(prompt)
mirror = ""
while active:
    mirror = input()
    if mirror == 'quit':
        active = False
    else:
        print(mirror)
