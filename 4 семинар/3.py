import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
df = pd.read_csv('iris_data.csv')
a = list(df['Species'])
ax1.pie([a.count('Iris-setosa'), a.count('Iris-versicolor'), a.count('Iris-virginica')], labels = ['Iris-setosa','Iris-versicolor','Iris-virginica'])
ax1.set_title('Species')
b = list(df['PetalLengthCm'])
l1, l2, l3=0, 0, 0
for i in range(len(b)):
    if b[i]<1.2:
        l1+=1
    if b[i]>1.5:
        l3+=1
    else:
        l2+=1
ax2.pie([l1, l2, l3], labels = ['<1.2','>1.2 and <1.5','>1.5'])
ax2.set_title('PetalLengthCm')
fig.show()
