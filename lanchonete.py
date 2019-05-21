sandwich_orders = ['bacon', 'salada', 'duplo', 'vegetariano']
finished_sandwiches = []


while sandwich_orders:
    pedido = sandwich_orders.pop()
    print("Preparei seu sanduiche de " + pedido.title())
    finished_sandwiches.append(pedido)
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche.title())
