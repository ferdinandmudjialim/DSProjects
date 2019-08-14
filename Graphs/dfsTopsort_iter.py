# From BFS DFS slides, but this doesn't work???
def iter_dfs_topsort(G):   
	S = set()  # visited-set
	Q = []
	res = []
	for u in G: 
		Q.append(u)
		while Q:
			v = Q.pop()
			if v in S: 
				continue
			S.add(v)
			Q.extend(G[v])
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

	print(iter_dfs_topsort(myDAG))