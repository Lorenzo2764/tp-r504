def puissance(a,b):
	if not type(a) is int:
		raise TypeError("Nombre entiers seulement")
	if not type(b) is int: 
		raise TypeError("Nombre entiers seulement")
	if b < 0:
		raise Exception("Exposant negatif non supporte")
	return a**b
