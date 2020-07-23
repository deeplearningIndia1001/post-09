#I.G : @deeplearningindia
""" program to find find given no. is even or odd using def()"""

def seperator(num):
	if num%2 == 0:
		return "Even"
	else:
		return "Odd"

x = 10
y = 7

print(seperator(x))
print(seperator(y))