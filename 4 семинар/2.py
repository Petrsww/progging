import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
fig = plt.figure()
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)
values1 = np.random.normal(0, 100, 500000)
values2 = np.random.normal(0, 100, 1000000)
values3 = np.random.normal(0, 100, 100000000)
ax1.hist(values1, 100)
ax1.grid()

ax2.hist(values2, 300)
ax2.grid()

ax3.hist(values3, 500)
ax3.grid()

fig.show()
