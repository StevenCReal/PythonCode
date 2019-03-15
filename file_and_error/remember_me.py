import json

# 如果以前存储了用户名， 就加载它
# 否则， 就提示用户输入用户名并存储它
filename = r"file_and_error\user_name.json"
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
     username = input("What is your name? ")
     with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")