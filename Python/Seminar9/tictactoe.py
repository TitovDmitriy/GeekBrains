import telebot
import random
from telebot import types

bot = telebot.TeleBot("токен")
item = {}
board = [' ' for c in range(9)]
              
playerSymbol = "X"
botSymbol = "0"

print("Bot is start")

winbool = False
losebool = False

def clear():
    global board
    board = [' ' for c in range(9)]
    
def win(cell_1, cell_2, cell_3):
    if cell_1 == playerSymbol and cell_2 == playerSymbol and cell_3 == playerSymbol:
        print("win")
        global winbool
        winbool = True

def lose(cell_1, cell_2, cell_3):
    if cell_1 == botSymbol and cell_2 == botSymbol and cell_3 == botSymbol:
        print("lose")
        global losebool
        losebool = True

def defend(cell_1, cell_2, posDef):
    if cell_1 == playerSymbol and cell_2 == playerSymbol:
        posDef = botSymbol

@bot.message_handler(commands=["start"])
def welcome(message):
    if message.text == "/start":
        global gameIsStart
        gameIsStart = True

    if gameIsStart == True:
        item = {}
        bot.send_message(message.chat.id, "Игра началась")
        global markup
        markup = types.InlineKeyboardMarkup(row_width=3)
        i = 0
        for i in range(9):
            item[i] = types.InlineKeyboardButton(board[i], callback_data=str(i))        
        markup.row(item[0], item[1], item[2])
        markup.row(item[3], item[4], item[5])
        markup.row(item[6], item[7], item[8])
        bot.send_message(message.chat.id, "Выбери клетку", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callbackInline(call):
    if call.message:

        # установки бота
        randomCell = random.randint(0, 8)
        if board[randomCell] == playerSymbol:
            randomCell = random.randint(0, 8)
        if board[randomCell] == botSymbol:
            randomCell = random.randint(0, 8)
        if board[randomCell] == " ":
            board[randomCell] = botSymbol
        # установки игрока
        for i in range(9):
            if call.data == str(i):
                if board[i] == " ":
                    board[i] = playerSymbol

            # условия победы
            win(board[0], board[1], board[2])
            win(board[0], board[4], board[8])
            win(board[6], board[4], board[2])
            win(board[6], board[7], board[8])
            win(board[0], board[3], board[6])
            item[i] = types.InlineKeyboardButton(board[i], callback_data=str(i))

        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Крестики нолики",
            reply_markup=None,
        )
        # обновление игрового поля
        global markup
        markup.row(item[0], item[1], item[2])
        markup.row(item[3], item[4], item[5])
        markup.row(item[6], item[7], item[8])
        bot.send_message(call.message.chat.id, "Выбери клетку", reply_markup=markup)

        global winbool
        if winbool:
            clear()
            bot.send_message(call.message.chat.id, "Бот проиграл")
            winbool = False
            
        global losebool
        if losebool:
            clear()
            bot.send_message(call.message.chat.id, "Бот выиграл")
            losebool = False
            
bot.polling(none_stop=True)
