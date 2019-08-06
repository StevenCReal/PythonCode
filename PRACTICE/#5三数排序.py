# method 1
raw = []
i = 0
while i < 3:
    x = int(input('int%d: ' % (i)))
    raw.append(x)
    i += 1
print(raw)

# method 2
for i in range(len(raw)):
    for j in range(i,len(raw)):     # range(i, len(raw)) 注意要从i开始，不然i循环完一轮后j又会从0开始
        if raw[i] > raw[j]:
            raw[i], raw[j] = raw[j], raw[i]  # amazing!
            print(raw)
print(raw)
