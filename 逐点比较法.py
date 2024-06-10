import matplotlib.pyplot as plt
import numpy as np

# 定义逆圆插补函数，从第三象限起点（-r, 0）开始的插补点。
def reverse_circle_interpolation(r, step=1):
    # 初始位置在第三象限的起点（-r, 0）
    x, y = -r, 0
    points = [(x, y)]

    def deviation(x, y, r):
        return x ** 2 + y ** 2 - r ** 2

    # 通过偏差判别函数判断下一个插补点的方向，循环计算插补点。
    while x < 0 and y > -r:
        if deviation(x, y, r) >= 0:
            x += step  # 在圆外或圆上时，x向右移动
        else:
            y -= step  # 在圆内时，y向下移动
        points.append((x, y))

        # 终点判断，防止y坐标超出范围
        if y <= -r:
            break

    # 确保最后两个点（-step，-r）和（0，-r）能够被绘制出来
    if points[-1] != (0, -r):
        points.append((0, -r))

    if points[-1] != (-step, -r):
        points.append((-step, -r))

    return points

# 定义并绘制四分之一圆函数
def plot_quarter_circle(r):
    theta = np.linspace(np.pi, 3*np.pi/2, 100)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    plt.plot(x, y, label='Quarter Circle')

# 定义绘制插补点函数
def plot_points(points):
    x_coords, y_coords = zip(*points)
    plt.plot(x_coords, y_coords, 'ro-', label='Interpolated Points')

# 参数设定
r = 6
step = 1

# 绘制圆弧
plot_quarter_circle(r)

# 计算逆圆插补点
points = reverse_circle_interpolation(r, step)

# 绘制插补点
plot_points(points)

# 图像设置
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Reverse Circle Interpolation in Third Quadrant')
plt.grid(True)
plt.legend()
plt.show()
