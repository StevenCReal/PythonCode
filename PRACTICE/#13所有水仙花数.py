# method 1
for i in range(100, 1000):
    if ((i % 10)**3 + (int(i / 10) % 10)**3 + (int(i / 100))**3) == i:
        print(i)

# method 2
for i in range(100, 1000):
    s = str(i)
    one = int(s[-1])
    ten = int(s[-2])
    hun = int(s[-3])
    if i == one**3 + ten**3 + hun**3:
        print(i)