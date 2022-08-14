# Programme affichant les n premiers nombres de la suite de Fibonacci

print("Bienvenue dans ce générateur de nombres de la suite de Fibonacci :")

user_request = int(input("Entrez le nombre de nombres à afficher :"))

a = 0
b = 1
somme = 0

print("Les {0} premiers nombres de la suite de Fibonacci sont :".format(
    user_request))

for _ in range(user_request):
    print(somme, end=' ')
    a = b
    b = somme
    somme = a + b
