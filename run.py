import os
import telebot
########################################################################################################################
def api():
    txt = open('api.txt').read().split('\n')
    global bot, adm, adm2
    bot, adm, adm2 = telebot.TeleBot(txt[0]), txt[1], txt[2]
    return bot, adm, adm2


api()

try: os.mkdir("dok")
except: pass

try: os.mkdir("xyz")
except: pass

while True:
     try: exec(open('encoding.py').read())
     except:
          bot.send_message(adm, 'Error')
          try:
               my_file = open('dok/error', 'a')
               text_for_file = 'error;'
               my_file.write(text_for_file)
               my_file.close()
          except:
               my_file = open('dok/error', 'w')
               text_for_file = 'error;'
               my_file.write(text_for_file)
               my_file.close()





