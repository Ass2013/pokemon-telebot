from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.weight = self.get_weight()
        self.type = self.get_type()

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
        
    def get_weight(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['weight'])
        else:
            return "6 kilograms"
        
    def get_type(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            types = [t['type']['name'] for t in data['types']]
            return ", ".join(types)
        else:
            return "electric"
        
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['sprites']['other']['home']['front_shiny']
        else:
            return "https://wiki.pokemoncentral.it/Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"The name of your Pokemon is: {self.name}, The weight of {self.name} is {self.weight}kg. {self.name}'s types are {self.type}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img



