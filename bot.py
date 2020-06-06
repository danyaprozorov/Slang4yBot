import telebot
import cfg

bot = telebot.TeleBot(cfg.TOKEN)


@bot.message_handler(content_types=['text'])
def rep(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
