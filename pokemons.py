class Pokemons():
    def __init__(self, name, type, description, ndex, region, is_caught):
        self.name = name
        self.type = type
        self.description = description
        self.ndex = ndex
        self.region = region
        self.is_caught = is_caught
    
    def speak(self):
        print('My name is', self.name)

    def details(self):
        print('Name:', self.name)

        if len(self.type) == 1:
            print('Type:', self.type[0])
        else:
            print('Type:', self.type[0],'/', self.type[1])
        print('Description:', self.description)
        print('Region:', self.region)

    def status(self):
        if self.is_caught == True:
            print('Pokemon', self.name, 'is caught.')
        else:
            print('Pokemon', self.name, 'is not caught yet')

chikorita = Pokemons('Chikorita', ['Grass'], 
                     'A small quadrupedal green Pokémon with a large lime green leaf on its head. It waves its leaf around to scare off foes but it also has a sweet smell to it. It loves to sunbathe.',
                     152, 'Johto', True)

crobat = Pokemons('Crobat', ['Posion', 'Flying'],
                  'It is the final evolution of Zubat and Golbat. Crobat can fly long distances. It usually flies with all four wingsbut, it can alternate what pairs of wings it flies with. Golbat evolves into Crobat when it has high-enough friendship levels. Brock\'s Zubat evolved into a Crobat in the anime.',
                  169, 'Johto', True)

pichu = Pokemons('Pichu', ['Electric'], 
                 'It is a playable character in Super Smash Bros. Melee and Super Smash Bros. Ultimate. Junichi Masuda noted that Pichu was intended to become the "next" Pikachu.',
                 172, 'Johto', False)

pichu.speak()
crobat.status()
chikorita.details()
crobat.details()
