import random, time, os

array = [2,1,-3,4,-1,2,1,-5,4]
def largest_sum(array):
	largest_list =[]
	while array:
		total = 0
		largest = array[0]
		for i in array:
			total += i
			if total > largest:
				largest = total
		largest_list.append(largest)
		array = array.remove(array[0])
		
	largest_value = max(largest_list)
		
	return(largest_value)
		
print(largest_sum(array))
		
		