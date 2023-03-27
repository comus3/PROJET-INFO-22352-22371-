
import time

def MAX(state, player):
	if gameOver(state):
		return utility(state, player), None

	theValue, theMove = float('-inf'), None
	for move in moves(state):
		successor = apply(state, move)
		value, _ = MIN(successor, player)
		if value > theValue:
			theValue, theMove = value, move
	return theValue, theMove

def MIN(state, player):
	if gameOver(state):
		return utility(state, player), None

	theValue, theMove = float('inf'), None
	for move in moves(state):
		successor = apply(state, move)
		value, _ = MAX(successor, player)
		if value < theValue:
			theValue, theMove = value, move
	return theValue, theMove

def timeit(fun):
	def wrapper(*args, **kwargs):
		start = time.time()
		res = fun(*args, **kwargs)
		print('Executed in {}s'.format(time.time() - start))
		return res
	return wrapper

@timeit
def next(state):
	player = currentPlayer(state)
	_, move = MAX(state, player)
	return move

state = [
	None, None, None,
	None, None, None,
	None, None, None,
]

print(next(state))