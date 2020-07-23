#I.G : @deeplearningindia
""" Using the power of lambda with def() """

def bahar(num):
	return lambda hp : num*hp

x = 10
y = 7

result = bahar(x)
print(result(5))

result = bahar(y)
print(result(5))