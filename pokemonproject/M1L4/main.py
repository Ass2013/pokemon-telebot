import telebot 
from config import token
from random import randint
from logic import Pokemon, Wizard, Fighter

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! I'm a pokemon game bot, press /go and I'll give you your Pokemon")

#@bot.message_handler(commands=['go'])
#def go(message):
#    if message.from_user.username not in Pokemon.pokemons.keys():
#        pokemon = Pokemon(message.from_user.username)
#        bot.send_message(message.chat.id, pokemon.info())
#        bot.send_photo(message.chat.id, pokemon.show_img())
#    else:
#        bot.reply_to(message, "You already have a Pokemon")

@bot.message_handler(commands=['go'])
def start(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        chance = randint(1,3)
        if chance == 1:
            pokemon = Pokemon(message.from_user.username)
        elif chance == 2:
            pokemon = Wizard(message.from_user.username)
        elif chance == 3:
            pokemon = Fighter(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "You already have a Pokemon")


@bot.message_handler(commands=['attack'])
def attack_pok(message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.username in Pokemon.pokemons.keys() and message.from_user.username in Pokemon.pokemons.keys():
            enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
            pok = Pokemon.pokemons[message.from_user.username]
            res = pok.attack(enemy)
            bot.send_message(message.chat.id, res)
        else:
            bot.send_message(message.chat.id, "You can fight only with Pokemons")
    else:
            bot.send_message(message.chat.id, "To attack, you have to answer the message of the person you want to fight")


bot.infinity_polling(none_stop=True)


