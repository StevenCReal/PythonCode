#用户
class User():
    """尝试创建用户"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print("User name: " + self.first_name + "·" + self.last_name)
        print(self.last_name + " is " + str(self.age) + " years old.")

    def greet_user(self):
        print("Have a nice day, " + self.last_name + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges():
    """管理员权限"""
    def __init__(self):
        self.privileges = ["add post", "delete post", "ban user"]
    
    """显示管理员拥有的权限"""
    def show_privileges(self):
        print("Admin can: ")
        for value in self.privileges:
            print("\t" + value)


class Admin(User):
    """初始化管理员"""
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()
        

#测试创建用户
steven = User('Jay', 'Chou', 40)

#测试用户属性描述及问候功能
steven.describe_user()
steven.greet_user()

#测试登陆次数记录
for value in range(1, 6):
    steven.increment_login_attempts()
    print(steven.login_attempts)

steven.reset_login_attempts()
print(steven.login_attempts)

#测试管理员权限功能
user1 =Admin('Steven','Chan',20)
user1.privileges.show_privileges()