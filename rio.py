rio = {
    'amazonas': 'brasil',
    'nilo': 'egito',
    'mississipi': 'estados unidos',
}

for nome, pais in rio.items():
    print("O " + nome.title() + " corre pelo " + pais.title() + ".")

for pais in rio.values():
    print(pais.title())
