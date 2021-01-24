
class item:
	def __init__(w,v):
		self.weight = w
		self.value = v
	def getWeight():
		return self.weight
	def getValue():
		return self.value
	def setWeight(w):
		self.weight = w
	def setValue(v):
		self.value = v


def knapsack(w,v, n, W):
	# intialize table of size n x n^2
	KS = [[0 for j in range(n**2+1)] for i in range(n+1)]
	for i in range(1,n**2+1):
		KS[0][i] = float('inf')


	for i in range(1,n+1):
		for j in range(n**2+1):
			if v[i-1] <= j:
				KS[i][j] = min(KS[i-1][j],w[i-1]+KS[i-1][j-v[i-1]])
			else:
				KS[i][j] = KS[i-1][j]

# 		solution lies in the nth row, so we traverse to find the biggest v, with the value in the cell less or equal to W
	max_v = 0
	prev = None
	for i in range(n**2+1):
		if KS[n][i] > W:
			return i-1
		else:
			continue


if __name__ == '__main__':
	val = [2, 2, 3,1]
	wt = [10, 20, 30,40]
	W = 50
	n = len(val)
	print(knapsack(wt,val,n,50))








