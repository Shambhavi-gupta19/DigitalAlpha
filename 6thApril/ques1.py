import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

dataset = pd.read_excel("housing_data.xlsx")
X = stats.itemfreq(dataset)

# scatter graph
plt.scatter(X[:,0], X[:,1], color='blue')

X1m = np.mean(X[:,0])
X2m = np.mean(X[:,1])
a = 0
b = 0

for i in range(len(X[:,0])):
    a = a + ((X[i][0]-X1m)*(X[i][1]-X2m))
    b = b + (X[i][0]-X1m)**2

cf = a/b
con = X2m - cf*X1m

regress = []
for i in range(len(X[:,0])):
    regress.append(con+(cf*X[i][0]))
    
# regression line
plt.plot(X[:,0], regress, color = 'red')
plt.show()

# histogram
plt.hist(dataset)
plt.show()
