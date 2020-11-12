

continuer = True
while continuer:
    table = int(input("choisissez la table de Multi :"))

    for x in range(1,10):
        print(x, "x", table,"=", x*table)
    choix = input("Voulez-vous ré-essayer ?")
    if choix not in ('o', 'oui', 'ok'):
        continuer = False

# nb = int(input("saisissez la table : "))
# i = 0 

# while i < 11: # Tant que i est strictement inférieure à 11
#     print(i + 1, "*", nb, "=", (i + 1) * nb)
#     i += 1 # On incrémente i de 1 à chaque tour de boucle
