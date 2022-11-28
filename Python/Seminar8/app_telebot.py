import telebot
from telebot import types

bot = telebot.TeleBot('секретный токен')

f = open('C:\GitHub_projects\GB\Python\Seminar8\Database.txt', 'r', encoding='UTF-8')
data = []
data = f.read().split('.')
f.close()

bot = telebot.TeleBot('Token')

@bot.message_handler(commands=['start', 'help'])
def start(m, res=False):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Сотрудники")
        markup.add(item1)
        bot.send_message(m.chat.id, 'Нажмите кнопку "Сотрудники" или отправьте слово "Команда", \
чтобы отобразить список всех сотрудников',  reply_markup=markup)

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Сотрудники' or message.text.strip() == 'Команда':
        bot.send_message(message.chat.id, data)

bot.polling(none_stop=True)


