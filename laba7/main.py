import telebot
import datetime
from telebot import types
import psycopg2

conn = psycopg2.connect(database="Laba7",
                        user="postgres",
                        password="1111",
                        host="localhost",
                        port="5432") #подключение к базе данных
cursor = conn.cursor()

token = "6962296210:AAFgO0nzrPpmrakaCkbCNtt2wqye_cmYAxo"
bot = telebot.TeleBot(token)
date = datetime.date.today()

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(True, True)
    keyboard.row('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Расписание на текущую неделю',
                 'Расписание на следующую неделю')
    bot.send_message(message.chat.id, "Здравствуйте! Хотите узнать расписание группы БИН2306?\nВыберите что Вас интерисует.", reply_markup=keyboard)

@bot.message_handler(commands=['mtuci'])
def start_message(message):
    bot.send_message(message.chat.id, 'Более подробно можите изучить тут: https://mtuci.ru/')

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, ' Здравствуйте! Я бот расписания и готов помочь Вам узнать расписание группы БИН2306.\nВот что я умею:\n/start - начало работы бота\n/mtci - официальный сайт\n/week - чет/нечет неделя')

@bot.message_handler(commands=['week'])
def week_message(message):
    bot.send_message(message.chat.id, 'Сейчас чётная неделя')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "понедельник":
        cursor.execute("SELECT * FROM public.pn")
        dates = cursor.fetchall()
        info = 'Понедельник\n'
        for e in dates:
            if e[2] =="":
                info += f'№{e[0]}. {e[3]} Нет пары\n'
            else:
                info += f'№{e[0]}. {e[3]}, {e[1]} ,  Кабинет:{e[2]},  Преподаватель: {e[4]}  \n'
        bot.send_message(message.chat.id, info)
    elif message.text.lower() == "вторник":
        cursor.execute("SELECT * FROM public.vt")
        dates = cursor.fetchall()
        info = 'Вторник\n'
        for e in dates:
            if e[2] =="":
                info += f'№{e[0]}. {e[3]} Нет пары\n'
            else:
                info += f'№{e[0]}. {e[3]}, {e[1]} ,  Кабинет:{e[2]},  Преподаватель: {e[4]}  \n'
        bot.send_message(message.chat.id, info)
    elif message.text.lower() == "среда":
        cursor.execute("SELECT * FROM public.cp")
        dates = cursor.fetchall()
        info = 'Среда\n'
        for e in dates:
            if e[2] == "":
                info += f'№{e[0]}. {e[1]} Нет пары\n'
            else:
                info += f'№{e[0]}. {e[3]}, {e[1]} ,  Кабинет:{e[2]},  Преподаватель: {e[4]}  \n'
        bot.send_message(message.chat.id, info)
    elif message.text.lower() == "четверг":
        cursor.execute("SELECT * FROM public.cht")
        dates = cursor.fetchall()
        info = 'Четверг\n'
        for e in dates:
            if e[2] =="":
                info += f'№{e[0]}. {e[1]} Нет пары\n'
            else:
                info += f'№{e[0]}. {e[3]}, {e[1]} ,  Кабинет:{e[2]},  Преподаватель: {e[4]}  \n'
        bot.send_message(message.chat.id, info)
    elif message.text.lower() == "пятница":
        cursor.execute("SELECT * FROM public.pt")
        dates = cursor.fetchall()
        info = 'Пятница\n'
        for e in dates:
            if e[2] =="":
                info += f'№{e[0]}. {e[1]} Нет пары\n'
            else:
                info += f'№{e[0]}. {e[3]}, {e[1]} ,  Кабинет:{e[2]},  Преподаватель: {e[4]}  \n'
        bot.send_message(message.chat.id, info)
    elif message.text.lower() == "расписание на следующую неделю":
        cursor.execute("SELECT * FROM public.pn")
        dates = cursor.fetchall()
        info = 'Расписание на следующую неделю\nПонедельник\n'
        for e in dates:
            if e[2] =="":
                info += f'№{e[0]}. {e[1]} Нет пары\n'
            else:
                info += f'№{e[0]}. {e[3]}, {e[1]} ,  Кабинет:{e[2]},  Преподаватель: {e[4]}  \n'
        cursor.execute("SELECT * FROM public.vt")
        dates = cursor.fetchall()
        info += '\nВторник\n'
        for e in dates:
            if e[2] =="":
                info += f'№{e[0]}. {e[1]} Нет пары\n'
            else:
                info += f'№{e[0]}. {e[3]}, {e[1]} ,  Кабинет:{e[2]},  Преподаватель: {e[4]}  \n'
        cursor.execute("SELECT * FROM public.cp")
        dates = cursor.fetchall()
        info += '\nСреда\n'
        for e in dates:
            if e[2] == "":
                info += f'№{e[0]}. {e[1]} Нет пары\n'
            else:
                info += f'№{e[0]}. {e[3]}, {e[1]} ,  Кабинет:{e[2]},  Преподаватель: {e[4]}  \n'
        cursor.execute("SELECT * FROM public.cht")
        dates = cursor.fetchall()
        info += '\nЧетверг\n'
        for e in dates:
            if e[2] =="":
                info += f'№{e[0]}. {e[1]} Нет пары\n'
            else:
                info += f'№{e[0]}. {e[3]}, {e[1]} ,  Кабинет:{e[2]},  Преподаватель: {e[4]}  \n'
        cursor.execute("SELECT * FROM public.pt")
        dates = cursor.fetchall()
        info += '\nПятница\n'
        for e in dates:
            if e[2] =="":
                info += f'№{e[0]}. {e[1]} Нет пары\n'
            else:
                info += f'№{e[0]}. {e[3]}, {e[1]} ,  Кабинет:{e[2]},  Преподаватель: {e[4]}  \n'
        bot.send_message(message.chat.id, info)
    elif message.text.lower() == "расписание на следующую неделю":
        cursor.execute("SELECT * FROM public.pnn")
        dates = cursor.fetchall()
        info = 'Расписание на следующую неделю\nПонедельник\n'
        for e in dates:
            if e[2] =="":
                info += f'№{e[0]}. {e[1]} Нет пары\n'
            else:
                info += f'№{e[0]}. {e[3]}, {e[1]} ,  Кабинет:{e[2]},  Преподаватель: {e[4]}  \n'
        cursor.execute("SELECT * FROM public.vtn")
        dates = cursor.fetchall()
        info += '\nВторник\n'
        for e in dates:
            if e[2] =="":
                info += f'№{e[0]}. {e[1]} Нет пары\n'
            else:
                info += f'№{e[0]}. {e[3]}, {e[1]} ,  Кабинет:{e[2]},  Преподаватель: {e[4]}  \n'
        cursor.execute("SELECT * FROM public.cpn")
        dates = cursor.fetchall()
        info += '\nСреда\n'
        for e in dates:
            if e[2] == "":
                info += f'№{e[0]}. {e[1]} Нет пары\n'
            else:
                info += f'№{e[0]}. {e[3]}, {e[1]} ,  Кабинет:{e[2]},  Преподаватель: {e[4]}  \n'
        cursor.execute("SELECT * FROM public.chtn1")
        dates = cursor.fetchall()
        info += '\nЧетверг\n'
        for e in dates:
            if e[2] =="":
                info += f'№{e[0]}. {e[1]} Нет пары\n'
            else:
                info += f'№{e[0]}. {e[3]}, {e[1]} ,  Кабинет:{e[2]},  Преподаватель: {e[4]}  \n'
        cursor.execute("SELECT * FROM public.ptn")
        dates = cursor.fetchall()
        info += '\nПятница\n'
        for e in dates:
            if e[2] =="":
                info += f'№{e[0]}. {e[1]} Нет пары\n'
            else:
                info += f'№{e[0]}. {e[3]}, {e[1]} ,  Кабинет:{e[2]},  Преподаватель: {e[4]}  \n'
        bot.send_message(message.chat.id, info)
    else:
        bot.send_message(message.chat.id, "Извините, я Вас не понял")
bot.polling(none_stop=True)
