import telebot
from telebot import types
import json
from interpreter import token_interpreter
from interpreter import yandex_translator as text

tok = token_interpreter.token

bot = telebot.TeleBot(tok)

language = 'ru_en'


main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn_ru_en = types.KeyboardButton('ru-en')
btn_en_ru = types.KeyboardButton('en_ru')
btn_ru_zh = types.KeyboardButton('ru_zh')
btn_zh_ru = types.KeyboardButton('zh_ru')
btn_ru_tr = types.KeyboardButton('ru_tr')
btn_tr_ru = types.KeyboardButton('tr_ru')
btn_ru_de = types.KeyboardButton('ru_de')
btn_de_ru = types.KeyboardButton('de_ru')
main_menu.add(btn_ru_en,btn_en_ru,btn_ru_zh,btn_zh_ru
              ,btn_ru_tr,btn_tr_ru,btn_ru_de,btn_de_ru)

def text_translation(user_text,language):
    """
    Функция передает 2 параметра в модуль для перевода,
    потом передаем ответ точке вызова.
    """
    transit= text.translate_me(user_text,language)
    return transit

@bot.message_handler(commands=['start'])
def greeting(message):
    #  Приветствует пользователя.
    bot.send_message(message.chat.id,'Привет мой друг!\n'
                                     'Готов перевести все, что вы пишете',reply_markup=main_menu)


@bot.message_handler(commands=['ru_en','en_ru','ru_zh'
                               ,'zh_ru','ru_tr','tr_ru'
                               ,'ru_de','de_ru'])
def select_a_language(message):
    # Иницилизируем артикуль стран для перевода
    global language
    bot.send_message(message.chat.id, 'Готов перевести все, что вы пишете!')
    language = message.text.lower()[1:]

@bot.message_handler(commands=['info'])
def the_description_of_the_bot(message):
    # Выводим сведения о Боте.
    info = ''
    try:
        file_info = 'info.json'
        with open(file_info,'r') as file:
            info = json.load(file)
    except:
        info = 'Нет никакой информации!'
    bot.send_message(message.chat.id,info)



@bot.message_handler(commands=['language'])
def select_a_language(message):
    #  ВЫводим список языков перевода.
    bot.send_message(message.chat.id,'Вот список языков для перевода \n'
                                     '/ru_en Русский-Англиский\n'
                                     '/en_ru Англиский-Русский\n'
                                     '/ru_zh Русский-Китайский\n'
                                     '/zh_ru Китайский-Русский\n'
                                     '/ru_tr Русский-Турецский\n'
                                     '/tr_ru Турецский-Русский\n'
                                     '/ru_de Русский-Немецский\n'
                                     '/de_ru Немецский-Русский')




@bot.message_handler(content_types=['text'])
def translation_of_polotchane(message):
    #  Модуль переводит введеный текст поумолчанию с Русского на Англиский.
    global language
    language_ = {'ru_en':'ru-en','en_ru':'en-ru','ru_zh':'ru-zh'
                 ,'zh_ru':'zh-ru','ru_tr':'ru-tr','tr_ru':'tr-ru'
                 ,'ru_de':'ru-de','de_ru':'de-ru'}
    input_value= message.text
    answer = text_translation(input_value,language_[language])

    bot.send_message(message.chat.id,answer)


bot.polling()




