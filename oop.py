from utils import *

class Problem():

	functions = {'nper':nper_annuity, 'rate':rate_annuity, 'pv':pv_annuity, 'pmt':pmt_annuity, 'fv':fv_annuity}

	def __init__(self, find):
		self.find = find

	def __repr__(self):
		result = 'NPER   |   RATE   |   PV   |   PMT   |   FV\n'
		result += f'{self.nper}   |   {self.rate}   |   {self.pv}   |   {self.pmt}   |   {self.fv}'
		return result

	def nper(self, nper):
		self.nper = nper
		return self

	def rate(self, rate):
		self.rate = rate
		return self

	def pv(self, pv):
		self.pv = pv
		return self

	def pmt(self, pv):
		self.pmt = pmt
		return self

	def fv(self, fv):
		self.fv = fv
		return self

	def compute(self):
		if self.find == 'nper':
			return functions[self.find](self.rate, self.pv, self.pmt, self.fv)
