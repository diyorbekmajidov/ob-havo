import telegram
import requests

TOKEN = '5740715104:AAELOe1Hag9M4VM8I5WtawEgEYfI6SBCQbw'
TOKEN1 = 'dd937da6ffbd174f0cfb2b0102bf778b'

# url = f'https://api.openweathermap.org/data/2.5/weather?lat={39.812096}&lon={66.308104}&appid={TOKEN1}'

bot = telegram.Bot(token = TOKEN)

def main():
    updates = bot.getUpdates()
    result = updates[-1]
    text = result.message.text
    update_id = result.update_id
    chat_id = result.message.chat.id
    return chat_id, update_id, text

def the_weather(text):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={text}&appid={TOKEN1}'
    data = requests.get(url).json()
    temp = data['main']['temp']
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    type_weather = data['weather'][0]['main']
    return temp, temp_max, temp_min, type_weather

# url = f'https://api.openweathermap.org/data/2.5/weather?q=London&appid={TOKEN1}'
# data = requests.get(url).json()
# print(data)

keyboard = [[telegram.KeyboardButton('Viloyatni tanlang')]]
last_update_id = -1
while True:
    chat_id, update_id, text = main()
    if last_update_id != update_id:
        if text == '/start':
            bot.sendMessage(chat_id,text, reply_markup=telegram.ReplyKeyboardMarkup(keyboard,resize_keyboard=True))
        if text == 'Viloyatni tanlang':
            keyboard=[[telegram.KeyboardButton('Samarqand'), telegram.KeyboardButton('Buxoro')],
            [telegram.KeyboardButton('Toshkent'), telegram.KeyboardButton('Andijon')]]
            bot.sendMessage(chat_id,'Shahar tanlang', reply_markup=telegram.ReplyKeyboardMarkup(keyboard,resize_keyboard=True))

        if text == "Samarqand" or text == "Toshkent" or text == "Buxoro" or text == "Andijon":
            temp, temp_max, temp_min, type_weather = the_weather(text)
            bot.sendMessage(chat_id, f'{round(temp-273)} kechasi ob-havo {round(temp_max-273)} va {type_weather } ⛈')

        last_update_id = update_id
