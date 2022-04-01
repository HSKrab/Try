import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib
# matplotlib.use('ps')


lst = []
while 1:
    try:
        x = int(input())
        lst.append(x)
    except EOFError:
        break
#print(type(lst), lst)

xx = [5, 5, 5, 6]
d = True
xx.append(88) if not d else xx.append(-87)
print(xx)
