# def get_formatted_name(first_name, last_name):
#     full_name = first_name + " " + last_name
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)


def get_formatted_name(first_name, last_name, midle_name=''):
    if midle_name:
        full_name = first_name + ' ' + midle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
