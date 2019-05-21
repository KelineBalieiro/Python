# alien = {'color': 'green', 'points': '5'}
# print(alien)

# alien['x_position'] = 0
# alien['y_position'] = 25
# print(alien)

# alien = {}
# alien['color'] = 'green'
# alien['y_position'] = 5
# print(alien)


# alien = {'color': 'green'}
# print("The alien is " + alien['color'] + ".")
# alien['color'] = 'yellow'
# print("The alien is now " + alien['color'] + ".")

# alien = {'xposition': 0, 'yposition': 25, 'speed': 'medium'}
# print("Original x-position: " + str(alien['xposition']))
# if alien['speed'] == 'slow':
#     xincrement = 1
# elif alien['speed'] == 'medium':
#     xincrement = 2
# else:
#     xincrement = 3
# alien['xposition'] = alien['xposition'] + xincrement
# print("New x-position: " + str(alien['xposition']))

alien = {'color': 'green', 'points': '5'}
print(alien)

del alien['points']
print(alien)
