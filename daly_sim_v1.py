# Defining functions for calculating YLLs and YLDs
# Michael Freeman
# June 2, 2011

# Define a function for calculating ylls.
def yll(a, B, c, K, L r):
# Calculate life expectancy at age a (L) as the standard life expectancy (l) minus the number of years lived (a).
	L = l - a
	value = K*C*e**(r*a)/((r+B)**2)*((e**(-(r+B)*(L+a)))*(-(r+B)*(L+a) - 1) - e**(-(r+B)*a)*(-(r+B)*a - 1)) + ((1-K)/r)*(1-e**(-r*L))
	return value

	######## Run through an example, using the standard values ##########
	
# Set standard life expectancy, 'l'
l = 82.5

# Set discount rate, 'r'
r = .03

# Set the age-weighting modulation factor, 'K'
K = 1

# Set the parameter from the age-weighting function, 'B'
B=.04

# Set the constant, 'C'
C = .1658	

### Choose desired age
a = 25

### Test the function:
yll(a, B, c, K, L r)
	
# Define a function to calculate ylds.

def yld(a, B, C, D, K, Len):
	value = D*((K*C*e**(-B*a))/(B**2)*(e**(-B*Len)*(-B*(Len+a)-1) - (-B*a-1)) +((1-K)*Len))
	return value
	
######## Run through an example, using the standard values, mostly set above ##########

### Choose a disability weight for the example.
D = .5
### Choose a length of disability for the example.
len = 25
yld(a, B, C, D, K, L)
	