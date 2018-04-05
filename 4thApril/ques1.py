import numpy as np

arr = np.array([['Rhia',10,20,30,40,50],
['Alan',75,80,75,85,100],
['Smith',80,80,80,90,95]])

sliced_arr=arr[0:3, 0:2]
print("Sliced Array : \n",sliced_arr)

arr[2] = ['Sam',82,79,88,97,99]
print("Updated Array : \n",arr)

arr[0][4] = 95
print("4th element of 1st row updated : \n",arr)

c = np.insert(arr, 6, (73,80,85),axis=1)
print("After insertion of column : \n",c)
