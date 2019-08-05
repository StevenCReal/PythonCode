# 数到20
for value in range(1, 21):
    print(value)

# 一百万
thousand = []
for value in range(1, 1001):
    thousand.append(value)
for value in thousand:
    print(value)

# 计算1~1000的总和
thousand = [value for value in range(1, 1001)]
print("min: " + str(min(thousand)))
print("max: " + str(max(thousand)))
print(sum(thousand))

# 奇数
jishu = [value for value in range(1, 21, 2)]
print(jishu)
