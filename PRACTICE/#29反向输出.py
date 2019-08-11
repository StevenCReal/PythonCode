num = input('Enter your number:')
print(len(num))
# for i in range(len(num)-1,-1,-1):
#     print(num[i],end='')
print(num[::-1])    # [::-1]表示从最后一位反向读取
