cars = ['Toyota', 'Honda', 'Yoshida']
print(cars)

print(cars[0].upper())

print(cars[-1])  # 返回最后一个元素
# ——————————————————————————————————————————————————————————————

cars.append('Suzuki')  # 在末尾添加新元素
print(cars[-1])
cars.insert(1, 'other')  # 插入元素
print(cars)
del cars[1]  # 删除元素——del
print(cars)

popped_car = cars.pop()  # 从列表末端“弹出”该元素，并能接着使用该元素——pop()
print(popped_car)
print(cars)
any_car = cars.pop(0)  # 从列表任意处弹出
print(any_car)
print(cars)

# 根据值来去除——remove()
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.\n")
# ——————————————————————————————————————————————————————————————————————————————————————————

motorcycles.sort()  # 按字母顺序排序
print(motorcycles)
motorcycles.sort(reverse=True)  # 按字母反顺序排序
print(motorcycles)

print(sorted(motorcycles, reverse=True))  # sorted()临时改变顺序
print(motorcycles)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()  # reverse()反转顺序，永久性的
print(cars)

print(len(cars))  # 获得长度
