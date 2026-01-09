from random import randint
import requests
from datetime import datetime
from datetime import timedelta
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
        self.max_hp = randint(30,320)
        self.hp = self.max_hp
        self.power = randint(10,300)
        self.last_feed_time = datetime.now()

        Pokemon.pokemons[pokemon_trainer] = self


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
        
    def feed(self, feed_interval = 40, hp_increase = 30):
        current_time = datetime.now()  
        delta_time = timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Your Pokmeons health increased: current health{self.hp}"
        else:
            return f"Next feeding time for your pokemon: {current_time-delta_time}"
        
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['sprites']['other']['home']['front_shiny']
        else:
            return "https://wiki.pokemoncentral.it/Pikachu"


    def show_img(self):
        return self.img
    # Метод класса для получения информации
    def info(self):
        return f"The name of your Pokemon is: {self.name}, The weight of {self.name} is {self.weight}kg. {self.name}'s types are {self.type}, the hp of {self.name} are {self.hp}/{self.max_hp}, the attack of {self.name} is {self.power} "

    def attack(self, enemy):
        if isinstance(enemy, Wizard):  # Проверка на то, что enemy является Wizard
            chance = randint(1,5)
            if chance == 1:
                return "Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
    
    # Метод для восстановления здоровья
    
class Wizard(Pokemon):
    def feed (self):
        return super().feed(hp_increase=60)


class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(5,15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f"\nYour pokemon used the Super attack that deals:{super_power} "
    
    def feed (self):
        return super().feed(feed_interval=20)



