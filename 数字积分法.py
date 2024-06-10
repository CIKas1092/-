import matplotlib.pyplot as plt
from matplotlib.patches import Arc

def plot_quarter_circle(r):
    # 绘制第三象限的1/4圆弧
    arc = Arc((0, 0), 2 * r, 2 * r, angle=0,
              theta1=180, theta2=270, color='red',
              linewidth=2, linestyle='-')
    plt.gca().add_patch(arc)

    # 添加线条用于图例
    plt.plot([], [], color='red', linestyle='-',
             linewidth=2, label='Quarter Circle')

def reverse_circle_interpolation(r, step):
    points = []
    x, y = -r, 0  # 起点位于第三象限
    a, b = 0, 0
    n, m = 0, 0

    while True:
        points.append((x, y))

        a += abs(y)
        b += abs(x)

        if a >= 8:
            a -= 8
            n = 1
            if x < 0:
                x += step
        else:
            n = 0

        if b >= 8:
            b -= 8
            m = 1
            if y >-r:
              y -= step
        else:
            m = 0



        if y <= -r and x == 0:
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
plt.title('Reverse Circle Interpolation (Third Quadrant)')
plt.grid(True)
plt.legend()
plt.show()
