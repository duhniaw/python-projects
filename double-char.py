def double_char(char):
	doubled_char = ""
	for i in range(len(char)):
		doubled_char += char[i]*2
	return doubled_char
	
print(double_char("201o"))