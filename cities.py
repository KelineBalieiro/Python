cidades = {
    'montes claros':{
        'pais' : 'Brasil',
        'populacao' : '400 mil',
        'fato' : 'pequi',
    },
    'montezuma':{
        'pais' : 'Brasil',
        'populacao' : '10 mil',
        'fato' : 'agua quente',
    },
    'bh' : {
        'pais' : 'Brasil',
        'populacao' : '1,4 milhão',
        'fato' : 'mineirao',
    }
}

for cidade, info in cidades.items():
    print("\nCidade:", cidade.title())
    pais = info['pais']
    pop = info['populacao']
    fato = info['fato']
    print("\tPaís: " + pais.title())
    print("\tPopulação: " + pop.title())
    print("\tFato: " + fato.title())
