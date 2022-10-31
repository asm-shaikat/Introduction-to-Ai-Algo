import math
# Initial values of Alpha and Beta
MAX, MIN = float('inf'), -float('inf')

# Returns optimal value for current player
#(Initially called for root and maximizer)
def minimax(depth, nodeIndex, maximizingPlayer, scores, alpha, beta, targetDepth):

	# Terminating condition. i.e
	# leaf node is reached
	if depth == targetDepth:
		return scores[nodeIndex]

	if maximizingPlayer:
	
		best = MIN

		# Recur for left and right children
		for i in range(0, 2):
			
			val = minimax(depth + 1, nodeIndex * 2 + i, False, scores, alpha, beta, targetDepth)
			best = max(best, val)
			alpha = max(alpha, best)

			# Alpha Beta Pruning
			if beta <= alpha:
				break
		
		return best
	
	else:
		best = MAX

		# Recur for left and
		# right children
		for i in range(0, 2):
		
			val = minimax(depth + 1, nodeIndex * 2 + i, True, scores, alpha, beta, targetDepth)
			best = min(best, val)
			beta = min(beta, best)

			# Alpha Beta Pruning
			if beta <= alpha:
				break
		
		return best
	

# scores = list(map(int, input("Terminal values: ").split()))
scores = [2,3,5,9,0,1,7,5]
#fingding length of binary tree by log(x, base 2)
treeDepth = math.log(len(scores), 2)

print("The optimal value is :", minimax(0, 0, True, scores, MIN, MAX, treeDepth))
			