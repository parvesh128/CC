class TreeNode:

	def __init__(self, val):
		self.val = val
		self.l = None
		self.r = None

	
def levelTraversal(root, curNode):

	queue = []
	queue.append(root)
	next_level_queue = []
	tra = []

	if curNode in queue:
		return queue[0].val

	while True:
		if len(queue) == 0:
			break

		temp = queue.pop(0)

		tra.append(temp.val)

		if temp.l is not None:
			next_level_queue.append(temp.l)

		if temp.r is not None:
			next_level_queue.append(temp.r)

		if len(queue) == 0:
			#print tra
			tra = []
			queue = next_level_queue[:]
			next_level_queue = []
			if curNode in queue:
				return queue[0].val


if __name__ == "__main__":

	root = TreeNode(1)
	root.l = TreeNode(2)
	root.r = TreeNode(3)
	#root.l.l = TreeNode(4)
	#root.l.r = TreeNode(5)
	root.r.l = TreeNode(6)
	root.r.r = TreeNode(7)

	print levelTraversal(root, root.r.r)















