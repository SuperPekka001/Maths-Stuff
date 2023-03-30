import matplotlib.pyplot as plt
import math

from matplotlib.patches import Arc

plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.left'] = False
plt.rcParams['axes.spines.bottom'] = False


def get_angle_plot(line1, line2, offset=1, color=None, origin=(0, 0), len_x_axis=1, len_y_axis=1):
    l1xy = line1.get_xydata()
    # Angle between line1 and x-axis
    slope1 = (l1xy[1][1] - l1xy[0][1]) / float(l1xy[1][0] - l1xy[0][0])
    angle1 = abs(math.degrees(math.atan(slope1)))  # Taking only the positive angle
    l2xy = line2.get_xydata()
    # Angle between line2 and x-axis
    slope2 = (l2xy[1][1] - l2xy[0][1]) / float(l2xy[1][0] - l2xy[0][0])
    angle2 = abs(math.degrees(math.atan(slope2)))
    theta1 = min(angle1, angle2)
    theta2 = max(angle1, angle2)
    if color is None:
        color = line1.get_color()  # Uses the color of line 1 if color parameter is not passed.
    return Arc(origin, len_x_axis * offset, len_y_axis * offset, 0, theta1, theta2, color=color)


def get_value(trig_func, A, B, C, x):
    if trig_func == 'sin':
        return f'Sin({x}°) = {str("%.2f" % (B / A))}'
    elif trig_func == 'cos':
        return f'Cos({x}°) = {str("%.2f" % (C / A))}'
    elif trig_func == 'tan':
        return f'Tan({x}°) = {str("%.2f" % (B / C))}'


def display_triangle(A, B, C, x, result=None):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    hypotenuse = plt.Line2D([0, 5], [0, 2.5])
    opposite = plt.Line2D([5, 5], [0, 2.5])
    adjacent = plt.Line2D([0, 5], [0, 0])
    ax.add_line(hypotenuse)
    ax.add_line(opposite)
    ax.add_line(adjacent)
    angle_plot = get_angle_plot(hypotenuse, adjacent, 1)
    # Gets the arguments to be passed to ax.text as a list to display the angle value besides the arc
    ax.add_patch(angle_plot)  # To display the angle arc
    ax.text(0.5, 0.1, x)  # To display the angle value
    ax.text(2.5, 1.5, A)
    ax.text(5.15, 1, B)
    ax.text(2.5, -0.25, C)
    if result: ax.text(0, 3.5, result, fontweight='bold', fontsize=25.0)
    ax.set_xlim(0, 7)
    ax.set_ylim(0, 5)
    plt.tick_params(left=False, right=False, labelleft=False,
                   labelbottom=False, bottom=False)
    plt.show()


trig_func = input('Would you like to calculate sin, cos or tan?\nEnter name of the trig function: ')
display_triangle('A', 'B', 'C', 'x')
print('Enter the values for sides A, B and C and angle x:- ')
A = float(input('Enter the value for side A: '))
B = float(input('Enter the value for side B: '))
C = float(input('Enter the value for side C: '))
x = float(input('Enter the value for angle x: '))
result = get_value(trig_func, A, B, C, x)
display_triangle(A, B, C, x, result)
