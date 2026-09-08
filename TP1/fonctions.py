def puissance(a,b):
	if not type(a) is int or not type(b) is int:
		raise TypeError("Nombres entiers seulement")

	if a == 0 and b < 0:
		return ("0^"+str(b)+" est indéfini.")

	res = a

	for i in range(1,abs(b)):
		res *= a

	if b < 0:
		return 1/res
	return res
