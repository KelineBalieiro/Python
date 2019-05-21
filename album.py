# def make_album(cant, mus, num_fai):
#     album = {'cantor': cant, 'musica': mus, 'numero_faixas': num_fai}
#     return album
# retorno = make_album('jorge', 'flor', '1')
# retorno1 = make_album('y', 'x', '1')
# retorno2 = make_album('w', 'z', '1')
# print(retorno)
# print(retorno1)
# print(retorno2)


def make_album(cant, mus):
    album = {'cantor': cant, 'musica': mus}
    return album
while True:
    cantor = input("Cantor: ")
    musica = input("Musica: ")
    album = make_album(cantor, musica)
    print(album)
