#记录访问访客名字

#给出文件名字
file_name = r"file_and_error\Guests List.txt"

active = True
while active:
    name = input("Enter your name: ")
    # 附加模式下写入用户名
    with open(file_name, 'a') as file_object:
        file_object.write(name + "\n")

    # 给予用户问候
    print("Hello, " + name + "!")

    # 控制重复输入用户名
    repeat = input("Continue? (yes/no): ")
    if repeat == 'no':
        break

# 读取并打印出访问过的用户名
with open(file_name, 'r') as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())