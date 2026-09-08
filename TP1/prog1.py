import fonctions as f

while True:
	a = input("nb a: ")
	b = input("nb b: ")
	try:
		a = int(a)
		b = int(b)
	except ValueError:
		pass
	res = f.puissance(a,b)
	print(res)