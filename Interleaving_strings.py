count = 0
memo = {}

def interLeave(s1, s2):
	return interLeaveImpl(s1, s2, 0, 0)


def interLeaveImpl(s1, s2, l1, l2):

	global count, memo
	count += 1

	if s1[l1:] in memo and s2[l2:] in memo[s1[l1:]]:
		return memo[s1[l1:]][s2[l2:]]

	if l1 == len(s1) and l2 == len(s2):
		return ['']

	newfirstSet = []
	if l1 < len(s1):
		firstSet = interLeaveImpl(s1, s2, l1 + 1 , l2)
		for string in firstSet:
			newfirstSet.append(s1[l1] + string)


	newSecondSet = []
	if l2 < len(s2):
		secondSet = interLeaveImpl(s1, s2, l1, l2 + 1)
		for string in secondSet:
			newSecondSet.append(s2[l2] + string)




	#print newfirstSet
	#print newSecondSet
	ret = list(set(newfirstSet + newSecondSet))

	#print str(ret) + '\n'
	
	if s1[l1:] not in memo:
		memo[s1[l1:]] = {}

	memo[s1[l1:]][s2[l2:]] = ret

	return ret


print interLeave('abcdel', 'fghijm')
print count
#print memo