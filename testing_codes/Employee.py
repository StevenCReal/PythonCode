class Employee():
    def __init__(self,first_name, last_name, salary = 0):
        """创建并初始化一位雇员"""
        self.first_name = first_name
        self.first_name = last_name
        self.salary = salary
    
    def give_raise(self, increment = 5000):
        if increment < 0:
           print("You cannot reduce salary!!")
           return False
        else:
            self.salary += increment
            return True