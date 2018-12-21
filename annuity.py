# Engineering 120 Annuity Functions

from utils import *

def pv(nper, rate, pmt):
	"""Returns the present value of an annuity

	Args:
	nper - number of periods
	rate - discount rate
	pmt - payment/present value

	>>> round(pv(2, .05, 100))
	186
	"""
	return pmt / rate * (1 - (1/(1+rate)**nper))

def fv(nper, rate, pmt):
	"""Returns the future value of an annuity

	Args:
	nper - number of periods
	rate - discount rate
	pmt - payment/present value

	>>> round(fv(4, .05, 100))
	431
	"""
	return pmt / rate * ((1+r)**nper -1)



















if __name__ == '__main__':
	import doctest
	doctest.testmod()