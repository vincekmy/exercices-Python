
continuer = True
while continuer:
    age = int(input("Quel äge avez-vous ?"))
    if age > 18:
        print("vous êtes majeur")
    elif age < 18:
            print("vous êtes mineur")  
            choix = input("Voulez-vous continuer ?")
            if choix not in ('o', 'oui', 'ok'):
                continuer = False



    