from datascience import *
import numpy as np
from tkinter import *


# some random functions

def bid_ask(buy_orders, sell_orders):
	'''Returns the bid and ask prices from lists of limit buy and limit sell orders

	Note that this returns a 2-tuple of values, so define variables as:
		bid_price, ask_price = bid_ask(buy_orders, sell_orders)

	Args:
	buy_orders - a list of the prices of limit buy orders
	sell_orders - a list of the prices of limit sell orders'''
	return max(buy_orders), min(sell_orders)

def arbitrage(buy_orders, sell_orders):
	'''Takes in two lists and determines if an artbitrage opportunity exists

	Args:
	buy_orders - a list of the prices of limit buy orders
	sell_orders - a list of the prices of limit sell orders'''
	bid_price, ask_price = bid_ask(buy_orders, sell_orders)
	if ask_price >= bid_price:
		return False
	return True

def repeat(x, n):
	'''Returns a list of x repeated n times

	Args:
	x - value to be repeated
	n - number of times to repear'''
	return [x for _ in range(n)]





# financial functions

def npv(s):
	'''Takes a sequence of cash flows and returns the net present value
	
	Args:
	s - list of values'''
	return sum(s)

def npv_stream(rate, s):
	'''Takes a sequence of cash flows for a certain number of years and returns the NPV

	Args:
	rate - discount rate
	s - list of values (beginning at year 0)'''

	present_values = [i/(1+rate)**j for i,j in zip(s, range(len(s)))]
	return sum(present_values)


def present_value(rate, nper, pmt):
	'''Returns the present value of an amount

	Args:
	rate - discount rate
	nper - number of periods
	pmt - payment/present value'''
	return pmt / (1+rate)**nper

def pv_stream(rate, start_n, end_n, s):
	'''Takes a sequence of cash flows and a number of periods and returns the present value
	
	Args:
	rate - discount rate
	start_n - starting period number
	end_n - ending period number (inclusive)
	s - a list of values'''
	return sum([present_value(rate, j, i) for i,j in zip(s, range(start_n, end_n+1))])

def pv_perpetuity(rate, pmt):
	'''Returns the present value of a perpetuity

	Args:
	rate - discount rate
	pmt - payment/present value'''
	return pmt / rate



def pv_g_perpetuity(rate, g_rate, pmt):
	'''Returns the present value of a growing perpetuity

	Args:
	rate - discount rate
	g_rate - rate of growth of perpetuity
	pmt - payment/present value'''
	return pmt / (rate - g_rate)

def pv_g_annuity(rate, g_rate, nper, pmt):
	'''Returns the present value of a growing annuity

	Args:
	rate - discount rate
	g_rate - rate of growth of perpetuity
	nper - number of periods
	pmt - payment/present value'''
	return pmt / (rate - g_rate) * (1 - ((1+g_rate)/(1+rate)**nper))

def ear(apr, nper):
	'''Returns the expected annual return for a given APR

	Args:
	apr - annual percent return
	nper - number of compounding periods per year'''
	return (1+(apr/nper))**nper - 1

def real_IR(nominal_IR, inflation_rate):
	'''Returns the real interest rate

	Args:
	nominal_IR - nominal interest rate
	inflation_rate - inflation rate'''
	return (nominal_IR - inflation_rate) / (1 + inflation_rate)

def cpn_pmt(coupon_rate, face_value, n_pmts_per_year):
	'''Returns the coupon payment amount for a bond

	Args:
	coupon_rate - coupon rate
	face_value - face value of the bond
	n_pmts_per_year - number of coupon payments per year'''
	return coupon_rate * face_value / n_pmts_per_year

def ytm(face_value, price, nper):
	'''Returns the yield to maturity of a bond

	Args:
	face_value - face value of a bond
	price - price of the bond
	noer - term of the bond'''
	return (face_value/price)**(1/nper) - 1

def zcb_price(ytm, face_value, nper):
	'''Returns the price of a zero-coupon bond

	Args:
	ytm - yield to maturity of the bond
	face_value - face value of the bond
	nper - term of the bond'''
	return face_value / (1+ytm)**n

def bond_price(coupon, ytm, face_value, nper):
	'''Returns the price of a coupon bond

	Args:
	coupon - the coupon payment of the bond
	ytm - yield to maturity of the bond
	face_value - face value of the bond
	nper - term of the bond'''
	return pv_annuity(ytm, nper, coupon) + present_value(ytm, nper, face_value)




# annuity formulae for problem function

def nper_annuity(rate, pv, pmt, fv=0):
	'''Returns the number of periods for an annuity

	Args:
	rate - discount rate
	pv - present value
	pmt - payment
	fv=0 - future value'''
	return np.nper(rate, pmt, pv, fv)

def rate_annuity(nper, pv, pmt, fv=0):
	'''Returns the discount rate of an annuity
	
	Args:
	nper - number of periods
	pv - present value
	pmt - payment amount
	fv=0 - future value'''
	return np.rate(nper, pmt, pv, fv)

def pmt_annuity(nper, rate, pv, fv=0):
	'''Returns the number of periods for an annuity

	Args:
	nper - number of periods
	rate - interest rate
	pv - present value
	fv=0 - future value'''
	return pv * rate / (1-(1/(1+rate)**nper))

def fv_annuity(nper, rate, pv, pmt=0):
	'''Returns the number of periods for an annuity

	Args:
	nper - number of periods
	rate - interest rate
	pv - present value
	pmt - payment amount'''
	if pmt == 0:
		return pv * (1+rate)**nper
	return pmt / rate * ((1+rate)**nper - 1)





# formulae for perpetuities

