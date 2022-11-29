import telebot
import math

bot = telebot.TeleBot('Token')
print("Bot is start")
value = ''
old_value = ''
keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(   telebot.types.InlineKeyboardButton('π', callback_data='π'),
                telebot.types.InlineKeyboardButton('sin', callback_data='sin'),
                telebot.types.InlineKeyboardButton('cos', callback_data='cos'),
                telebot.types.InlineKeyboardButton('n!', callback_data='n!'))

keyboard.row(   telebot.types.InlineKeyboardButton('√', callback_data='√'),
                telebot.types.InlineKeyboardButton('C', callback_data='C'),
                telebot.types.InlineKeyboardButton('<=', callback_data='<='),
                telebot.types.InlineKeyboardButton('/', callback_data='/'))

keyboard.row(   telebot.types.InlineKeyboardButton('7', callback_data='7'),
                telebot.types.InlineKeyboardButton('8', callback_data='8'),
                telebot.types.InlineKeyboardButton('9', callback_data='9'),
                telebot.types.InlineKeyboardButton('*', callback_data='*'))

keyboard.row(   telebot.types.InlineKeyboardButton('4', callback_data='4'),
                telebot.types.InlineKeyboardButton('5', callback_data='5'),
                telebot.types.InlineKeyboardButton('6', callback_data='6'),
                telebot.types.InlineKeyboardButton('-', callback_data='-'))

keyboard.row(   telebot.types.InlineKeyboardButton('1', callback_data='1'),
                telebot.types.InlineKeyboardButton('2', callback_data='2'),
                telebot.types.InlineKeyboardButton('3', callback_data='3'),
                telebot.types.InlineKeyboardButton('+', callback_data='+'))

keyboard.row(   telebot.types.InlineKeyboardButton('-/+', callback_data='-/+'),
                telebot.types.InlineKeyboardButton('0', callback_data='0'),
                telebot.types.InlineKeyboardButton(',', callback_data='.'),
                telebot.types.InlineKeyboardButton('=', callback_data='='))



@bot.message_handler(commands=["start", "calculator"])
def getMessege(messege):
    global value
    if value == '':
        bot.send_message(messege.from_user.id, "0", reply_markup=keyboard)
    else:
        bot.send_message(messege.from_user.id, value, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global value, old_value
    data = query.data
    if data == 'π':
        value = str(math.pi)
    elif data == 'sin':
        value = str(math.sin(int(value)))
    elif data == 'cos':
        value = str(math.cos(int(value)))
    elif data == 'n!':
        value = str(math.factorial(int(value)))
    elif data == '-/+':
        value = str(float(value) * (-1))           
    elif data == 'C':
        value = ''
    elif data == '√':
        if value != '':
            value = str(float(value) ** 0.5)            
    elif data == '<=':
        if value != '':
            value = value[:len(value)-1] 
    elif data == '=':
        try:
            value = str(eval(value))
        except:
            value = 'Ошибка!'

    else:
        value += data

    if (value != old_value and value != '') or ('0' != old_value and value == ''):
        if value == '':
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='0', reply_markup=keyboard)
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=value, reply_markup=keyboard)
    old_value = value
    if value == 'Ошибка!': value = ''

    
bot.polling(none_stop=False, interval=0)
