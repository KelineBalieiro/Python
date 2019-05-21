# favorite_languages ={
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }

# print ("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

# favorite_languages ={
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " + language.title() + ".")

# favorite_languages ={
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# for name in favorite_languages.keys():
#     print(name.title())

# favorite_languages ={
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())
#     if name in friends:
#         print(" Hi " + name.title() + ", I see your favorite language is " +
#             favorite_languages[name].title() + "!")



# favorite_languages ={
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# for name in sorted(favorite_languages.keys()):
#     print(name.title() + ", thank you for taking the poll.")


# favorite_languages ={
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# print("The fallowing lanuages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())


# favorite_languages ={
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# print("The fallowing lanuages have been mentioned:")
# for language in set(favorite_languages.values()):
#     print(language.title())


favorite_languages ={
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

