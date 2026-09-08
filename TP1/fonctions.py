def puissance(a,b):
	if not type(a) is int:
		raise TypeError("Nombre entiers seulement")
	if not type(b) is int: 
		raise TypeError("Nombre entiers seulement")
	return a**b