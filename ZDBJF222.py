import matplotlib.pyplot as plt
import numpy as np  # 导入库


# 定义逆圆插补函数,计算从第二象限起点（0, r）开始的插补点。
# 偏差判别函数
def reverse_circle_interpolation(r, step=1):  #半径r和步长step作为参数
    # 初始位置在第二象限的起点（0, r）
    x, y = 0, r
    points = [(x, y)]

    print(f'Initial point: ({x}, {y})')  # 输出初始点

    def deviation(x, y, r):              #当前点与圆心的偏差
        return x ** 2 + y ** 2 - r ** 2

    # 定义偏差判别函数，判断当前点是否在圆内或圆外。
    while x > -r and y > 0:
        if deviation(x, y, r) >= 0:
            y -= step
        else:
            x -= step
        points.append((x, y))

        print(f'Interpolated point: ({x}, {y})')  # 输出插补点

        # 通过偏差判别函数判断下一个插补点的方向，循环计算插补点。
        # 终点判断
        if x <= -r:
            break

    # 终点判断，防止x坐标超出范围
    # 确保最后的点能够被绘制出来
    if points[-1] != (-r, step):
        points.append((-r, step))
        print(f'Final point: ({-r}, {step})')  # 输出最后点

    if points[-1] != (-r, 0):
        points.append((-r, 0))
        print(f'Final point: ({-r}, 0)')  # 输出最后点



    return points


# 定义并绘制四分之一圆函数
def plot_quarter_circle(r):
    theta = np.linspace(np.pi / 2, np.pi, 100)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    plt.plot(x, y, label='Quarter Circle')


# 定义绘制插补点函数
def plot_points(points):
    x_coords, y_coords = zip(*points)
    plt.plot(x_coords, y_coords, 'ro-', label='Interpolated Points')


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
plt.gca().set_aspect('equal', adjustable='box')  # 窗口大小
plt.xlabel('X')  # 设置x轴的标签
plt.ylabel('Y')  # 设置y轴的标签
plt.title('Reverse Circle Interpolation')  # 设置整个图表的标题
plt.grid(True)  # 启用网格线
plt.legend()  # 添加图例
plt.show()  # 显示图表
