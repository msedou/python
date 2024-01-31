print("Hello World !");
nom = "Dupont";
prenom = "Jean";
age = 30;
print(f"Bonjour , je m'appelle {prenom} {nom} et j'ai {age} ans.");

#les listes 
plateformes_sociales = ["facebook","Instagram","Snapchat","Twitter"];
plateformes_sociales[2] = "Linkedin";
plateformes_sociales.append("TikTok");
#plateformes_sociales.remove("Snapchat");
len(plateformes_sociales);
plateformes_sociales.sort();

#extend(): Ajoute plusieurs éléments à la fin de la liste.
#insert() : Insère un élément à une position donnée dans la liste.
#pop(): Supprime et renvoie l'élément à une position donnée de la liste, ou le dernier élément si aucun indice n'est spécifié.
#index(): Renvoie la première occurrence de l'élément spécifié dans la liste.
#count(): Renvoie le nombre d'occurrences de l'élément spécifié dans la liste.
#reverse() : Inverse l'ordre des éléments de la liste.

#---------------------------------------------------------
ensoleille = False;
neig = True;

if ensoleille:
	print("On va a la plage");
elif neig:
	print("On fait un bonhome de neig");
else :
	print("On reste a la maison")



#-----------------------------------------
avec_soleil = True
en_semaine = False


if avec_soleil and not en_semaine:
	print("On va a la plage")
elif avec_soleil and en_semaine:
	print("On va au travail ")
else:
	print("On reste a la maison")
#-------------------------------------
fruit = "pome"
match fruit:
	case "pome":
		print("super On a une pome du jamais vue")
	case "banane":
		print("ok une banane")
	case "orang":
		print("du vitame c")
	case _:
		print("Je ne connais pas ce fruit")