from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem
import datetime

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',

'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

planets_ephem = ['Sun','Mercury','Venus', 'Earth', 'Mars', 'Jupiter','Saturn', 'Uranus', 'Neptune']

def start_message(bot, update):
    text_start = 'Привет' \
                 '\n Здесь ты узнаешь нахождение планеты в определенный период времени.\n' \
                 'Используй /planet [Название планеты на английском языке]'
    update.message.reply_text(text_start)


def planets(bot, update):
    text_user = update.message.text.split(' ')
    print(text_user, text_user[1])
    print (text_user[1] in planets_ephem)
    print (planets_ephem)

    if text_user[1] in planets_ephem:
        print("in if")
        planet_info = getattr(ephem, text_user[1])
        print(planet_info)
        planet = planet_info('23/08/2013')
        print(planet)
        update.message.reply_text('Ваша планета находиться в созвездии:')
        update.message.reply_text(ephem.constellation(planet)[1])
    else:
        update.message.reply_text('Не работает :(')
        print(text_user[1], text_user)

def main():
    mybot = Updater(settings. API_KEY, request_kwargs=settings.PROXY)
    logging.info('бот запускается')
     
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', start_message))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler('planet', planets))

    mybot.start_polling()
    mybot.idle()


main()

print(dir(ephem))