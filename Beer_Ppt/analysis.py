import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_excel("Book1.xlsx")
week=np.array(dataset['Week'])
price_12pk=np.array(dataset['PRICE 12PK'])
price_18pk=np.array(dataset['PRICE 18PK'])
price_30pk=np.array(dataset['PRICE 30PK'])
case_12pk=np.array(dataset['CASES 12PK'])
case_18pk=np.array(dataset['CASES 18PK'])
case_30pk=np.array(dataset['CASES 30PK'])

plt.scatter(week,price_12pk)
A = np.vstack([week, np.ones(len(week))]).T

m, c = np.linalg.lstsq(A, price_12pk)[0]
plt.plot(week, m*week + c, 'r')
print("y= {}x+{}".format(round(m,2),round(c,2)))
plt.title("Week vs Price_12PK")
plt.xlabel("WEEK")
plt.ylabel("PRICE_12PK")
plt.legend()
plt.show()

plt.scatter(week,price_18pk)
m, c = np.linalg.lstsq(A, price_18pk)[0]
plt.plot(week, m*week + c, 'r')
print("y= {}x+{}".format(round(m,2),round(c,2)))
plt.title("Week vs Price_18PK")
plt.xlabel("WEEK")
plt.ylabel("PRICE_18PK")
plt.show()

plt.scatter(week,price_30pk)
m, c = np.linalg.lstsq(A, price_30pk)[0]
plt.plot(week, m*week + c, 'r')
print("y= {}x+{}".format(round(m,2),round(c,2)))
plt.title("Week vs Price_30PK")
plt.xlabel("WEEK")
plt.ylabel("PRICE_30PK")
plt.show()


plt.scatter(price_12pk,case_12pk)
B = np.vstack([price_12pk,np.ones(len(price_12pk))]).T
m, c = np.linalg.lstsq(B, case_12pk)[0]
plt.plot(price_12pk, m*price_12pk + c, 'r')
print("y= {}x+{}".format(round(m,2),round(c,2)))
plt.title("Price_12pk vs Case_12PK")
plt.xlabel("PRICE_12pk")
plt.ylabel("CASE_12PK")
plt.show()

plt.scatter(price_18pk,case_18pk)
C = np.vstack([price_18pk,np.ones(len(price_18pk))]).T
m, c = np.linalg.lstsq(C, case_18pk)[0]
plt.plot(price_18pk, m*price_18pk + c, 'r')
print("y= {}x+{}".format(round(m,2),round(c,2)))
plt.title("Price_18pk vs Case_18PK")
plt.xlabel("PRICE_18pk")
plt.ylabel("CASE_18PK")
plt.show()

plt.scatter(price_30pk,case_30pk)
D = np.vstack([price_30pk,np.ones(len(price_30pk))]).T
m, c = np.linalg.lstsq(D, case_30pk)[0]
plt.plot(price_30pk, m*price_30pk + c, 'r')
print("y= {}x+{}".format(round(m,2),round(c,2)))
plt.title("Price_30pk vs Case_30PK")
plt.xlabel("PRICE_30pk")
plt.ylabel("CASE_30PK")
plt.show()

print("Correlation between case_12pk and price_12pk")
print(np.corrcoef(case_12pk,price_12pk))
print("Correlation between case_18pk and price_18pk")
print(np.corrcoef(case_18pk,price_18pk))
print("Correlation between case_30pk and price_30pk")
print(np.corrcoef(case_30pk,price_30pk))
