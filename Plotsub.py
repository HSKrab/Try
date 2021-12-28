import csv
import matplotlib.pyplot as plt
import numpy as np
import re
import matplotlib.ticker as ticker
import matplotlib.gridspec as gridspec

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

figure, ax = plt.subplots(figsize=(16.53, 11.69))
gs = gridspec.GridSpec(2, 4)

ax1 = plt.subplot(gs[0, :])
plt.bar(names, values)
plt.title('Total')

ax2 = plt.subplot(gs[1, 0])
plt.scatter(names, values)
plt.title('Graph-1')
ax3 = plt.subplot(gs[1, 1], sharey=ax2)
plt.plot(names, values)
plt.title('Graph-2')
ax4 = plt.subplot(gs[1, 2], sharey=ax2)
plt.bar(names, values)
plt.title('Graph-3')
ax5 = plt.subplot(gs[1, 3], sharey=ax2)
plt.bar(names, values)
plt.title('Graph-4')
plt.setp([ax3.get_yticklabels(), ax4.get_yticklabels(),
          ax5.get_yticklabels()], visible=False)

for axis in ['top', 'bottom', 'left', 'right']:
    ax1.spines[axis].set_linewidth(2)
    ax2.spines[axis].set_linewidth(2)
    ax3.spines[axis].set_linewidth(2)
    ax4.spines[axis].set_linewidth(2)
    ax5.spines[axis].set_linewidth(2)

ax1.tick_params(axis='both', which='both', top='on',
                right='on', direction='in', width=2)
ax2.tick_params(axis='both', which='both', top='on',
                right='on', direction='in', width=2)
ax3.tick_params(axis='both', which='both', top='on',
                right='on', direction='in', width=2)
ax4.tick_params(axis='both', which='both', top='on',
                right='on', direction='in', width=2)

#plt.subplots_adjust(wspace=0.2, hspace=0.3)

plt.suptitle('Categorical Plotting')
plt.show()
