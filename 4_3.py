#Exibe de 1 ate 20
# for numero in range(1,21):
#     print(numero)

#Exibe de 1 ate 1000000
# for numero in range(1,1000000):
#     print(numero)

#Exibe primeiro e ultimo item da lista e a soma de todos os itens
# lista = range(1,1000000)
# print(min(lista))
# print(max(lista))
# print(sum(lista))

# impares = list(range(1,20,2))
# print(impares)

# numeros = []
# for numero in list(range(3,30,3)):
#     print(numero)

# cubo = []
# for numero in range(1,10):
#     cubo.append(numero**3)
# print(cubo)

cubo = [numero**3 for numero in range(1,10)]
print(cubo)
