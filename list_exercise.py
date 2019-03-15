# 数到20
for value in range(1, 21):
    print(value)

# 一百万
million = []
for value in range(1, 1000001):
    million.append(value)
for value in million:
    print(value)

# 计算1~1 000 000的总和
million = [value for value in range(1, 1000001)]
print("min: " + str(min(million)))
print("max: " + str(max(million)))
print(sum(million))

#奇数
jishu = [value for value in range(1, 21, 2)]
print(jishu)