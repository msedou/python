#Vous allez créer une calculatrice qui permettra d'effectuer une opération simple entre deux nombres.
#créer deux variables pour stocker les deux nombres
number1 = 12
number2 = 7

#stocker le symbole qui représentera l'opération à effectuer
symbole = "-"

if(number1 !=0 and number2 !=0):
	if(symbole =="+"):
		print(f"la somme de {number1} + {number2} est egale a ",number1 + number2)
	elif(symbole =="*"):
		print(f"le produit des nombres {number1} * {number2} est egal a : ",number1 * number2)
	elif(symbole == "-"):
		if(number1 > number2):
			print(f"la difference de {number1} et de  {number2} est de :",number1 - number2)
	else:
		print("cette operateur n'existe pas")