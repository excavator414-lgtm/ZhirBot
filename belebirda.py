import telebot
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['GitHub'])
def site(message):
    bot.send_message(message.chat.id, 'GitHub создателя бота по ссылке: \n https://github.com/excavator414-lgtm')

@bot.message_handler(commands=['start', 'Hello'])
def main(message):
    bot.send_message(message.chat.id, f'Привет,{message.from_user.first_name}! Я так называемый прототип будущих ботов от @Katft!')

@bot.message_handler(commands=['Help'])
def help(message):
    bot.send_message(message.chat.id, f'Весь этот бот, это так называемый прототип работающий на серверах Render \n<b>Созданный бот относится к</b> <u>@Katft</u>', parse_mode="html")



@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет,{message.from_user.first_name}! Я так называемый прототип будущих ботов от @Katft!')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'Ваш ID: {message.from_user.id}')



bot.infinity_polling()