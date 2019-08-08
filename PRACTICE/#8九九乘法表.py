for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d * %d = %d\t' % (j, i, j*i), end='')   # 注意%d的用法，还有利用end=''来取消换行
    print('\n')
