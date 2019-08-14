# Emulates a post-order processing & reversal for a topological order result
def dfs_topsort(G, s, S=None): 
	if S is None: 
		S = set()
	Stack = []
	res = []
	Stack.append(s)
	while Stack: 
		u = Stack[-1]  # peek Stack
		S.add(u)

		# if all neighbors already visited, then pop the Stack
		# if not, then choose next u not already visited
		flag = False
		for v in G[u]:
			if v not in S:
				flag = True
				u = v
				break
		if flag:  # found unvisited neighbor
			Stack.append(u)
		else:  # all already visited
			Stack.pop()
			res.append(u)
	res.reverse()
	return res


if __name__ == '__main__':
	myDAG = {'A': ['B','C'],
			 'B': ['C', 'D'],
			 'C': ['E', 'F'],
			 'D': [],
			 'E': ['D'],
			 'F': ['E'],
			 'G': ['A', 'F']}  # G is the root of myDAG

	print(dfs_topsort(myDAG, 'G'))
