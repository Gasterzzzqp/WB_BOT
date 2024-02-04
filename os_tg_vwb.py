import telebot
import time
import random
from telebot import types
bot = telebot.TeleBot('6640643329:AAFcffwzCBi2UHwq2yzgeaz5vKYpYOr66Hg')




@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Добавляем две кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Ссылка на майнинг")
        item2=types.KeyboardButton("Информация о сайте")
        item3 = types.KeyboardButton("WB скидка")
        item4 = types.KeyboardButton("Пожертвования")
        item5 = types.KeyboardButton("Связь с разработчиком")

        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)


        bot.send_message(m.chat.id, "Привет "+m.from_user.first_name ,  reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем ему случайный факт
    if message.text.strip() == 'Пожертвования' :
        bot.send_message(message.chat.id,'ljh')
    # Если юзер прислал 2, выдаем умную мысль
    elif message.text.strip() == 'Ссылка на майнинг':
            pass

bot.polling(none_stop=True, interval=0)



















































