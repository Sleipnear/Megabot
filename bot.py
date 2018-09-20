from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',

'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

teleg_log=logging.getLogger('telegram.ext.updater')

def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
	user_text = "Привет {}! Ты написал: {}".format (update.message.chat.first_name, update.message.text) 
	logging.info ("User: %s, Chat id: %s, Message: %s", update.message.chat.username, 
					update.message.chat.id, update.message.text)
	update.message.reply_text(user_text)

	def ephems(bot,update):
    text = 'Вызван /ephem'
    print(text)
	update.message.reply_text(text)

def main():
	mybot = Updater(settings. API_KEY, request_kwargs=settings.PROXY)
	logging.info('бот запускается')
	 
	dp = mybot.dispatcher
	dp.add_handler(CommandHandler('start', greet_user))
	dp.add_handler(MessageHandler(Filters.text, talk_to_me))
	dp.add_handler(CommandHandler("ephem", ephems))

	mybot.start_polling()
	mybot.idle()


main()