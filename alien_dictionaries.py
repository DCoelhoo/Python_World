alien_0 = {
    'color' : 'green', 
    'points' : 5,
}

print(alien_0)

#Add content to Dictionaries
alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['z_position'] = -1

print(alien_0)

print(f'\n The alien color is: {alien_0["color"]}')
#Edit content in Dictionaries
alien_0['color'] = 'yellow'

print(f'\n The alien color has changed to: {alien_0["color"]}')

del alien_0['z_position']

print(alien_0)

print("\n----------------\n")

#Nesting 
alien_1 = {
    'color' : 'green', 
    'points' : 10,
}

alien_2 = {
    'color' : 'red', 
    'points' : 15,
}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)