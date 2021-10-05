import numpy as np
import matplotlib.pyplot as plt


train_data_array = np.load('data_bak/train/P-2.npy')
test_data_array = np.load('data_bak/test/P-2.npy')

train_data = []
test_data = []

for data in train_data_array:
    train_data.append(data[0])
for data in test_data_array:
    test_data.append(data[0])

train_x = [i + 1 for i in range(len(train_data))]
test_x = [i + 1 for i in range(len(test_data))]
fig = plt.figure(figsize=(21, 9))
ax = fig.add_subplot(2, 1, 1)
bx = fig.add_subplot(2, 1, 2)
ax.plot(train_x, train_data)
bx.plot(test_x, test_data)
plt.show()
