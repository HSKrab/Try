# https://matplotlib.org/tutorials/introductory/pyplot.html
# https://matplotlib.org/2.1.1/api/_as_gen/matplotlib.pyplot.plot.html

import matplotlib.pyplot as plt
import numpy as np

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
#plt.plot(t, t**0.5, 'mp', t, t, 'r--', t, t**4, 'bs', t, t**3, 'g^')

x = [1, 2, 3]
y = [5, 7, 8]
fig, ax = plt.subplots()
ax.plot(x, y)
ax2 = ax.twinx()
plt.plot([1.5, 2.5, 4.5], [-1, -2, -6])
ax3 = ax.twinx()
plt.plot([6, 7, 8.3], [100, 101, 106])
plt.show()
plt.savefig(
    '\\\\Server01\\niihama_office\\破砕機事業\\設計関係\\謝\\締め付けトルク測定\\2222222222222.pdf', transparent=True)
