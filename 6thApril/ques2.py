import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_excel("ca_result.xlsx")
year = dataset.iloc[1:,0]
group1 = dataset.iloc[1:,3]
group2 = dataset.iloc[1:,6]
bothg = dataset.iloc[1:,9]
plt.plot(year,group1,label="Group 1")
plt.plot(year,group2,label="Group 2")
plt.plot(year,bothg,label="Both Group")
plt.xlabel("Year")
plt.ylabel("Pass %")

plt.show()
