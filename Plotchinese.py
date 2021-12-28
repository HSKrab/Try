# 最小二乘擬合示例
import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
import matplotlib
from reportlab.pdfbase import pdfmetrics, ttfonts
import japanize_matplotlib

#plt.rcParams['font.sans-serif'] = ['Yu Gothic']
# zhfont1 = matplotlib.font_manager.FontProperties(
# fname=r'C:\Users\Hsieh\AppData\Local\Programs\Python\Python39\Lib\site-packages\matplotlib\mpl-data\fonts\ttf\YuGothM.ttf')


def func(x, p):
    """
    A*sin(2*pi*k*x + theta)
    """
    A, k, theta = p
    return A*np.sin(2*np.pi*k*x+theta)


def residuals(p, y, x):
    """
    x.y variation  
    """
    return y - func(x, p)


x = np.linspace(0, -2*np.pi, 100)
A, k, theta = 10, 0.34, np.pi/6  # real data
y0 = func(x, [A, k, theta])
y1 = y0 + 2 * np.random.randn(len(x))  # add noise

p0 = [7, 0.2, 0]  # speculative regression func.
plsq = leastsq(residuals, p0, args=(y1, x))

#print("真實引數:", [A, k, theta])
#print("擬合引數", plsq[0])

plt.plot(x, y0, label="真實資料")
plt.plot(x, y1, label="帶噪聲的實驗資料")
plt.plot(x, func(x, plsq[0]), label="擬合數據")
plt.legend()
plt.savefig('fit.pdf')
plt.show()
