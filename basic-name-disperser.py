import random
while True:
	inpu = input("Name :")
	def dis(name):
		lst = list(name)
		random.shuffle(lst)
		nmed = "".join(lst)
		return nmed
	print(dis(inpu))
	
