# Demander à l'utilisateur d'entrer un nombre
n = int(input("Enter number: "))

# Initialiser la variable qui contiendra le nombre inversé
rev = 0

# Tant que le nombre est supérieur à 0
while n > 0:
    # Extraire le dernier chiffre du nombre
    dig = n % 10
    # Ajouter ce chiffre à la nouvelle valeur inversée
    rev = rev * 10 + dig
    # Supprimer le dernier chiffre du nombre (division entière par 10)
    n = n // 10
# Afficher le résultat : le nombre inversé
print("Reverse of the number:", rev)
