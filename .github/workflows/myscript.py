import os
# Exécuter la commande git bisect start
goodhash = "84cae48c4a7a261844abf94cc9925b90605fda00"
badhash = "1fc3fc00082f68ec53605acc9b3e37841dd04c48"
os.system(f"git bisect start {badhash} {goodhash}")

# Exécuter les tests pour chaque commit dans la plage spécifiée
command = "python manage.py test"
os.system(f"git bisect run {command}")
#Si jamais on veut revenir à l'état initial de notre repo
#(avant l'utilisation du git bisect on peut ajouter la ligne suivante )
#on ajoute la ligne suivante
os.system(f"git bisect reset")
