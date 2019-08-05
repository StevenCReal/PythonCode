# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

# method 1
total = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if ((i != j) and (i != k) and (j != k)):
                print(i, j, k)
                total += 1
print(total)

# method 2
import itertools

total2 = 0
a = [1, 2, 3, 4]
for i in itertools.permutations(a, 3):  # permutation指排列组合，iterable目前可理解为可迭代对象
    print(i)
    total2 += 1
print(total2)
