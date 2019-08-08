import math

for i in range(100, 200):
    flag = 0
    for j in range(2, round(math.sqrt(i)) + 1):
        if i % j == 0:
            flag = 1
            break
    if flag:
        continue
    print(i)

print('\nSimplify the code with \'else\': \n')

for i in range(100, 200):
    for j in range(2, round(math.sqrt(i)) + 1):
        if i % j == 0:
            break
    else:  # 这里用的是for...else语句，for中必须有break，
        # 当迭代对象完成所有迭代后且此时的迭代对象为空时，如果存在else子句则执行else子句，没有则继续执行后续代码；
        # 如果迭代对象因为某种原因（如带有break关键字）提前退出迭代，则else子句不会被执行，程序将会直接跳过else子句继续执行后续代码
        print(i)
