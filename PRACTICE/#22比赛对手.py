import copy
a = set(['x', 'y', 'z'])    # 集合的特点：无序、不重复,传入list，元素可修改
b = set(copy.deepcopy(a))
c = set(copy.deepcopy(a))
a -= set(('x'))     # 传入tuple，元素不可修改
c -= set(('x','z'))

for i in a:
    for j in b:
        for k in c:
            print(set((i,j,k)))
            if len(set((i,j,k))) ==3:
                print('a:%s, b:%s, c:%s' %(i,j,k))
