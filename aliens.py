# alien0 = {'color': 'green', 'point':5}
# alien1 = {'color': 'yellow', 'point':10}
# alien2 = {'color': 'red', 'point':15}

# aliens = [alien0, alien1, alien2]

# for alien in aliens:
#     print(alien)

# aliens = []
# for alien in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)

# for alien in aliens[:5]:
#     print(alien)
# print("...")

# print("Total number of aliens: " + str(len(aliens)))

aliens = []
for alien in range(0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)
print("...")

print("Total number of aliens: " + str(len(aliens)))
