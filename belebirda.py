import telebot
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['GitHub'])
def site(message):
    bot.send_message(message.chat.id, f'GitHub создателя бота по ссылке: https://github.com/excavator414-lgtm')

@bot.message_handler(commands=['start', 'Hello'])
def main(message):
    bot.send_message(message.chat.id, f'Привет,{message.from_user.first_name}! Я так называемый прототип будущих ботов от @Katft!')

@bot.message_handler(commands=['Help'])
def main(message):
    bot.send_message(message.chat.id, f'Созданный бот относится к @Katft')


bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.reply_to(message, "Ага фото, круто")



@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет,{message.from_user.first_name} ! Я так называемый прототип будущих ботов от @Katft!')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'Ваш ID: {message.from_user.id}')



bot.infinity_polling()