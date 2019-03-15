avengers = [
    'Iron Man', 'Captain America', 'The Hulk', 'Black Widow', 'Ant Man',
    'Thor', 'Black Panther', 'Spider Man', 'Scarlet Witch', 'War Machine',
    'Docotor Strange'
]
for avenger in avengers:
    print(avenger)
print("Avengers will come back!\n")

for value in range(1, 10):  #达到10时停止，所以只显示1~9
    print(value)
print('\n')

number = list(range(1, 11))
print(number)

even_number = list(range(2, 11, 2))  #可指定步长
print(even_number)

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

squares_2 = []
for value in range(1, 11):
    squares_2.append(value**2)
print(squares_2)

print("min: " + str(min(squares)))
print("max: " + str(max(squares)))
print("sum: " + str(sum(squares)))

squares_3 = [value**2
             for value in range(1, 11)]  #列表解析 将for循环和创建新元素的代码合并成一行，并自动附加新元素
print(squares_3)

print(avengers)
print(avengers[2:5])  #切片

print("Here are last three avengers: ")
for avenger in avengers[-3:]:
    print(avenger)

avengers_2019 = avengers[:]  #必须用切片的方法，即加冒号
print(avengers_2019)

fast_food = ['KFC', 'Mc.Donald', 'Pizza Hut']
junk_food = fast_food  #这时两个变量实际指向同个列表了
fast_food.append('Burger King')
print(junk_food)

currency = ('RMB', 'dollar', 'yen')  #圆括号的是元组，元组的元素无法修改
print(currency[0])
print(currency[1])

#虽然不能修改元组的元素， 但可以给存储元组的变量赋值。
currency = ('pound', 'euro', 'HK Dollar')
print(currency)
