import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("Sales_Records.csv")

#print name of columns:
print(dataset.columns.values)

#print 10 rows and 10 columns:
print(dataset.iloc[:10,:10])

#plot any graph of profits:
profit = dataset["Total Profit"]
item_name=dataset["Item Type"]
plt.bar(item_name,profit)
plt.title("Bar Graph for Total profit and Item Type")
plt.xlabel("Item Type")
plt.xticks(item_name, fontsize=8,rotation=45)
plt.ylabel("Total Profit")
plt.show()

#print item_type whose total cost 1000000:
total_cost = dataset["Total Cost"]
i=0
for n in total_cost:
    if(n>=1000000):
        print(item_name[i])
    i+=1
