import telebot
from telebot import types  # для указание типов


bot = telebot.TeleBot("6109760153:AAHwLXSdmHJjnc2lX9ggaGXg_ZNE8Z9OjuY")


global lavash


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Создать новый заказ")
    markup.add(btn1)
    bot.send_message(message.chat.id,
                     text="Приветствую! Я бот сети 'Shabway'. Через меня вы можете...".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def choice(message):


    list = []


    list = []
    list.append("Лук")
    list.append("Помидоры")
    list.append("Огурцы")
    list.append("Салат")
    list.append("Халапеньо")


    def check(message):
        list.remove(message.text)
        print(list)

    def time(message):
        print(list)
        markup8 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn8_0 = types.KeyboardButton("Начать готовить сразу")
        btn8_1 = types.KeyboardButton("Приготовить через 10 минут")
        btn8_2 = types.KeyboardButton("Приготовить через 15")
        btn8_3 = types.KeyboardButton("Приготовить через 30 минут")
        btn8_4 = types.KeyboardButton("Приготовить через 45 минут")
        btn8_5 = types.KeyboardButton("Приготовить через час")
        markup8.add(btn8_0, btn8_1, btn8_2, btn8_3, btn8_4, btn8_5)
        bot.send_message(message.chat.id, text="Выберите через сколько сможете забрать заказ:".format(
            message.from_user), reply_markup=markup8)


    def f1(message):
        list.append(message.text)
        print(list)
        markup6 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn7_1 = types.KeyboardButton("Огурцы соленые")
        btn7_2 = types.KeyboardButton("Огурцы малосольные")
        btn7_3 = types.KeyboardButton("Сыр плавленный чеддер")
        btn7_4 = types.KeyboardButton("Сыр плавленный моцарелла")
        btn7_5 = types.KeyboardButton("Морковь по Корейски")
        btn7_6 = types.KeyboardButton("Перец халапеньо")
        btn7_7 = types.KeyboardButton("Картофель фри")
        btn7_8 = types.KeyboardButton("Обжаренный лук")
        btn7_9 = types.KeyboardButton("Без наполнителя")
        markup6.add(btn7_1, btn7_2, btn7_3, btn7_4, btn7_5, btn7_6, btn7_7, btn7_8, btn7_9)
        bot.send_message(message.chat.id, text="Выбрать наполнители:".format(
            message.from_user),reply_markup=markup6)
        bot.register_next_step_handler(message, time)


    def sostav(message):
        print(list)
        markup5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn6_0 = types.KeyboardButton("Не менять состав")
        btn6_1 = types.KeyboardButton("Лук")
        btn6_2 = types.KeyboardButton("Помидоры")
        btn6_3 = types.KeyboardButton("Огурцы")
        btn6_4 = types.KeyboardButton("Салат")
        btn6_5 = types.KeyboardButton("Халапеньо")
        markup5.add(btn6_0, btn6_1, btn6_2, btn6_3, btn6_4, btn6_5)
        bot.send_message(message.chat.id, text="Выберите, какой из ингредиентов по умолчанию вы хотите удалить:".format(
            message.from_user), reply_markup=markup5)
        if message.text == "Не менять состав":
            bot.register_next_step_handler(message, check)
        elif message.text == "Лук":
            print(list)
            bot.register_next_step_handler(message, check)
        bot.register_next_step_handler(message, check)


    def dopsous(message):
        list.append(message.text)
        print(list)
        markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn5_1 = types.KeyboardButton("Барбекю")
        btn5_2 = types.KeyboardButton("Сырный")
        btn5_3 = types.KeyboardButton("Терияки")
        btn5_4 = types.KeyboardButton("Бургер")
        btn5_5 = types.KeyboardButton("Карри")
        btn5_6 = types.KeyboardButton("Брусничный")
        btn5_7 = types.KeyboardButton("Томатный")
        btn5_8 = types.KeyboardButton("Острый сальса")
        btn5_9 = types.KeyboardButton("Чесночный")
        btn5_10 = types.KeyboardButton("Гранатовый")
        btn5_11 = types.KeyboardButton("Без соуса")
        markup4.add(btn5_1, btn5_2, btn5_3, btn5_4, btn5_5, btn5_6, btn5_7, btn5_8, btn5_9, btn5_10, btn5_11)
        bot.send_message(message.chat.id, text="Выберите еще один дополнительный соус:".format(
            message.from_user), reply_markup=markup4)
        bot.register_next_step_handler(message, sostav)


    def sous(message):
        list.append(message.text)
        print(list)
        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn4_1 = types.KeyboardButton("Барбекю")
        btn4_2 = types.KeyboardButton("Сырный")
        btn4_3 = types.KeyboardButton("Терияки")
        btn4_4 = types.KeyboardButton("Бургер")
        btn4_5 = types.KeyboardButton("Карри")
        btn4_6 = types.KeyboardButton("Брусничный")
        btn4_7 = types.KeyboardButton("Томатный")
        btn4_8 = types.KeyboardButton("Острый сальса")
        btn4_9 = types.KeyboardButton("Чесночный")
        btn4_10 = types.KeyboardButton("Гранатовый")
        btn4_11 = types.KeyboardButton("Без соуса")
        markup3.add(btn4_1, btn4_2, btn4_3, btn4_4, btn4_5, btn4_6, btn4_7, btn4_8, btn4_9, btn4_10, btn4_11)
        bot.send_message(message.chat.id, text="Выберите дополнительный соус:".format(
            message.from_user), reply_markup=markup3)
        bot.register_next_step_handler(message, dopsous)


    def meat(message):
        list.append(message.text)
        print(list)
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3_1 = types.KeyboardButton("Индейка")
        btn3_2 = types.KeyboardButton("Куриный шашлык")
        markup2.add(btn3_1, btn3_2)
        bot.send_message(message.chat.id, text="Выберите мясное наполнение шаурмы:".format(
            message.from_user), reply_markup=markup2)
        bot.register_next_step_handler(message, sous)


    if message.text == "Создать новый заказ":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn2_1 = types.KeyboardButton("Светлый лаваш")
        btn2_2 = types.KeyboardButton("Сырный лаваш")
        btn2_3 = types.KeyboardButton("Пита")
        btn2_4 = types.KeyboardButton("Тонкая пита")
        markup1.add(btn2_1, btn2_2, btn2_3, btn2_4)
        bot.send_message(message.chat.id, text="Выберите лаваш:".format(
            message.from_user), reply_markup=markup1)
        bot.register_next_step_handler(message, meat)


bot.polling(none_stop = True)
