# https://ithelp.ithome.com.tw/articles/10197029

from sklearn import tree

features = [[150, 1], [170, 1], [130, 0], [140, 0]]
labels = [0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

wantPredict = clf.predict([[120, 0]])
if wantPredict == [1]:
    print('This is an apple')
elif wantPredict == [0]:
    print('This is an orange')
