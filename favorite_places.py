favorite_places = {
    'keline' : {
        'cidade' : 'bh',
    },
    'luiz' : {
        'cidade' : 'montezuma',
    },
    'cassia' : {
        'cidade' : 'moc'
    },
}

for username, user_info in favorite_places.items():
    print("\nUsername: " + username.title())
    location = user_info['cidade']
    print("\nCidade: " + location.title())
