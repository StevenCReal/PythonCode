num = input('Enter your num: ')
a = 0
b = len(num) - 1
flag = 1
while a < b:
    if num[a] != num[b]:
        print('不是回文串')
        flag = 0
        break
    a, b = a + 1, b - 1
if flag:
    print('是回文串')
