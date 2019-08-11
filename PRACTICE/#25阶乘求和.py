# method 1
res = 0
for i in range(1, 21):
    s = 1
    for j in range(1, i + 1):
        s *= j
    res += s
print(res)

# method 2
# 1+2!+3!+...+20!=1+2(1+3(1+4(...20(1))))
res = 1
for i in range(20, 1, -1):
    res = i * res + 1
print(res)
