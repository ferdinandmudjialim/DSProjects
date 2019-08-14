# From BFS DFS slides
def dfs_topsort(G): 
	S = set()
	res = []
	def recurse(u): 
		if u in S: 
			return  # if u already explored, break out of recurse
		S.add(u)
		for v in G[u]: 
			recurse(v)
		res.append(u)
	for u in G: 
		recurse(u)
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

	print(dfs_topsort(myDAG))