
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
import numpy.ma as ma
from matplotlib.ticker import FixedLocator, FixedFormatter

x1, x2, x3 = [9.6, 30.9], [17, 38.8], [27, 50]


def set_in(T):
    x2.append(T)
    x1.append(x1[-1]+(x1[-1]-x1[-2])*(x2[-1]-x2[-2])/(x2[-2]-x2[-3]))
    x3.append(x3[-1]+(x3[-1]-x3[-2])*(x2[-1]-x2[-2])/(x2[-2]-x2[-3]))


def set_inv(T):
    x3.append(T)
    x1.append(x1[-1]+(x1[-1]-x1[-2])*(x3[-1]-x3[-2])/(x3[-2]-x3[-3]))
    x2.append(x2[-1]+(x2[-1]-x2[-2])*(x3[-1]-x3[-2])/(x3[-2]-x3[-3]))


set_in(43)
set_inv(65)
x = x1
fig = plt.figure(figsize=(16.53, 11.69))
ax = fig.add_axes([0.1, 0.12, 0.85, 0.8])
A1, = ax.plot(x, x1, label="Atmosphere", ls=':', linewidth=0.5,
              marker="o", markersize=20,  alpha=0.9)
A2, = ax.plot(x, x2, label="Inside Panel", ls=':', linewidth=0.5,
              marker="^", markersize=20,  alpha=0.9)
A3, = ax.plot(x, x3, label="Inverter", ls=':', linewidth=0.5,
              marker="D", markersize=20, alpha=0.9)
ax.set_xticks(x)
ax.set_xticklabels(['Winter', 'Autumn', 'Tᵢₙ = 43°C', 'Tᵢₙᵥ = 65°C'])
ax.set_xlim(5, 50)
ax.set_ylim(0, 75)
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("%d°C"))
ax.yaxis.set_major_locator(ticker.MultipleLocator(15))

for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(4)

ax.tick_params(axis='x', which='major', top=False,
               right='on', direction='in', width=3, labelsize=18, pad=15)
ax.tick_params(axis='y', which='both', top='on',
               right='on', direction='in', width=3, labelsize=18, pad=10)
ax.tick_params(axis='both', which='major', length=8)

labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
[label.set_fontweight('bold') for label in labels]

"""
ax.xaxis.grid(True, which='major', color='#666666',
              linestyle='-', linewidth=2, alpha=0.4)
ax.xaxis.grid(True, which='minor', color='#999999',
              linestyle=':', alpha=0.4)
"""
ax.yaxis.grid(True, which='major', color='#666666',
              linestyle='-', linewidth=1, alpha=0.4)

style = dict(size=18, color='gray')
for i in range(len(x)):
    for j in (x1, x2, x3):
        ax.text(x[i]+1.3, j[i]-2.5, '%.1f' %
                j[i], va='center', ha='center', **style)

font2 = {'family': 'Times New Roman',
         'weight': 'bold',
         'size': 26,
         }

ax.set_xlabel('Various Conditions', font2, labelpad=14)
ax.set_ylabel('Temperature', font2, labelpad=24)

font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 24,
         }
plt.legend(prop=font1, loc=2)

plt.title('Temperature Prediction',
          fontname="Times New Roman", fontweight='bold', fontsize=32, pad=24)

plt.savefig('C:\\Users\\h.hsieh\\Desktop\\2021.01.19.pdf',
            transparent=True)
#plt.savefig('CSVPlot/Temperature_Predction.pdf', transparent=True)
plt.show()
