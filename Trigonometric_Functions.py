import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
sin = np.sin(x)
cos = np.cos(x)
tan = np.tan(x)
sec = 1 / cos
cot = 1 / tan
csc = 1 / sin

plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.spines.top'] = False
fig, ax = plt.subplots(3, 2)

plt.subplot(3, 2, 1)
plt.plot(x, sin)
plt.title('Sine(x)')

plt.subplot(3, 2, 2)
plt.plot(x, cos)
plt.title('Cosine(x)')

plt.subplot(3, 2, 3)
plt.plot(x, tan)
plt.title('Tangent(x)')

plt.subplot(3, 2, 4)
plt.plot(x, sec)
plt.title('Secant(x)')

plt.subplot(3, 2, 5)
plt.plot(x, cot)
plt.title('Cotangent(x)')

plt.subplot(3, 2, 6)
plt.plot(x, csc)
plt.title('Cosecant(x)')

plt.setp(ax,
         ylim=(-2, 2),
         xticks=np.arange(-2 * np.pi, (2 * np.pi) + np.pi, step=np.pi),
         xticklabels=['-2π', '-π', '0', 'π', '2π'])
fig.tight_layout()
plt.show()
