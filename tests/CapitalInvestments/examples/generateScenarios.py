import numpy as np
"""
script to generate scenario data for use case no. 3
"""

data = """13.3129 12.0228 0. -10.0700 -9.7767 -9.2155 -2.4372 -2.6301 0. 35.0000 33.9806 0. -18.6000 -17.0216 7.4458 5.5379 4.7605 0. -1.4400 -1.3178 0.7879 0.6783 0. 2.1000 0. -5.0300 -5.1809 -4.8835 -0.9595 -0.7563 0. -5.2500 128.1380 128.2798 0. -6.5200 2.8700  2.4705  0. 1.0747 0.8547 0.7869 0.
        21.8624 18.9040 0. -10.0700 -9.7767 -9.2155  1.7311  1.8953 0. 35.0000 33.9806 0. -18.6000 -17.0216 7.6872 3.5478 2.4095 0. -1.4400 -1.3178 6.1143 4.9364 0. 2.1000 0. -5.0300 -5.1809 -4.8835 19.6488 14.0932 0. -5.2500 137.9677 137.2397 0. -6.5200 12.6347 10.5147 0. 5.7381 4.3390 3.9302 0.
        25.9080 21.2811 0. -10.0700 -9.7767 -9.2155  4.3399  4.8291 0. 35.0000 33.9806 0. -18.6000 -17.0216 5.7428 1.3533 0.6569 0. -1.4400 -1.3178 8.6657 6.4683 0. 2.1000 0. -5.0300 -5.1809 -4.8835 28.5139 18.2305 0. -5.2500 141.9167 140.7095 0. -6.5200 16.8106 13.6791 0. 7.7351 5.6566 5.0684 0.
        """
data = list(float(val) for val in data.split())

data = np.asarray(data).reshape((3, -1))

lowRisk = [0.1667, 0.6667, 0.1666]
medRisk = [0.3333, 0.5, 0.1667]

# projects 3, 6, 15
lowIndex = [6,7,8] + [14,15,16,17] + [36, 37, 38]
# projects 1, 8, 11, 13, 16
medIndex = [0,1,2] + [20,21,22] + [28, 29, 30] + [32, 33, 34] + [39, 40, 41, 42]
# projects 2, 4, 5, 7, 9, 10, 12, 14
noIndex  = [3,4,5] + [9,10,11] + [12,13] + [18,19] + [23, 24] + [25, 26, 27] + [31] + [35]

newData = np.zeros((9,43))
prob = np.zeros(9)
for j in range(3): # low risk
  for k in range(3): # medium risk
    newData[j+k*3, lowIndex] = data[j, lowIndex]
    newData[j+k*3, noIndex] = data[0, noIndex]
    newData[j+k*3, medIndex] = data[k, medIndex]
    prob[j+k*3] = lowRisk[j] * medRisk[k]

for i in range(9):
  strOut = ' '.join(list(str(val) for val in newData[i,:]))
  print(strOut)

probStr = ' '.join(list(str(val) for val in prob))
print(prob)
