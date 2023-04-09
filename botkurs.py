import telebot  # telebot (pyTelegramBotAPI) импортируем библиотеку для создания бота на python
from telebot import types  # для того чтобы кнопки заработали, нужно импортировать типы
from configkurs import token  # из файла configkurs забираем переменную с токеном

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
# описание команды старт
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Где купить продукт")
    btn2 = types.KeyboardButton("Справка о продуктах")
    btn3 = types.KeyboardButton("Найти рецепт")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,
                     text="Привет! 👋\n"
                          "\n"
                          "*Я БОТ для домашних кондитеров.*\n"
                          "\n"
                          "Муку для приготовления сладкого десерта можно найти в любом магазине.😉\n"
                          "❗ Я вам расскажу:\n"
                          "👉 где найти остальные ингредиенты\n"
                          "👉 сможете узнать полезную информацию о продуктах\n"
                          "👉 покажу несколько рецептов чудесных сладких десертов\n"
                          "\n"
                          "*Нажмите пожалуйста необходимую кнопку* 👇", parse_mode="Markdown", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    # описание кнопки Где купить продукт
    if message.text == "Где купить продукт":
        buttons = types.InlineKeyboardMarkup(row_width=1)
        button1 = types.InlineKeyboardButton('➡ Секретный ингредиент (агар, пектин и т.п.)', callback_data='but1')
        button2 = types.InlineKeyboardButton('➡ Шоколад или глазурь', callback_data='but2')
        button3 = types.InlineKeyboardButton('➡ Сливки или сыр', callback_data='but3')
        button4 = types.InlineKeyboardButton('➡ Хочу купить продукты как юридическое лицо', callback_data='but4')
        buttons.add(button1, button2, button3, button4)
        bot.send_message(message.chat.id, text='Выберите продукт который вы хотите купить 👇 ', reply_markup=buttons)
    # описание кнопки Справка о продуктах
    elif message.text == "Справка о продуктах":
        buttons1 = types.InlineKeyboardMarkup(row_width=1)
        button1_1 = types.InlineKeyboardButton('ℹ Какао алкализованное и натуральное',
                                               url="https://www.chocoluxe.ru/articles/chocolate/"
                                                   "what-cocoa-powder-to-choose-natural-vs-alkalized/")
        button1_2 = types.InlineKeyboardButton('ℹ Мастика кондитерская',
                                               url="https://lv-cake.ru/chto-takoe-mastika-dlya-torta/")
        button1_3 = types.InlineKeyboardButton('ℹ Загуститель для сливок',
                                               url="https://paulinecakeclub.ru/"
                                                   "vsyo-pro-zagustitel-dlya-slivok/")
        button1_4 = types.InlineKeyboardButton('ℹ Агар-агар',
                                               url="https://pikabu.ru/story/chto_"
                                                   "takoe_agaragar_i_kak_ego_ispolzovat_6161475")
        buttons1.add(button1_1, button1_2, button1_3, button1_4)
        bot.send_message(message.chat.id, text='Выберите продукт 👇, о котором вы хотите узнать 🧑‍🏫',
                         reply_markup=buttons1)
    # описание кнопки Найти рецепт
    elif message.text == "Найти рецепт":
        buttons2 = types.InlineKeyboardMarkup(row_width=1)
        button2_1 = types.InlineKeyboardButton('☑ Зефир', url="https://www.youtube.com/watch?v=AMb18tRPC3c")
        button2_2 = types.InlineKeyboardButton('☑ Бисквит', url="https://www.youtube.com/watch?v=5SRR9td_MQs")
        button2_3 = types.InlineKeyboardButton('☑ Имбирный пряник', url="https://www.youtube.com/watch?v=yDEnDcMihqg")
        button2_4 = types.InlineKeyboardButton('☑ Меренговый рулет', url="https://www.youtube.com/watch?v=hXyrcRbvnTc")
        buttons2.add(button2_1, button2_2, button2_3, button2_4)
        bot.send_message(message.chat.id, text='❓ Что вы хотите приготовить 👨‍🍳', reply_markup=buttons2)
    # описание если пользователь напишет слово shop
    elif message.text.lower() == "shop":
        bot.send_message(message.from_user.id, '❗ *Специализированные магазины для кондитеров*\n'
                                               'стремятся к тому, чтобы у них кондитеры, которые пекут торты '
                                               'в домашних условиях, смогли '
                                               'приобрести всё необходимое для кондитерского ремесла.\n'
                                               '\n'
                                               '☑ В Минске это магазины 👇\n'
                                               '🔹 *BakenArt* [Ссылка на интернет-магазин](https://bakenart.by/)\n'
                                               '🔹 *Хлеб Кондитера* '
                                               '[Ссылка на интернет-магазин](https://hleb-konditera.by/)\n'
                                               '🔹 *Ярада* [Ссылка на интернет-магазин](https://ярада.бел/)\n'
                                               '\n'
                                               '☑ Аналогичные магазины есть в областных и районных центрах Беларуси.\n'
                                               'Например 👇:\n'
                                               '🔹 В Гомеле это *Тортодел* '
                                               '[Ссылка на интернет-магазин](http://tortodel.by/)\n'
                                               '🔹 В Бресте это *Мир кондитера* '
                                               '[Ссылка на интернет-магазин](http://mirkonditera.by/)\n'
                                               '\n'
                                               '☑ Специализированных магазинов очень много по всей Беларуси. \n'
                                               'Хотите найти такой у себя в городе\n'
                                               'просто вбейте в поисковике 👇 \n'
                                               '💻 *магазин для кондитера* и название Вашего города \n'
                                               'и Вы получите всю необходимую информацию.😉', parse_mode="Markdown")
    # если в сообщении от пользователя написана неправильная команда или непонятные слова
    else:
        bot.send_message(message.chat.id, text="😕 На такую команду я не запрограммирован... 🤷‍♀️")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # описание кнопки Секретные ингредиенты из кнопки Меню - Где купить продукт
    if call.data == 'but1':
        bot.send_message(call.message.chat.id, text='Данные продукты Вы можете найти:\n'
                                                    '➡ в любых сетевых розничных магазинах \n'
                                                    '(смотрите отдел с приправами)\n'
                                                    '➡ в специализированных магазинах для кондитеров\n'
                                                    '➡ на масс-маркетах Wildberries и Ozon\n'
                                                    '\n'
                                                    '❗ Хотите узнать \n'
                                                    'о специализированных магазинах для кондитеров напишите \n'
                                                    '*shop*', parse_mode="Markdown")
        bot.answer_callback_query(call.id)
    # описание кнопки Шоколад или глазурь из кнопки Меню - Где купить продукт
    elif call.data == 'but2':
        bot.send_message(call.message.chat.id, text='Для покрытия изделия шоколадом 🍩 можно использовать шоколадку🍫,'
                                                    ' купленную в любом розничном магазине.\n'
                                                    'Её надо будет просто растопить.\n'
                                                    '\n'
                                                    'А можно купить шоколад в каллетах(монетках).\n'
                                                    'Его удобнее топить.\n'
                                                    'Такой шоколад продаётся в специализированных '
                                                    'магазинах для кондитеров. \n'
                                                    '\n'
                                                    '❗ Хотите узнать \n'
                                                    'о специализированных магазинах для кондитеров напишите \n'
                                                    '*shop*\n'
                                                    '\n'
                                                    'Узнать о кондитерском шоколаде и его отличиях от обычного можно ' +
                                                    '[ТУТ](https://shokolad.today/chocolatier/konditerskiy-shokolad)\n'
                                                    '\n'
                                                    'Глазурь, которая заменяет шоколад, '
                                                    'тоже продаётся в специализированных магазинах\n'
                                                    '\n', parse_mode="Markdown")
        bot.answer_callback_query(call.id)
        # описание кнопки Сливки или сыр из кнопки Меню - Где купить продукт
    elif call.data == 'but3':
        bot.send_message(call.message.chat.id,
                         text='‼ Самый большой выбор сыров и сливок в сетевых гипермаркетах.\n'
                              'У них вы можете заказать доставку продуктов "на дом".\n'
                              '\n'
                              '▪ В магазинах формата "у дома" выбор очень ограничен.\n'
                              '\n'
                              '▪ В специализированных магазинах для кондитеров тоже можно приобрести и сыр и сливки. \n'
                              '\n'
                              '❗ Хотите узнать \n'
                              'о специализированных магазинах для кондитеров напишите \n'
                              '*shop*', parse_mode="Markdown")

        bot.answer_callback_query(call.id)
    # описание кнопки Хочу купить продукты как юридическое лицо из кнопки Меню - Где купить продукт
    elif call.data == 'but4':
        bot.send_message(call.message.chat.id,
                         text='Есть большой выбор компаний, который продаёт '
                              'кондитерские ингредиенты юридическим лицам.\n'
                              '🔸 *Шоколад кондитерский в монетках* \n'
                              'Вы можете приобрести у компании '
                              '*Велес-Фуд* ' + '[ИХ САЙТ](https://velesfood.com/)\n'
                              '\n'
                              '🔸 *Творожный сыр марки Креметта* \n'
                              'Вы можете приобрести у компании *ИмЭкс Трейд* ' +
                              '[ИХ САЙТ](https://imextrade.by/)\n'
                              'или\n'
                              'можно приобрести творожные сыры белорусских производителей:\n'
                              '🟢 *Туровский молочный комбинат* ' + '[ИХ САЙТ](https://turovmilk.by/)\n'
                              '🟢 *Молочный мир* ' + '[ИХ САЙТ](https://milk.by/)\n'
                              '🟢 *Праймилк* ' + '[ИХ САЙТ](https://primemilk.by/)\n'
                              '\n'
                              '*🔸 Сливки ... * Если хотите приготовить сладкий десерт. то вам нужны сливки 33%. \n'
                              'Только они взбиваются до нужной консистенции\n'
                              '\n'
                              '*Сливки Петмол*\n'
                              'Вы можете приобрести у представительства компании Danone в Минске '
                              + '[ИХ САЙТ](https://danone.by/)\n'
                              'или\n'
                              'можно приобрести сливки, которые произведены в Республике Беларусь:\n'
                              '🟢 *Молочный гостинец* ' + '[ИХ САЙТ](https://www.molgost.by/)\n'
                              '🟢 *Молочный мир* ' + '[ИХ САЙТ](https://milk.by/)\n'
                              '🟢 *Милкавита* ' + '[ИХ САЙТ](https://milkavita.by/)\n'
                              '\n'
                              '*🔸 Кондитерскую глазурь*\n'
                              'Вы можете приобрести непосредственно у белорусского производителя Белга-Пром\n'
                              'Узнать информацию о них можно по ' + '[ссылке](https://belgaprom.propartner.by/)\n'
                              '\n'
                              '🔸 *Секретные ингредиенты (агар, пектин и другие)*\n'
                              'Вы можете приобрести у следующих компаний:\n'
                              '🟢 *Продхимснаб* ' + '[ИХ САЙТ](https://phs.by/)\n'
                              '🟢 *Барса* ' + '[ИХ САЙТ](https://www.barsa.by/)\n'
                              'Компании находятся в Минске, но осуществляют доставку по всей Беларуси.',
                         parse_mode="Markdown")

        bot.answer_callback_query(call.id)


# запускаем бота
bot.polling(none_stop=True, interval=0)
