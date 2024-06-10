import matplotlib.pyplot as plt
from matplotlib.patches import Arc

def plot_quarter_circle(r):
    # 绘制第二象限的1/4圆弧
    arc = Arc((0, 0), 2 * r, 2 * r, angle=0,
              theta1=90, theta2=180, color='red',
              linewidth=2, linestyle='-')
    plt.gca().add_patch(arc)

    # 添加线条用于图例
    plt.plot([], [], color='red', linestyle='-',
             linewidth=2, label='Quarter Circle')

def reverse_circle_interpolation(r, step):
    points = []
    x, y = 0, r
    a, b = 0, 0

    while True:
        if (x, y) not in points:  # 避免重复添加点
            points.append((x, y))
            print(f"Point: ({x}, {y})")  # 打印当前插补点

        a += abs(y)
        b += abs(x)

        if a >= 8:
            a -= 8
            if x > -r:
                x -= step

        if b >= 8:
            b -= 8
            if y > 0:
                y -= step

        if x == -r and y == 0:  # 对终点进行判定
            if (x, y) not in points:  # 避免重复添加终点
                points.append((x, y))
                print(f"Point: ({x}, {y})")  # 打印终点
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
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Reverse Circle Interpolation')
plt.grid(True)
plt.legend()
plt.show()
