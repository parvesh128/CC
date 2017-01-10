def maxConsecutive(arr):
	map = {}

	for num in arr:
		map[num] = 1

	maxCon = 0
	maxConList = []
	curCon = 0
	curConList = []
	for num in map.keys():

		if num - 1 in map:
			continue

		curCon = 1
		curConList = []
		curConList.append(num)
		temp = num + 1
		while temp in map:
			curConList.append(temp)
			curCon += 1
			temp += 1

		maxConList = maxConList if maxCon >= curCon else curConList
		maxCon = max(curCon, maxCon) 

	return (maxCon, maxConList)


arr = [1, 94, 93, 1000, 2, 92, 1001]
print maxConsecutive(arr)


