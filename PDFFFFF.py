# https://stackoverflow.com/questions/2797525/matplotlib-pdf-export-uses-wrong-font
import matplotlib.font_manager as fm
import matplotlib.pylab as pylab
import scipy
import matplotlib
matplotlib.use('cairo')

font = fm.FontProperties(
    family='yugothib', fname='C:\\Users\\h.hsieh\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\matplotlib\\mpl-data\\fonts\\ttf\\yugothib.ttf')

data = scipy.arange(5)
fig = pylab.figure()
ax = fig.add_subplot(111)
ax.bar(data, data)
ax.set_yticklabels(ax.get_yticks(), fontproperties=font)
ax.set_xticklabels(ax.get_xticks(), fontproperties=font)
pylab.savefig('foo1.pdf')
