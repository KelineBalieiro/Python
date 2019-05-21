# usuarios = ['admin', 'maria', 'julia', 'clara', 'amanda', 'kaka']
# for usuario in usuarios:
#     if usuario == 'admin':
#         print("Olá admin, gostaria de ver um relatório de status?")
#     else:
#         print("Olá " + usuario.title() + ", obrigado por fazer login novamente!")

usuarios = []
if usuarios:
    for usuario in usuarios:
        if usuario == 'admin':
            print("Olá admin, gostaria de ver um relatório de status?")
        else:
            print("Olá " + usuario.title() + ", obrigado por fazer login novamente!")
else:
    print("Precisamos encontrar alguns clientes!")
