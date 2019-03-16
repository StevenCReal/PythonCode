import matplotlib.pyplot as plt

from random_walk import RandomWalk

times = 0
# 只要程序处于活动状态， 就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实例， 并将其包含的点都绘制出来
    rw = RandomWalk(5000)
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds, edgecolors=None, s=1)

    #突出起点和终点
    plt.scatter(0,0, c='green', edgecolors='none', s=20)
    plt.scatter(rw.x_values[-1],rw.y_values[-1], c='blue', edgecolors='none', s=20)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    times += 1
    if times == 20:
        break