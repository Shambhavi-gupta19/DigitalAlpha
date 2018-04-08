#Question3:

import matplotlib.pyplot as plt
from scipy import stats
X=[1.45,2.20,0.75,1.23,1.25,1.25,3.09,1.99,2.00,0.78,1.32,2.25,3.15,3.85,0.52,0.99,1.38,1.75,1.22,1.75]

#Frequency Distribution table
print(stats.itemfreq(X))


#Histogram
plt.hist(X)
plt.xlabel("Price of Birthday Cards")
plt.ylabel("Frequency")
plt.show()
