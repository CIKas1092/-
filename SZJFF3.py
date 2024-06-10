import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np
    #导入库


def plot_quarter_circle(r):
    # 绘制第二象限的1/4圆弧
    arc = Arc((0, 0), 2 * r, 2 * r, angle=0,
              theta1=90, theta2=180, color='red',
              linewidth=2, linestyle='-')
    plt.gca().add_patch(arc)

    # 添加线条用于图例
    plt.plot([], [], color='red', linestyle='-',
             linewidth=2, label='Quarter Circle')

    #数字积分法
def reverse_circle_interpolation(r, step): #定义r和step
    points = []                            #
    x, y = 0, r                            #定义起点
    a, b, n, m = 0, 0, 0, 0                #a,b是3位2进制寄存器
                                           #n, m代表溢出，相当于ΔX和ΔY

    while True:
        points.append((x, y))

        a += abs(y)
        b += abs(x)

        if a >= 8:                         #判断ΔX
            a -= 8
            n = 1
            if x > -r:
                x -= step
        else:
            n = 0

        if b >= 8:                         #判断ΔY
            b -= 8
            m = 1
            y -= step
        else:
            m = 0

        if x == -r:
            a = 0

        if x == -r and y == 0:            #对终点进行判定
            points.append((x, y))
            break

    return points


def plot_points(points):
    x_vals = [p[0] for p in points]
    y_vals = [p[1] for p in points]
    plt.plot(x_vals, y_vals, marker='o',
             linestyle='-', color='blue',
             label='Interpolation Points')


plt.figure()

# 参数设定
r = 5
step = 1

# 绘制圆弧
plot_quarter_circle(r)

# 计算逆圆插补点
points = reverse_circle_interpolation(r, step)

# 绘制插补点
plot_points(points)

# 图像设置
plt.gca().set_aspect('equal', adjustable='box')  #窗口大小
plt.xlabel('X')                                  #设置y轴的标签
plt.ylabel('Y')                                  #设置y轴的标签
plt.title('Reverse Circle Interpolation')        #设置整个图表的标题
plt.grid(True)                                   #启用网格线
plt.legend()                                     #添加图例
plt.show()                                       #显示图表
