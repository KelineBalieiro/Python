class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.num_cpf = '111.111.111-11'p

    def cpf(self):
        print("O cpf é: " + self.num_cpf)

    def email(self):
        print("O email é: ")
#inform = User('111.111.111-85', 'usuario@usuario.com')
usuario = User('keline', 'balieiro')
print(usuario.first_name.title() + ' ' + usuario.last_name.title())
#print(inform.cpf + ' ' + inform.email)
usuario.cpf()
