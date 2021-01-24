def equalSub(A,S,n):
	if S%2 != 0:
		return False
	else:
		# divide the sum of the whole array
		sub_sum = S//2

		# initialize DP table
		subset = ([[False for i in range(sub_sum+1)] for j in range(n+1)])

		# when the sum is 0, then the answer is true
		for i in range(n+1):
			subset[i][0] = True

		# when the subset contains no element, all the subset sum greater than 0 get answer of False
		for i in range(1,sub_sum+1):
			subset[0][i] = False

		# main loop
		for i in range(1,n+1):
			for j in range(1,sub_sum+1):
				if A[i-1] <= j:
					subset[i][j] = (subset[i-1][j] or subset[i-1][j-A[i-1]])
				elif A[i-1] > j:
					subset[i][j] = subset[i-1][j]

		return subset[n][sub_sum]


if __name__ == '__main__':
	A= [1, 1, 3, 4, 7]
	S = sum(A)
	n = len(A)
	if equalSub(A,S,n)==True:
		print('YES')
	else:
		print('NO')