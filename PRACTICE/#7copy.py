import copy
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ['a']]

# 有关浅拷贝和深拷贝的参见印象笔记
# 可变对象：
# ——python基础（5）：深入理解 python 中的赋值、引用、拷贝、作用域
b = a[:]  # 浅拷贝：
c = a  # 赋值
d = copy.copy(a)  # 浅拷贝
e = copy.deepcopy(a)  # 深拷贝

a.append(5)
a[10].append('b')

print('a=', a)
print('b=', b)
print('c=', c)
print('d=', d)
print('e=', e)
