import matplotlib.pyplot as plt
import numpy as np

x=np.array([8,2,11,6,5,4,12,9,6,1])
y=np.array([3,10,3,6,8,12,1,4,9,14])

plt.scatter(x,y)

meanx=np.mean(x)
meany=np.mean(y)
xi=x-meanx
yi=y-meany
xyi=xi*yi
xi=xi*xi

m=sum(xyi)/sum(xi)
print('Slope : ',m)
intercept=meany-m*meanx
print("Y-Intercept : ",intercept)
print("Equation of line : \n y = {}x+{}".format(round(m,1),round(intercept,1)))
new_y=m*np.array(x)+intercept
print("new y coordinates : \n",new_y)

plt.plot(x,new_y,color='red')
plt.show()
