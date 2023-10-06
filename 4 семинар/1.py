import numpy as np
import matplotlib.pyplot as plt
U = [300,
325,
350,
375,
400,
425,
725,
700,
650,
600,
550,
500,
]
I = [144,
156,
170,
181,
194,
206.5,
350,
340,
319,
292,
265.2,
243.9
]
I=sorted(I)
U=sorted(U)
fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(111)
x = [144, 350]
y = np.interp(x, I, U)

plt.title('График напряжения от силы тока', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
plt.xlabel('I, A')
plt.ylabel('U, B')

ax1.scatter(I, U, marker='x')
ax1.errorbar(I, U, yerr=0.002, xerr = 0.004, color = 'k', linestyle = 'None')
ax1.plot(x, y, 'r')
ax1.grid()
slope, intercept = np.polyfit(np.log(I), np.log(U), 1)
print(slope)


plt.show()

