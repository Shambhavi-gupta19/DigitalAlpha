def binary_search(list,n):
	first = 0
	last = len(list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if list[mid] == item :
			found = True
		else:
			if item < list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found

sorted_list=[]
for x in range(10):
    sorted_list.append(input("Enter the numbers in sorted order : "))
item= input("Enter the number which is to be searched : ")

if(binary_search(sorted_list, item)):
    print("Number Found")
else:
    print("Number not Found")
