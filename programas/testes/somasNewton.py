from sympy import *
import numpy as np

def assembleEquation(coeff):
	##Assemble equation
	exp = len(coeff)-1
	x = Symbol('x')
	y = 0
	for i in coeff:
		y = y + i*x**exp
		exp = exp - 1
	#print('y:', y)
	return x, y
	
def calculateDerivative(y, x):
	##Derivative calculation
	yDer = y.diff(x)
	#print('yDer:', yDer)
	##Set a value vector that is applied to the derivative, returning a numpy
	f = lambdify(x, yDer, 'numpy')
	return yDer, f

def calculateNewtonSumPositive(y, yDer, kNewton):
	##Improper polynomial division and Newton´s sum
	yTerms = [[float(z) for z in term.as_coeff_exponent(x)] for term in y.as_ordered_terms()]
	yTerms.sort(key=lambda z: -z[1])
	yTerms = np.array(yTerms)
	#print('coefficient/exponent pairs (sorted by exponents) of y:', yTerms)
	divisor = yTerms[0,0]
	eDivisor = yTerms[0,1]
	rest_yDer = yDer
	polynomial = 0
	kNewton = kNewton+1
	for k in range(kNewton):
		rest_yTerms = [[float(zDer) for zDer in term.as_coeff_exponent(x)] for term in rest_yDer.as_ordered_terms()]
		rest_yTerms.sort(key=lambda zDer: -zDer[1])
		rest_yTerms = np.array(rest_yTerms)
		#print('coefficient/exponent pairs (sorted by exponents) of yDer:', rest_yTerms)
		dividend = rest_yTerms[0,0]
		eDividend = rest_yTerms[0,1]
		q = dividend/divisor
		e = int(eDivisor - eDividend)
		#print('data:', k, e, q, divisor, dividend)
		polynomial = polynomial + q*(x**(-e))
		subtrahend = expand(q*y*(x**(-e)))
		#print('subtrahend', subtrahend)
		rest_yDer = rest_yDer - subtrahend
		#print('rest_yDer:', rest_yDer)
		#print('polynomial:', polynomial)
		if kNewton == e: 
			sumKNewton = q
			break
		if kNewton < e:
			sumKNewton = 0
			break
	return sumKNewton, polynomial
	
def calculateNewtonSum(y, yDer, kNewton):
	if kNewton >=0: 
		sumKNewton, polynomial = calculateNewtonSumPositive(y, yDer, kNewton)
		return sumKNewton
	else:
		deg = degree(y, gen=x)
		#print('deg', deg)
		sumKNewton, polynomial = calculateNewtonSumPositive(y, yDer, deg-1)
		#print('y:', y)
		#print('polynomial:', polynomial)
		termsY = [[float(zDer) for zDer in term.as_coeff_exponent(x)] for term in y.as_ordered_terms()]
		termsY.sort(key=lambda zDer: -zDer[1])
		termsY = np.array(termsY)
		termsPolynomial = [[float(zDer) for zDer in term.as_coeff_exponent(x)] for term in polynomial.as_ordered_terms()]
		termsPolynomial.sort(key=lambda zDer: -zDer[1])
		termsPolynomial = np.array(termsPolynomial)
		##Get y coefficients
		yCoeff = []
		for i in range(deg+1):
			mask = (i == termsY[:,1])
			if any(mask):
				yCoeff = yCoeff + [termsY[mask][0,0]]
			else:
				yCoeff = yCoeff + [0]
		yCoeff = np.array(yCoeff)	
		##Get polynomial coefficients
		polCoeff = []
		for i in range(1, deg+1):
			mask = (-i == termsPolynomial[:,1])
			if any(mask):
				polCoeff = polCoeff + [termsPolynomial[mask][0,0]]
			else:
				polCoeff = polCoeff + [0]
		polCoeff = np.array(polCoeff)
		sumKNewton = 0
		for i in range(-kNewton):
			#print('yCoeff:', yCoeff, yCoeff[1:])
			#print('polCoeff:', polCoeff)
			sumBase = np.sum(np.multiply(yCoeff[1:], polCoeff))/(-yCoeff[0])
			polCoeff = np.append([sumBase], polCoeff[:-1], axis=0)
			sumKNewton = sumBase
		return sumKNewton

##################################################################
#Coefficients of the expression and kNewton
coeff = [1,-7,2,-21] #from higher exponents to lower
kNewton = -2
##################################################################
x, y = assembleEquation(coeff)
#print('y:', y)
yDer, f = calculateDerivative(y, x)
#print('yDer:', yDer)
##Calculate derivative to specific points
#points = np.array([0,1])
#print('derivative in certain points:', points, f(points))
##Polynomial division
#q, r = div(yDer:, y, domain='ZZ')
#print('quocient:', q)
#print('rest:', r)
###
sumKNewton = calculateNewtonSum(y, yDer, kNewton)
print('sumKNewton:', kNewton, '->', sumKNewton)