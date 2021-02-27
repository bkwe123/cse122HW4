"""Scripts used for Question #2"""

from itertools import permutations

#P0->1 = Pout=0 x Pout=1
def orGate(a, b):
	"""a and b are inputs Pa=0 and Pb=0, return Px=0"""
	return a*b

def fourOrA(a, b, c, d):
	"""returns sum of node switching factors"""
	NodeOne = orGate(a, b)
	NodeTwo = orGate(NodeOne, c)
	Final = orGate(NodeTwo, d)
	return Final * (1-Final) + NodeOne * (1-NodeOne) + NodeTwo * (1-NodeTwo)



def fourOrB(a, b, c, d):
	"""returns sum of node switching factors"""
	NodeOne = orGate(a, b)
	NodeTwo = orGate(c, d)
	Final = orGate(NodeOne, NodeTwo)
	return Final * (1-Final) + NodeOne * (1-NodeOne) + NodeTwo * (1-NodeTwo)

a0 = 0.2		#Pa=0
b0 = 0.4		#Pb=0
c0 = 0.6		#Pc=0
d0 = 0.7		#Pd=0

orders = list(permutations([a0, b0, c0, d0], 4)) #all possible input orders
orderA = []
alphaSumA = 1
orderB = []
alphaSumB = 1
for ele in orders:
	alphaSum = fourOrA(ele[0], ele[1], ele[2], ele[3])
	if alphaSum < alphaSumA:
		alphaSumA = alphaSum
		orderA = ele

	alphaSum = fourOrB(ele[0], ele[1], ele[2], ele[3])
	if alphaSum < alphaSumB:
		alphaSumB = alphaSum
		orderB = ele

print("Gate A:", orderA)
print("Gate A:", orderB)