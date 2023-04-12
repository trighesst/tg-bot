import telebot
from telebot import types

bot = telebot.TeleBot('6128199622:AAHz4rI2bcPlw2sowf9EUfbiQCp1njNMLZM')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Со скольки лет можно работать?")
    btn2 = types.KeyboardButton("Найти работу.")
    btn3 = types.KeyboardButton("Что я умею?")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот для нахождения работы для подростка.".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def funs(message):
    if(message.text == "Со скольки лет можно работать?"):
        bot.send_message(message.chat.id, text='Подростки могут официально устроиться на работу и оформить трудовую книжку с 14 лет. Для этого понадобится согласие любого из родителей, а также органа опеки и попечительства. С 16 лет молодые люди вправе сами заключать трудовой договор.')
    elif(message.text == "Найти работу."):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Рабочий день до 4 часов.")
        btn2 = types.KeyboardButton("Рабочий день от 4 до 6 часов.")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Выбери нужный тебе график", reply_markup=markup)
        
    elif (message.text == "Что я умею?"):
        bot.send_message(message.chat.id, text='Я твой помощник в трудоустройстве, я даю гарантию что, помогу найти тебе работу за маленький срок, со мной работает множество предприятий, которые ищут себе работников, удачи тебе найти работу, которая тебе понравится.' )
        
    elif (message.text == "Рабочий день до 4 часов."):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Копирайтер.ЗП от 500")
        button2 = types.KeyboardButton("курьер.ЗП от 350")
        button3 = types.KeyboardButton("Промоутер.ЗП от 200")
        markup.add(button1,button2 ,button3 )
        bot.send_message(message.chat.id, "Выбери нужную тебе вакансию", reply_markup=markup)
        
    elif message.text == "Рабочий день от 4 до 6 часов.":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 =  types.KeyboardButton("Програмист.ЗП от 700")
        btn2 = types.KeyboardButton("Оператор горячий линии.ЗП от 500")
        btn3 = types.KeyboardButton("Рекрутер.ЗП от 600")
        markup.add(btn1,btn2 ,btn3 )
        bot.send_message(message.chat.id, text="Выбери нужную тебе вакансию", reply_markup=markup)
    
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Со скольки лет можно работать?")
        button2 = types.KeyboardButton("Найти работу.")
        button3 = types.KeyboardButton("Что я умею?")
        markup.add(button1, button2, button3 )
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

    elif (message.text == "Копирайтер.ЗП от 500", "курьер.ЗП от 350", "Промоутер.ЗП от 200", "Програмист.ЗП от 700", "Оператор горячий линии.ЗП от 500", "Рекрутер.ЗП от 600"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 =  types.KeyboardButton("TeleGram")
        btn2 =  types.KeyboardButton("Телефон")
        markup.add(btn1,btn2)
        bot.send_message(message.chat.id, text="Хорошо, теперь выбери где тебе проще связаться",  reply_markup=markup)
        
    elif (message.text == "Телефон"):
        markup = types.InlineKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton(text='Написать номер')
        markup.add(btn1)
        bot.send_message(message.chat.id,"Напишите свой номер телефона", reply_markup = markup)
        
        
            
        
        
        
        
        
bot.polling(none_stop=True)


