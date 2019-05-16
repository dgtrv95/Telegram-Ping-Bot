import os
import telebot

hostname = 'ip server or url'
channel = '@************'
token = '*************'

response = os.system('ping ' + hostname)
bot = telebot.TeleBot(token)


if response == 0:
  print(hostname + ' is up!')
else:
  print(hostname + ' is down!')
  bot.send_message(channel, hostname + ' is down!')