def rate_perpetuity(pv, pmt):
	'''Determines the discount rate of a perpetuity.

	Args:
	pv - present value of perpetuity
	pmt - payment amount'''
	return pmt / pv

def pmt_perpetuity(rate, pv):
	'''Determines the payment amount of a perpetuity.

	Args:
	rate - discount rate
	pv - present value of perpetuity'''
	return rate * pv



# create a window to run problems with Tkinter

def problem(p_type='', f_nper=False, f_rate=False, f_pv=False, f_pmt=False, f_fv=False):
	'''Creates an interactive window using the tkinter library that is useful in solving
	financial problems. Based on the arguments, can be used to find nper, rate, pv, pmt,
	or fv.

	Args:
	type='' - determines formulae to be used; annuity by default if undefined
	f_nper=False - set to True to find nper
	f_rate=False - set to True to find rate
	f_pv=False - set to True to find present value
	f_pmt=False - set to True to find payment
	f_fv=False - set to True to find future value'''

	window = Tk()

	nper = Label(window, text="NPER")
	rate = Label(window, text="RATE")
	pv = Label(window, text="PV")
	pmt = Label(window, text="PMT")
	fv = Label(window, text="FV")

	e_nper = Entry(window, textvariable=StringVar())
	e_rate = Entry(window, textvariable=StringVar())
	e_pv = Entry(window, textvariable=StringVar())
	e_pmt = Entry(window, textvariable=StringVar())
	e_fv = Entry(window, textvariable=StringVar())


	def run():
		if p_type == 'perpetuity':
			if f_rate:
				given_pv = float(e_pv.get())
				given_pmt = float(e_pmt.get())
				answer = rate_perpetuity(given_pv, given_pmt)
				result = Label(window, text="%s" %(answer))
				result.pack()

			elif f_pv:
				given_rate = float(e_rate.get())
				given_pmt = float(e_pmt.get())
				answer = pv_perpetuity(given_rate, given_pmt)
				result = Label(window, text="%s" %(answer))
				result.pack()

			elif f_pmt:
				given_rate = float(e_rate.get())
				given_pv = float(e_pv.get())
				answer = pv_perpetuity(given_rate, given_pv)
				result = Label(window, text="%s" %(answer))
				result.pack()

		else:
			if f_nper:
				given_rate = float(e_rate.get())
				given_pv = float(e_pv.get())
				given_pmt = float(e_pmt.get())
				given_fv = float(e_fv.get())
				answer = nper_annuity(given_rate, given_pv, given_pmt, given_fv)
				result = Label(window, text="%s" %(answer))
				result.pack()

			elif f_rate:
				given_nper = float(e_nper.get())
				given_pv = float(e_pv.get())
				given_pmt = float(e_pmt.get())
				given_fv = float(e_fv.get())
				answer = rate_annuity(given_nper, given_pv, given_pmt, given_fv)
				result = Label(window, text="%s" %(answer))
				result.pack()

			elif f_pv:
				given_nper = float(e_nper.get())
				given_rate = float(e_rate.get())
				given_pmt = float(e_pmt.get())
				given_fv = float(e_fv.get())
				answer = pv_annuity(given_nper, given_rate, given_pmt, given_fv)
				result = Label(window, text="%s" %(answer))
				result.pack()

			elif f_pmt:
				given_nper = float(e_nper.get())
				given_rate = float(e_rate.get())
				given_pv = float(e_pv.get())
				given_fv = float(e_fv.get())
				answer = pmt_annuity(given_nper, given_rate, given_pv, given_fv)
				result = Label(window, text="%s" %(answer))
				result.pack()

			elif f_fv:
				given_nper = float(e_nper.get())
				given_rate = float(e_rate.get())
				given_pv = float(e_pv.get())
				given_pmt = float(e_pmt.get())
				answer = fv_annuity(given_nper, given_rate, given_pv, given_pmt)
				result = Label(window, text="%s" %(answer))
				result.pack()


	b = Button(window, text="Find", command=run)

	if p_type == 'perpetuity':
		if f_rate:
			pv.pack()
			e_pv.pack()
			pmt.pack()
			e_pmt.pack()
			b.pack()

			window.mainloop()


		elif f_pv:
			rate.pack()
			e_rate.pack()
			pmt.pack()
			e_pmt.pack()
			b.pack()

			window.mainloop()


		elif f_pmt:
			rate.pack()
			e_rate.pack()
			pv.pack()
			e_pv.pack()
			b.pack()

			window.mainloop()


	else:
		if f_nper:
			rate.pack()
			e_rate.pack()
			pv.pack()
			e_pv.pack()
			pmt.pack()
			e_pmt.pack()
			fv.pack()
			e_fv.pack()
			b.pack()

			window.mainloop()


		elif f_rate:
			nper.pack()
			e_nper.pack()
			pv.pack()
			e_pv.pack()
			pmt.pack()
			e_pmt.pack()
			fv.pack()
			e_fv.pack()
			b.pack()

			window.mainloop()


		elif f_pv:
			nper.pack()
			e_nper.pack()
			rate.pack()
			e_rate.pack()
			pmt.pack()
			e_pmt.pack()
			fv.pack()
			e_fv.pack()
			b.pack()

			window.mainloop()


		elif f_pmt:
			nper.pack()
			e_nper.pack()
			rate.pack()
			e_rate.pack()
			pv.pack()
			e_pv.pack()
			fv.pack()
			e_fv.pack()
			b.pack()

			window.mainloop()


		elif f_fv:
			nper.pack()
			e_nper.pack()
			rate.pack()
			e_rate.pack()
			pv.pack()
			e_pv.pack()
			pmt.pack()
			e_pmt.pack()
			b.pack()

			window.mainloop()























