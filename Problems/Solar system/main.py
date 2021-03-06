# create the planets.txt
with open('planets.txt', mode='w', encoding='utf-8') as file:
    for planet in ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']:
        file.write(planet + '\n')