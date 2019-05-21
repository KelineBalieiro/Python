#def greet_user(username):
#    print("Hello," + username.title() + "!")
#greet_user('jesse')

#def favorite_book(title):
#    print("Um dos meus livros favoritos é " + title.title() + ".")
#favorite_book('Alice no país das maravilhas')

#def describe_pet(animal_type, pet_name):
 #   print("\nI have a " + animal_type + ". " "My " + animal_type +"'s name is " + pet_name.title() + ".")
#describe_pet('hamster', 'harry')
#describe_pet('dog', 'willie')

#def describe_pet(animal_type, pet_name):
 #   print("\nI have a " + animal_type + ".")
  #  print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#describe_pet(animal_type='hamster', pet_name='harry')


#def build_person(first_name, last_name):
#    person = {'first': first_name, 'last': last_name}
#    return person
#musician = build_person('jimi', 'hendrix')
#print(musician)


#def build_person(first_name, last_name, age=''):
#    person = {'first': first_name, 'last': last_name}
#    if age: person['age'] = age
#    return person
#musician = build_person('jimi', 'hendrix', age=27)
#print(musician)

users = [
  {
    "id": 1,
    "name": "Allan",
    "age": 27,
    "profile_picture": "http://…",
    "city": "São Paulo"
  },
  {
    "id": 2,
    "name": "Julie",
    "age": 29,
    "profile_picture": "http://…",
    "city": "Curitiba"
  },
  {
    "id": 3,
    "name": "Pedro",
    "age": 31,
    "profile_picture": "http://…",
    "city": "Rio de Janeiro"
  }
]

# Crie a função que irá filtrar a lista
def users_over_27(user):
  return user["age"] > 27

# Filtramos os usuários utilizando o método filter
filtered_users = filter(users_over_27, users)

list(filtered_users)
