
def swap(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

def partition_3_way(arr):

	top_of_bottom_group = 0
	bottom_of_top_group = len(arr) - 1

	top_middle_group = 0


	while top_middle_group <= bottom_of_top_group:
		val = arr[top_middle_group]
		if val == 0:
			swap(arr,top_of_bottom_group, top_middle_group )
			top_middle_group += 1
			top_of_bottom_group += 1
		elif val == 2:
			swap(arr, bottom_of_top_group , top_middle_group)
			bottom_of_top_group -= 1
		else:
			top_middle_group += 1

arr = [0,1,1,0,1,2,1,2,0,0,0,1]

partition_3_way(arr)

print arr
