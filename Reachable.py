class Reachibility:
	memo = {}

	@staticmethod
	def isReachable(x, y, dx, dy):
		if x == dx and y == dy:
			return True

		if (x > 0 and y > 0) and (x > dx or y > dy):
			return False

		memo = Reachibility.memo

		if (x, y) in memo and (dx, dy) in memo[(x, y)]:
			return memo[(x, y)][(dx, dy)]

		ret = Reachibility.isReachable(x + y, y, dx, dy) or\
			Reachibility.isReachable(x, y + x, dx, dy)

		if (x, y) not in memo:
			memo[(x, y)] = {}

		memo[(x, y)][(dx, dy)] = ret

		return ret


if __name__ == '__main__':
	print Reachibility.isReachable(1, 4, 5, 9)


