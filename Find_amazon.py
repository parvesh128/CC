
class Retval:

	def __init__(self, numPaths, points):
		self.numPaths = numPaths
		self.points = points

	def __add__(self, other):
		numPaths = self.numPaths + other.numPaths
		points = self.points + other.points

		return Retval(numPaths, points)

def isInBoundsAndNext(mat, visited, r, c, rows, cols, char):

	if r >= 0 and c >=0 and r < rows and c < cols and not visited[r][c] and mat[r][c] == char:
		return True
	return False

def DFS(r, c, rows, cols, mat, visited, string, points):


	visited[r][c] = True

	if len(string) == 0:
		return Retval(1, points)

	left_paths = Retval(0,[])
	if isInBoundsAndNext(mat, visited, r, c-1, rows, cols, string[0]):
		temp_points = points[:]
		temp_points.append((r,c-1))
		left_paths = DFS(r, c-1, rows, cols, mat, visited, string[1:], temp_points)

	right_paths = Retval(0,[])
	if isInBoundsAndNext(mat, visited, r, c+1, rows, cols, string[0]):
		temp_points = points[:]
		temp_points.append((r,c+1))
		right_paths = DFS(r, c+1, rows, cols, mat, visited, string[1:], temp_points)

	top_paths = Retval(0,[])
	if isInBoundsAndNext(mat, visited, r-1, c, rows, cols, string[0]):
		temp_points = points[:]
		temp_points.append((r-1,c))
		top_paths = DFS(r-1, c, rows, cols, mat, visited, string[1:], temp_points)

	bottom_paths = Retval(0,[])
	if isInBoundsAndNext(mat, visited, r+1, c, rows, cols, string[0]):
		temp_points = points[:]
		temp_points.append((r+1,c))
		top_paths = DFS(r+1, c, rows, cols, mat, visited, string[1:], temp_points)


	total_paths = left_paths + right_paths + top_paths + bottom_paths
	return total_paths







def findStrings(mat):

	rows = len(mat)
	cols = len(mat[0])


	


	startPoints = []
	numPaths = Retval(0, [])
	for r in range(rows):
		for c in range(cols):
			if mat[r][c] == 'A':
				startPoints.append((r,c))

	print startPoints
	for point in startPoints:
		r, c = point
		visited = [[False for col in range(cols)] for row in range(rows)]

		if (r,c) in numPaths.points:
			continue

		numPaths = numPaths + DFS(r,c, rows, cols, mat, visited, 'MAZON', [(r,c)])

	print numPaths.numPaths
	print numPaths.points


mat = [['B','B','A','B','B','N'], 
	   ['B','B','M','B','B','O'], 
	   ['B','B','A','B','B','Z'], 
	   ['N','O','Z','B','B','A'], 
	   ['B','B','B','B','B','M'], 
	   ['B','B','B','B','B','A']]

findStrings(mat)






