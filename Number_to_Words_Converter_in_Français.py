def nombre_en_lettres(nombre):
    """Convertit un nombre entier en lettres en français."""
    if not nombre.isdigit() or int(nombre) < 0:
        return "Entrée invalide. Entrez un nombre entier positif."

    if nombre == "0":
        return "zéro"

    unités = ["", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf"]
    dizaines = ["", "", "vingt", "trente", "quarante", "cinquante", "soixante", "soixante", "quatre-vingt", "quatre-vingt"]
    exceptions = ["dix", "onze", "douze", "treize", "quatorze", "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf"]

    def convertir_trois_chiffres(n):
        """Convertit un nombre de trois chiffres maximum."""
        n = int(n)
        result = ""

        if n >= 100:
            centaine = n // 100
            if centaine > 1:
                result += unités[centaine] + " "
            result += "cent"
            if n % 100 != 0:
                result += " "

        reste = n % 100
        if reste < 20 and reste >= 10:
            result += exceptions[reste - 10]
        else:
            dizaine = reste // 10
            unité = reste % 10
            result += dizaines[dizaine]
            if dizaine in [7, 9]:
                result += "-" + exceptions[unité] if unité > 0 else ""
            elif unité == 1 and dizaine not in [8]:
                result += "-et-un"
            elif unité > 0:
                result += "-" + unités[unité]

        return result.strip()

    # Découpage du nombre en tranches de trois chiffres
    parties = []
    while nombre:
        parties.append(nombre[-3:])
        nombre = nombre[:-3]

    parties.reverse()
    échelles = ["", "mille", "million", "milliard", "billion", "billiard", "trillion"]
    résultat = ""

    for i, partie in enumerate(parties):
        if partie != "000":
            if i == len(parties) - 2 and int(partie) == 1:  # Gérer "mille" sans "un"
                résultat += "mille "
            else:
                résultat += convertir_trois_chiffres(partie) + " " + échelles[len(parties) - 1 - i] + " "

    return résultat.strip()

# Exemple d'utilisation
nombre = input("Entrez un nombre : ")
print(nombre_en_lettres(nombre))
