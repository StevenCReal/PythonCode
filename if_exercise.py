# 以特殊方式跟管理员打招呼
# 处理没有用户的情形
users = ['user1', 'user2', 'user3', 'admin', 'user4']
if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to check the program?")
        else:
            print("Hello " + user + ", thank you for logging in again!")
else:
    print("We need to find some users!")

# 检查用户名
current_users = users[:]
new_users = ['User5', 'USER1', 'admin', 'user2', 'user6']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user + " has been used, please enter a new name.")
    else:
        print(new_user + " has not been used.")

# 序数
numbers = [value for value in range(1, 10)]
for number in numbers:
    if number / 4 >= 1:
        print(str(number) + 'th')
    elif number == 1:
        print(str(number) + 'st')
    elif number == 2:
        print(str(number) + 'nd')
    else:
        print(str(number) + 'rd')
