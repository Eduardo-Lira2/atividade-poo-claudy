#exercicio 1:
numeros = [ 10 , 20 , 30, 40, 50]
print (numeros)

#exercicio 2:
frutas = [' banana ',' maca ',' abacaxi ',' melao ',' uva ','melancia ']

print (frutas[0])
print (frutas[5])
print (frutas[2])
#exercico 3:

frutas[1] = "palmeira"

print (frutas)

# exercicio 4:

novo_numero = int(input('digite um numero'))

numeros.append (novo_numero)
print (numeros)

#exercicio 5:

frutas.pop ()
print (frutas)

# exercicio 6:

print("Comprimento da lista numeros:", len(numeros))

# exercicio 7:

soma_numeros = sum(numeros)
print("Soma dos elementos da lista numeros:", soma_numeros)

# exercicio 8:

numeros.sort()
print("Lista numeros ordenada:", numeros)

# exercicio 9:

frutas.reverse()
print("Lista frutas invertida:", frutas)

# exercicio 10:

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_mesclada = lista1 + lista2
print("Lista mesclada:", lista_mesclada)

# exercicio 11:

numero_usuario = int(input("Digite um número para verificar se está na lista: "))
if numero_usuario in numeros:
    print("O número", numero_usuario, "está na lista.")
else:
    print("O número", numero_usuario, "não está na lista.")
