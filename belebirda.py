import telebot
from telebot import types
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)




@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Съесть фото', callback_data='delete')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')

    markup.row(btn2)
    bot.send_message(message, 'Ага фото, круто', reply_markup=markup)



@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Текст изменён вроде', callback.message.chat.id, callback.message.message_id)
        


@bot.message_handler(commands=['github'])
def site(message):
    bot.send_message(message.chat.id, f'GitHub создателя бота по ссылке: https://github.com/excavator414-lgtm')

@bot.message_handler(commands=['start', 'Hello'])
def main(message):
    bot.send_message(message.chat.id, f'Привет,{message.from_user.first_name}! Я так называемый прототип будущих ботов от @Katft!')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, f'Созданный бот относится к @Katft')



@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет,{message.from_user.first_name} ! Я так называемый прототип будущих ботов от @Katft!')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'Ваш ID: {message.from_user.id}')





bot.infinity_polling()