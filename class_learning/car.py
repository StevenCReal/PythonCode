"""一组用于表示燃油汽车和电动汽车的类"""


class Car():
    def __init__(
            self,  # 都是形参
            make,
            model,
            year,
    ):
        self.make = make  # 定义变量make, model, year, odometer_reading
        self.model = model  #  以self 为前缀的变量都可供类中的所有方法使用
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):  # 每个与类相关联的方法调用都自动传递实参self ， 它是一个指向实例本身的引用， 让实例能够访问类中的属性和方法
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles


class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """打印一条消息， 指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """
        电动汽车的独特之处
        初始化父类的属性， 再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)  # super()超类方法
        self.battery = Battery()
