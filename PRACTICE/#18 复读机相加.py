a = input('Enter a: ')
num = int(input('Enter num: '))
s = 0
for i in range(1, num + 1):
    s += int(a)
    a += a[0]  # a是字符串，a[0]是2

print(s)
