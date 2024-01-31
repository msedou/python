def message():
	print("Hello World !")


message()


def afficher_nom_prenom(nom,prenom):
	print("Nom :",nom)
	print("Prenom :",prenom)

afficher_nom_prenom("Jhon","lechinoi")


def calcul_somme(a,b):
	resultat = a + b;
	return resultat


resultat = calcul_somme(12,22)
print(resultat)

def conversion_du_nombre_jour_de_travail_en_heur(nombre_de_jour_de_travail):
	#1 jour est egal a 24 H
	nombre_heur_mensuel = nombre_de_jour_de_travail * 24
	return nombre_heur_mensuel



def calcule_salaire_horaire(nombre_heur_de_travail):
	salaire_horaire = 6500
	salaire_horaire_total = nombre_heur_de_travail * salaire_horaire
	return salaire_horaire_total,salaire_horaire,nombre_heur_de_travail



def calcule_salaire_mensuel(nombre_jour_de_travaile):
	#convertir le nombre de jour de travail en heur
	resultat_nombre_heur_de_travail = conversion_du_nombre_jour_de_travail_en_heur(nombre_jour_de_travaile)
	result_salair_mensuell =calcule_salaire_horaire(resultat_nombre_heur_de_travail)
	return result_salair_mensuell ,resultat_nombre_heur_de_travail


salair_mensuel =calcule_salaire_mensuel(30)
print(salair_mensuel)

