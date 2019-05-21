def car(fabricante, modelo, **info):
    carro = {}
    carro['fabricante'] = fabricante
    carro['modelo'] = modelo
    for key, value in info.items():
        carro[key] = value
    return carro
car = car('Toyota', 'Corola',
           cor = 'Azul')
print(car)
