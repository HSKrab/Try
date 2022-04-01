# https://pyecontech.com/2020/03/27/python%E6%95%99%E5%AD%B8-%E5%A6%82%E4%BD%95%E8%A7%A3%E6%B1%BAmatplotlib%E4%B8%AD%E6%96%87%E4%BA%82%E7%A2%BC%E5%95%8F%E9%A1%8C/


import matplotlib.font_manager
import matplotlib
print(matplotlib.__file__)

# C:\Users\Hsieh\AppData\Local\Programs\Python\Python39\Lib\site-packages\matplotlib\mpl-data\fonts\ttf
# C:\Users\Hsieh\.matplotlib

a = sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])

for i in a:
    print(i)
