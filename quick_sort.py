def partition(arr, start, end):
	pivot = arr[end]
	partitionidx = start

	for i in range(start, end, 1):
		if arr[i] < pivot:
			temp = arr[partitionidx]
			arr[partitionidx] = arr[i]
			arr[i] = temp
			partitionidx += 1

	arr[end] = arr[partitionidx]
	arr[partitionidx] = pivot
	return partitionidx