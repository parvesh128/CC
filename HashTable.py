class Hasher:

	class LLNode:

		def __init__(self, K, V):
			self.key = K
			self.val = V
			self.n = None
			self.p = None

	def __init__(self, capacity):
		self.arr = [None]*capacity
		self.capacity = capacity

	def put(self, key, val):
		llnode = self._getNodeForKey(key)

		if llnode is not None:
			llnode.val = val
			return

		llnode = self.LLNode(key, val)

		idx = self._getIndexForKey(key)

		cur_head = self.arr[idx]

		if cur_head is not None:
			llnode.n = cur_head
			cur_head.p = llnode

		self.arr[idx] = llnode

	def remove(self, key):
		llnode = self._getNodeForKey(key)

		if llnode is None:
			return

		if llnode.p is not None:
			llnode.p.n = llnode.n
		else:
			idx = self._getIndexForKey(key)
			self.arr[idx] = llnode.n

		if llnode.n is not None:
			llnode.n.p = llnode.p

	def get(self, key):
		llnode = self._getNodeForKey(key)

		return None if llnode is None else llnode.val

	def _getNodeForKey(self, key):
		idx = self._getIndexForKey(key)

		cur = self.arr[idx]

		while cur is not None:
			if cur.key == key:
				return cur
			cur = cur.n

		return None


	def _getIndexForKey(self, key):
		return abs(len(str(key)) % self.capacity)

	def __repr__(self):
		ret = ''

		for idx, item in enumerate(self.arr):
			if item is None:
				continue

			if len(ret) != 0:
				ret = ret + '\n'

			ret = ret + str(idx) + ' --> '

			cur = item

			while cur is not None:
				ret = ret + ' ' + str((cur.key, cur.val))
				cur = cur.n

		return ret

	__str__ = __repr__


if __name__ == '__main__':
	hasher = Hasher(5)

	hasher.put('a', 1)
	hasher.put('b',2)
	hasher.put('aa',3)
	hasher.put('aaa',4)
	hasher.put(1,5)
	hasher.put('2ab',6)
	hasher.put('2113', 546)
	hasher.put('12345', 3434)

	print hasher

	print ('***********')

	hasher.remove('a')

	print hasher