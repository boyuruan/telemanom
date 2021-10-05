import numpy as np
import matplotlib.pyplot as plt
from datetime import date
from dateutil.relativedelta import relativedelta
import pandas as pd


start_date = date(2017, 3, 1)
end_date = date(2017, 3, 31)
path_to_file = '/Users/boyuruan/Documents/check_quality/Data/12094932/'
data = []
while start_date <= end_date:
    if start_date.strftime('%w') in ['0', '6']:
        start_date += relativedelta(days=+1)
        continue
    with open(path_to_file + start_date.strftime('%Y%m%d') + '_flow.txt') as f:
        for line in f:
            data.append(float(line))
    start_date += relativedelta(days=+1)
data = np.array(data)
D = pd.DataFrame(data)
D = D.interpolate(method='linear')
data = D.values.reshape(1, -1)[0]
X = []
for d in data:
    X.append([d])
X = np.array(X)
fig = plt.figure(figsize=(21, 9))
ax = fig.add_subplot(2, 1, 1)
bx = fig.add_subplot(2, 1, 2)
print(len(X) / 480)
ax.plot(range(len(X[0:10*480])), X[0:10*480])
bx.plot(range(len(X[20 * 480:])), X[20*480:])
plt.show()
np.save('/Users/boyuruan/OneDrive/Code/telemanom/data/train/X-1.npy',
        X[0:10*480])
np.save(
    '/Users/boyuruan/OneDrive/Code/telemanom/data/test/X-1.npy', X[20 * 480:])
