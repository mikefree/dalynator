'''
Defining functions for calculating YLLs and YLDs
# Michael Freeman
# June 2, 2011
'''

# Define a function for calculating ylls.
def yll(a, g, n, B=.04, c=.1658, K=1, r=.03):
	'''
	Returns YLL for n individuals gender 'g' who died at age a
	a = age, no default.
	g= gender, no default.
	n = number of deaths, no default.
	B = .04 (age-weighting)
	c=.1658 (constant)'
	K = 1 (age-weighting modulation factor)
	l = 82.5 (standard life expectancy)
	r = .03 (discount rate
	'''
	# Set the life expectancy based on the gender input:
	if g=='males':
		l = 80
	if g=='females':
		l=82.5
	# Calculate life expectancy at age a (L) as the standard life expectancy (l) minus the number of years lived (a).
	L = l - a
	value = (K*C*e**(r*a)/((r+B)**2)*((e**(-(r+B)*(L+a)))*(-(r+B)*(L+a) - 1) - e**(-(r+B)*a)*(-(r+B)*a - 1)) + ((1-K)/r)*(1-e**(-r*L)))*n
	return value

	''' Run through an example, using the standard values '''
	
# Choose age
a = 25
# Choose gender
g = 'females'
# Choose number of deaths
n = 10000
# Test the function:
yll(a, g, n)
	
# Define a function to calculate ylds.

def yld(a, D, Len, n, B=.04, C=.1658, K=1, r=.03):
	''' 
	Returns YLDs for n individuals age 'a' who have a disability with weight 'D' and length 'Len'
	a = age of onset, no default.
	D = Disability weight, no default.
	Len = Length of time with disability, no default.
	n = number of people with disability, no default.
	B = .04 (age-weighting)
	c = .1658 (constant)'
	K = 1 (age-weighting modulation factor)
	r = .03 (discount rate
	'''
	value = D*((K*C*e**(r*a)/((r+B)**2)*((e**(-(r+B)*(L+a)))*(-(r+B)*(Len+a) - 1) - e**(-(r+B)*a)*(-(r+B)*a - 1)) + ((1-K)/r)*(1-e**(-r*Len))))*n
	return value
	
	''' Run through an example, using the standard values '''


# Choose disability weight for the example.
D = .5

# Choose a length of disability 
len = 25

# Choose number of disabled
n = 10000
yld(a, D, len, n)
	