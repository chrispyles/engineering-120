# Engineering 120 Utilities

def bid_ask(buy_orders, sell_orders):
	"""Returns the bid and ask prices from lists of limit buy and limit sell orders

	Note that this returns a 2-tuple of values, so define variables as:
		bid_price, ask_price = bid_ask(buy_orders, sell_orders)

	Args:
	buy_orders - a list of the prices of limit buy orders
	sell_orders - a list of the prices of limit sell orders

	>>> bid_ask([100, 200], [200, 400])
	(200, 200)
	"""
	return max(buy_orders), min(sell_orders)

def arbitrage(buy_orders, sell_orders):
	"""Takes in two lists and determines if an artbitrage opportunity exists

	Args:
	buy_orders - a list of the prices of limit buy orders
	sell_orders - a list of the prices of limit sell orders

	>>> arbitrage([100, 200], [200, 400])
	False
	>>> arbitrage([100, 600], [700, 400])
	True
	"""
	bid_price, ask_price = bid_ask(buy_orders, sell_orders)
	if ask_price >= bid_price:
		return False
	return True

def repeat(x, n):
	"""Returns a list of x repeated n times

	Args:
	x - value to be repeated
	n - number of times to repear

	>>> repeat(1, 5)
	[1, 1, 1, 1, 1]
	>>> repeat('a', 3)
	['a', 'a', 'a']
	"""
	return [x for _ in range(n)]

def round(x):
	"""Round x to an integer

	>>> round(3.2)
	3
	>>> round(3.7)
	4
	"""
	if x % 1 >= .5:
		return int(x // 1) + 1
	else:
		return int(x // 1)

def fv(nper, rate, amt):
	"""Returns the future value of an amount

	>>> round(fv(4, .05, 100))
	122
	"""
	return amt * (1+rate)**nper
















if __name__ == '__main__':
	import doctest
	doctest.testmod()