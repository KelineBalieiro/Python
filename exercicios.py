import random
NOMES = ['Pedro', 'Carla', 'Bernardo', 'Carlos', 'Lúcio', 'Luis', 'Paulo', 'Maria', 'Márcia', 'Beatriz', 'Viviane', 'Juliana']
SOBRENOMES = ['Silva', 'Pereira', 'Ferreira', 'Santos']
CIDADES = [('Montes Claros', 'MG'), ('Belo Horizonte', 'MG'), ('Goiânia', 'GO'), ('Anápolis', 'GO'), ('Cabo Frio', 'RJ'), ('Niterói', 'RJ')]

pessoas = [
   {'id': num, 'nome': random.choice(NOMES)+' '+random.choice(SOBRENOMES), 'cep': random.choice(CIDADES), 'idade': random.randint(18, 60)}
   for num in range(1, 101)
]
print(pessoas)

# pessoas_mg = [p for p in pessoas if p['cep'][1] == 'MG']

# 2 - Filtre todas as pessoas de MG com 'Maria' no nome
[p['nome'] for p in pessoas if p['nome'].split()[0] == 'Maria']
for p in pessoas:
    nome = p['nome']
    if nome.split()[0] == 'Maria':
        print(nome)

# 3 - Conte quantas pessoas tem 'Pedro' no nome

len([p['nome'] for p in pessoas if p['nome'].split()[0] == 'Pedro'])
contador = 0
for p in pessoas:
    nome = p['nome']
    if nome.split()[0] == 'Pedro':
        contador = contador + 1
        print(nome.split()[0], ": ",  contador)


# # 4 - Calcule a média de idade das pessoas (dica: use a função sum())
sum([p['idade'] for p in pessoas ]) / len([p['idade'] for p in pessoas ])

lista = []
for p in pessoas:
    idade = p['idade']
    lista.append(idade)
soma = sum(lista)
media = soma/len(lista)
print(media)


# 5 - Calcule a média de idade das pessoas de cada estado

sum([p['idade'] for p in pessoas if p['cep'][1] == 'MG']) / len([p['idade'] for p in pessoas if p['cep'][1] == 'MG'])
print("MG")
lista = []
for p in pessoas:
    if p['cep'][1] == 'MG':
        idade = p['idade']
        lista.append(idade)
soma = sum(lista)
media = soma/len(lista)
print(media)

sum([p['idade'] for p in pessoas if p['cep'][1] == 'GO']) / len([p['idade'] for p in pessoas if p['cep'][1] == 'GO'])
[p for p in pessoas if p['cep'][1] == 'GO' ]
print("GO")
lista = []
for p in pessoas:
    if p['cep'][1] == 'GO':
        idade = p['idade']
        lista.append(idade)
soma = sum(lista)
media = soma/len(lista)
print(media)

sum([p['idade'] for p in pessoas if p['cep'][1] == 'RJ']) / len([p['idade'] for p in pessoas if p['cep'][1] == 'RJ'])
[p for p in pessoas if p['cep'][1] == 'RJ' ]
print("RJ")
lista = []
for p in pessoas:
    if p['cep'][1] == 'RJ':
        idade = p['idade']
        lista.append(idade)
soma = sum(lista)
media = soma/len(lista)
print(media)

# 6 - Calcule a mediana da idade de cada pessoa

[sorted(p['idade'] for p in pessoas)[len(pessoas)//2]]

lista = []
mediana = 0
centro = 0
for p in pessoas:
    idade = p['idade']
    contador = contador + idade
    soma = contador
    lista.append(idade)
idade_ordenada = sorted(lista)
meio = (len(idade_ordenada))/2
if(meio % 2 == 1):
    mediana=idade_ordenada[meio]
else:
    mediana=(idade_ordenada[centro-1]+idade_ordenada[centro])/2
print(mediana)

#idade = [p for p in pessoas if p['idade'] == 54]
