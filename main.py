import requests
import random
import telebot
from bs4 import BeautifulSoup as bs

URL = "https://www.anekdot.ru"
BOT_TOKEN = '5593276803:AAEmjdBhg5u5cLddYWMNx-yMsFQ3TD0D7_M'
PAGE = requests.get(URL)

def parsing(page):
    soup = bs(page.text, 'html.parser')
    jokes = soup.find_all('div', class_ = 'text')
    return [j.text for j in jokes]

list_of_jokes = parsing(PAGE)

random.shuffle(list_of_jokes)

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def greet(message):
    bot.send_message(message.chat.id, 'Привет, чтобы посмеяться отправь слово: «шутка»')

@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.lower() == 'шутка':
        bot.send_message(message.chat.id, list_of_jokes[0])
        del list_of_jokes[0]
    else:
        bot.send_message(message.chat.id, 'Чтобы посмеяться отправь слово «шутка»')
bot.polling()


