import telebot
from telebot import types

bot = telebot.TeleBot('Token')

print("Bot is start")

f = open('C:\GitHub_projects\GB\Python\Seminar8\Database.txt', 'r', encoding='UTF-8')
data = []
data = f.read().split('.')
f.close()

@bot.message_handler(commands=['start', 'help'])
def start(m, res=False):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Записная книжка")
        markup.add(item1)
        bot.send_message(m.chat.id, 'Сохраните данные о контакте или нажмите кнопку "Записная книжка", \
чтобы отобразить список всех ваших записей',  reply_markup=markup)

# Сохраняет сообщения в файл
@bot.message_handler(func=lambda message: True, content_types=['text'])
def msg(message):
    f = open("C:\GitHub_projects\GB\Python\Seminar9\Phone_book.txt", 'a',  encoding='UTF-8')
    f.write(message.text + '\n')
    f.close()
    f = open("C:\GitHub_projects\GB\Python\Seminar9\Phone_book.csv", 'a',  encoding='UTF-8')
    f.write(message.text + '\n')
    f.close()

# Демонстрирует данные из файла
@bot.message_handler(content_types=["text"])
def handle_text(message):
    global data
    if message.text.strip() == 'Записная книжка':
        bot.send_message(message.chat.id, data)


bot.polling(none_stop=True)

