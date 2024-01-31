numerateur = input("Entrez le numerateur :")
denominateur = input("Entrez le denominateur :")


try:

	resultat = int(numerateur) / int(denominateur)
	print(f"Le resultat est : {resultat}")
except zeroDivisionError:
	print("Erreur : Division par zero !")
except ValueError:
	print("Erreur: Conversion de type incorrecte")