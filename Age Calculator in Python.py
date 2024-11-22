from datetime import date

def calculer_age():
    print("Calculatrice d'âge")
    try:
        jour = int(input("Entrez votre jour de naissance (JJ) : "))
        mois = int(input("Entrez votre mois de naissance (MM) : "))
        annee = int(input("Entrez votre année de naissance (AAAA) : "))

        naissance = date(annee, mois, jour)
        aujourd_hui = date.today()  # Assure-toi que ce nom est correct.
        
        age = aujourd_hui.year - naissance.year - ((aujourd_hui.month, aujourd_hui.day) < (naissance.month, naissance.day))

        print(f"Vous avez {age} ans.")
    except ValueError:
        print("Date invalide. Veuillez réessayer.")

calculer_age()
