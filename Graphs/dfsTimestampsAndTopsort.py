# From BFS DFS slides, but changed to work? 
# This is just dfs but with preorder and postorder timestamps 
# Can be useful to tell if one node is a descendant of another
def dfs(G, s, d, f, S=None, t=0): 
	if S is None: 
		S = set()
	d[s] = t; t +=1  # set discover time
	S.add(s)
	for u in G[s]: 
		if u in S:  # already visited. skip.
			continue
		t = dfs(G, u, d, f, S, t)
	f[s] = t; t += 1  # set finish time
	return t  # return timestamp

if __name__ == '__main__':
	myDAG = {'A': ['B','C'],
			 'B': ['C', 'D'],
			 'C': ['E', 'F'],
			 'D': [],
			 'E': ['D'],
			 'F': ['E'],
			 'G': ['A', 'F']}  # G is the root of myDAG

	discover = {}
	finished = {}
	print(dfs(myDAG, 'G', discover, finished))
	print(discover)
	print(finished)

	# sorts nodes by increasing discovery time (from a dictionary)
	topsort = [k for k,v in sorted(finished.items(), key=lambda entry: entry[1])] 
	topsort.reverse()  # for top sorting, must reverse from order of finish times
	print(topsort)