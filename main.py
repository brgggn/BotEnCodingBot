########################################################################################################################
import time

import telebot
from telebot import types
from key import *
########################################################################################################################
from f_def import *
from book import *
########################################################################################################################
# сохраняет все пользовательские файлы

vocalist = 'Brigitte Bardot'
music = 'inside/'+'Moi Je Joue'+'.m4a'
########################################################################################################################

########################################################################################################################
# start
def a_start(message):
    file = 'dok/star_user'
    try:
        my_file = open(file, 'r')
        fr = (my_file.read()).split(';')

        if str(message.chat.id) not in fr:
            my_file = open(file, 'a')
            b_start(message, my_file)

    except IOError as e:
        my_file = open(file, 'w')
        b_start(message, my_file)

    if str(message.chat.id) in adm:
        time.sleep(0.5)
        bot.send_message(message.chat.id, start()[1])
        time.sleep(0.5)
        bot.send_message(message.chat.id, start()[3])
        time.sleep(0.5)
    else:
        time.sleep(0.5)
        bot.send_message(message.chat.id, start()[1])
        time.sleep(0.5)
    a_menu(message)

def b_start(message, my_file):
    try:
        chat_id = str(message.chat.id) + ';'
        my_file.write(chat_id)
        bot.send_message(message.chat.id, f'{start()[0]}, {message.chat.first_name}')
    except: bot.send_message(message.chat.id, mes_txt('error1'))

########################################################################################################################
def a_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(types.KeyboardButton(keyboard('simplecommands')))
    markup.row(types.KeyboardButton(keyboard('coding')))
    markup.row(types.KeyboardButton(keyboard('conversion')))
    markup.row(types.KeyboardButton(keyboard('about')))

    bot.send_message(message.chat.id, 'menu', reply_markup=markup)


########################################################################################################################
# settings
def a_settings(message):
    file = 'dok/mes_user'
    try:
        my_file = open(file, 'r')
        fr = (my_file.read()).split(';')
        if str(message.chat.id) in fr:
            bot.send_message(message.chat.id, text=mes_txt('ofnotice'), reply_markup=inline_comand('ofnotice'))
        else: bot.send_message(message.chat.id, text=mes_txt('innotice'), reply_markup=inline_comand('innotice'))
    except: bot.send_message(message.chat.id, text=mes_txt('innotice'), reply_markup=inline_comand('innotice'))

def a_innotice(message):
    file = 'dok/mes_user'
    try:
        my_file = open(file, 'r')
        fr = (my_file.read()).split(';')

        if str(message.chat.id) not in fr:
            chat_id = str(message.chat.id) + ';'
            my_file = open(file, 'a')
            my_file.write(chat_id)

    except IOError as e:
        my_file = open(file, 'w')
        b_start(message, my_file)

def a_ofnotice(message):
    file = 'dok/mes_user'
    try:
        my_file = open(file, 'r')
        fr = (my_file.read()).split(';')
        if str(message.chat.id) in fr:

            fr.remove(str(message.chat.id))
            chat_id = ''
            for i in range(len(fr)):
                if fr[i] == '': pass
                else:
                    chat_id += fr[i] + ';'

            my_file = open(file, 'w')
            my_file.write(chat_id)

    except IOError as e:
        my_file = open(file, 'w')
        b_start(message, my_file)
########################################################################################################################
# inimage
def a_inimage(message):
    try:
        msg = bot.send_message(message.chat.id, mes_txt('inimage1'))
        bot.register_next_step_handler(msg, b_inimage)

    except: bot.send_message(message.chat.id, mes_txt('error1'))

def b_inimage(message):
    try:
        file_pfoto = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_pfoto.file_path)
        src = str(message.chat.id) + '.bmp'
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        msg = bot.send_message(message.chat.id, mes_txt('inimage2'))
        bot.register_next_step_handler(msg, c_inimage)

    except: bot.send_message(message.chat.id, mes_txt('error1'))

def c_inimage(message):
    try:
        user_id = str(message.chat.id)
        f_inimage(user_id, message.text)
        image_new = f'{user_id}new.gif'
        doc = open(image_new, 'rb')
        bot.send_document(user_id, doc)
        doc.close()
        os.remove(image_new)
        bot.send_message(message.chat.id, text=mes_txt('reiteration'), reply_markup=inline_comand('image'))

    except: bot.send_message(message.chat.id, mes_txt('error1'))
########################################################################################################################
# ofimage
def a_ofimage(message):
    try:
        if message.chat.type == 'private':
            msg = bot.send_message(message.chat.id, mes_txt('ofimage1'))
            bot.register_next_step_handler(msg, b_ofimage)

    except: bot.send_message(message.chat.id, mes_txt('error1'))

def b_ofimage(message):
    try:
        if message.chat.type == 'private':
            document_id = message.document.file_id
            file_info = bot.get_file(document_id)
            downloaded_file = bot.download_file(file_info.file_path)

            src = f'{str(message.chat.id)}new.gif'
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)

            user_id = str(message.chat.id)
            bot.send_message(str(message.chat.id), f_ofimage(user_id))
            bot.send_message(message.chat.id, text=mes_txt('reiteration'), reply_markup=inline_comand('image'))

    except: bot.send_message(message.chat.id, mes_txt('error1'))
########################################################################################################################
# caesar
def a_caesar(message):
    print(0)
    try:
        msg = bot.send_message(message.chat.id, mes_txt('caesar1'))
        bot.register_next_step_handler(msg, b_caesar)

    except: bot.send_message(message.chat.id, mes_txt('error1'))

def b_caesar(message):
    print(1)
    try:
        file = f'{str(message.chat.id)}'
        open_file = open(file, 'w')
        open_file.write(str(message.text))
        open_file.close()
        markup = inline_comand('caesar')
        bot.send_message(message.chat.id, text=mes_txt('shag'), reply_markup=markup)
        print(2)

    except: bot.send_message(message.chat.id, mes_txt('error1'))

def c_caesar(message, shag):
    try:
        file = f'{str(message.chat.id)}'
        open_file = open(file, 'r')
        text = open_file.read()
        open_file.close()
        os.remove(file)
        bot.send_message(message.chat.id, f_caesar(str(shag), text))
        bot.send_message(message.chat.id, text=mes_txt('reiteration'), reply_markup=inline_comand('coding'))

    except: bot.send_message(message.chat.id, mes_txt('error1'))
########################################################################################################################
# invigenere
def a_invigenere(message):
    try:
        msg = bot.send_message(message.chat.id, mes_txt('invigenere1'))
        bot.register_next_step_handler(msg, b_invigenere)

    except: bot.send_message(message.chat.id, mes_txt('error1'))

def b_invigenere(message):
    try:
        file = f'{str(message.chat.id)}'
        open_file = open(file, 'w')
        open_file.write(str(message.text))
        open_file.close()

        msg = bot.send_message(message.chat.id, mes_txt('invigenere2'))
        bot.register_next_step_handler(msg, c_invigenere)

    except: bot.send_message(message.chat.id, mes_txt('error1'))

def c_invigenere(message):
    try:
        file = f'{str(message.chat.id)}'
        open_file = open(file, 'r')
        text = open_file.read()
        open_file.close()
        os.remove(file)

        key  = str(message.text)

        bot.send_message(message.chat.id, f_vigenere('+', key, text))
        bot.send_message(message.chat.id, text=mes_txt('reiteration'), reply_markup=inline_comand('vigenere'))

    except: bot.send_message(message.chat.id, mes_txt('error1'))
########################################################################################################################
# ofvigenere
def a_ofvigenere(message):
    try:
        msg = bot.send_message(message.chat.id, mes_txt('ofvigenere1'))
        bot.register_next_step_handler(msg, b_ofvigenere)

    except: bot.send_message(message.chat.id, mes_txt('error1'))

def b_ofvigenere(message):
    try:
        file = f'{str(message.chat.id)}'
        open_file = open(file, 'w')
        open_file.write(str(message.text))
        open_file.close()

        msg = bot.send_message(message.chat.id, mes_txt('ofvigenere2'))
        bot.register_next_step_handler(msg, c_ofvigenere)

    except: bot.send_message(message.chat.id, mes_txt('error1'))

def c_ofvigenere(message):
    try:
        file = f'{str(message.chat.id)}'
        open_file = open(file, 'r')
        text = open_file.read()
        open_file.close()
        os.remove(file)

        key  = str(message.text)

        bot.send_message(message.chat.id, f_vigenere('-', key, text))
        bot.send_message(message.chat.id, text=mes_txt('reiteration'), reply_markup=inline_comand('vigenere'))

    except: bot.send_message(message.chat.id, mes_txt('error1'))
########################################################################################################################
# inmorse
def a_inmorse(message):
    try:
        msg = bot.send_message(message.chat.id, mes_txt('inmorse1'))
        bot.register_next_step_handler(msg, b_inmorse)

    except: bot.send_message(message.chat.id, mes_txt('error1'))

def b_inmorse(message):
    try:
        bot.send_message(message.chat.id, f_inmorse(str(message.text)))
        bot.send_message(message.chat.id, text=mes_txt('reiteration'), reply_markup=inline_comand('morse'))

    except: bot.send_message(message.chat.id, mes_txt('error1'))
########################################################################################################################
# ofmorse
def a_ofmorse(message, lang):
    try:
        file = f'{str(message.chat.id)}'
        open_file = open(file, 'w')
        open_file.write(str(lang))
        open_file.close()
        msg = bot.send_message(message.chat.id, mes_txt('ofmorse1'))
        bot.register_next_step_handler(msg, b_ofmorse)
    except: bot.send_message(message.chat.id, mes_txt('error1'))

def b_ofmorse(message):
    try:
        file = f'{str(message.chat.id)}'
        open_file = open(file, 'r')
        lang = open_file.read()
        open_file.close()
        os.remove(file)
        bot.send_message(message.chat.id, f_ofmorse(str(message.text), lang))
        bot.send_message(message.chat.id, text=mes_txt('reiteration'), reply_markup=inline_comand('morse'))  #

    except: bot.send_message(message.chat.id, mes_txt('error1'))
########################################################################################################################
# transn
def a_transn(message):
    try:
        file = f'{str(message.chat.id)}'

        open_file = open(file, 'r')
        nk = open_file.read()
        nk = nk.split(';')

        open_file.close()

        n = nk[0]
        k = nk[1]

        msg = bot.send_message(message.chat.id, mes_txt('transn3')+f'\n\n{n} -> {k}')
        bot.register_next_step_handler(msg, b_transn)
    except: bot.send_message(message.chat.id, mes_txt('error1'))

def b_transn(message):
    try:
        file = f'{str(message.chat.id)}'

        open_file = open(file, 'r')
        nk = open_file.read()
        nk = nk.split(';')

        open_file.close()
        os.remove(file)

        n = nk[0]
        k = nk[1]
        a = str(message.text)

        bot.send_message(message.chat.id, f'{n} -> {k}\n\n{a} -> {f_trans(int(n), a, int(k))}')
        bot.send_message(message.chat.id, text=mes_txt('reiteration'), reply_markup=inline_comand('conversion'))
    except: bot.send_message(message.chat.id, mes_txt('error1'))
########################################################################################################################
# inbin
def a_inbin(message):
    try:
        msg = bot.send_message(message.chat.id, mes_txt('inbin1'))
        bot.register_next_step_handler(msg, b_inbin)
    except: bot.send_message(message.chat.id, mes_txt('error1'))

def b_inbin(message):
    try:
        bot.send_message(message.chat.id, f_inbin(str(message.text)))
        bot.send_message(message.chat.id, text=mes_txt('reiteration'), reply_markup=inline_comand('bin'))
    except: bot.send_message(message.chat.id, mes_txt('error1'))
########################################################################################################################
# ofbin
def a_ofbin(message):
    try:
        msg = bot.send_message(message.chat.id, mes_txt('ofbin1'))
        bot.register_next_step_handler(msg, b_ofbin)
    except: bot.send_message(message.chat.id, mes_txt('error1'))

def b_ofbin(message):
    try:
        bot.send_message(message.chat.id, f_ofbin(str(message.text)))
        bot.send_message(message.chat.id, text=mes_txt('reiteration'), reply_markup=inline_comand('bin'))
    except: bot.send_message(message.chat.id, mes_txt('error1'))
########################################################################################################################
# inurl
def a_inurl(message):
    try:
        msg = bot.send_message(message.chat.id, mes_txt('inurl1'))
        bot.register_next_step_handler(msg, b_inurl)
    except: bot.send_message(message.chat.id, mes_txt('error1'))

def b_inurl(message):
    try:
        bot.send_message(message.chat.id, f_inurl(str(message.text)))
        bot.send_message(message.chat.id, text=mes_txt('reiteration'), reply_markup=inline_comand('url'))
    except: bot.send_message(message.chat.id, mes_txt('error1'))
########################################################################################################################
# ofurl
def a_ofurl(message):
    try:
        msg = bot.send_message(message.chat.id, mes_txt('ofurl1'))
        bot.register_next_step_handler(msg, b_ofurl)
    except: bot.send_message(message.chat.id, mes_txt('error1'))

def b_ofurl(message):
    try:
        bot.send_message(message.chat.id, f_ofurl(str(message.text)))
        bot.send_message(message.chat.id, text=mes_txt('reiteration'), reply_markup=inline_comand('url'))
    except: bot.send_message(message.chat.id, mes_txt('error1'))
########################################################################################################################
# qr
def a_qr(message):
    try:
        msg = bot.send_message(message.chat.id, mes_txt('qr1'))
        bot.register_next_step_handler(msg, b_qr)
    except: bot.send_message(message.chat.id, mes_txt('error1'))

def b_qr(message):
    try:
        qr_name = str(message.chat.id) + '.png'

        f_qr(str(message.text), qr_name)
        qr = open(qr_name, 'rb')
        bot.send_photo(message.chat.id, qr)
        qr.close()
        os.remove(qr_name)
        bot.send_message(message.chat.id, text=mes_txt('reiteration'), reply_markup=inline_comand('simplecommands'))
    except: bot.send_message(message.chat.id, mes_txt('error1'))

########################################################################################################################
# color
def a_color(message):
    try:
        msg = bot.send_message(message.chat.id, mes_txt('color1'))
        bot.register_next_step_handler(msg, b_color)
    except:
        bot.send_message(message.chat.id, mes_txt('error1'))

def b_color(message):
    try:
        color_name = str(message.chat.id) + '.png'
        text = (str(message.text)).split()
        r, g, b = text
        color(int(r), int(g), int(b), color_name)
        col = open(color_name, 'rb')
        bot.send_photo(message.chat.id, col)
        col.close()
        os.remove(color_name)

        bot.send_message(message.chat.id, text=mes_txt('reiteration'), reply_markup=inline_comand('simplecommands'))
    except:
        bot.send_message(message.chat.id, mes_txt('error1'))

########################################################################################################################
# randp
def a_randp(message):
    try:
        msg = bot.send_message(message.chat.id, mes_txt('randp'))
        bot.register_next_step_handler(msg, b_randp)
    except: bot.send_message(message.chat.id, mes_txt('error1'))

def b_randp(message):
    try:
        bot.send_message(message.chat.id, f_randp(int(message.text)))
        bot.send_message(message.chat.id, text=mes_txt('reiteration'), reply_markup=inline_comand('simplecommands'))
    except: bot.send_message(message.chat.id, mes_txt('error1'))
########################################################################################################################
# dnup
def a_dnup(message):
    try:
        msg = bot.send_message(message.chat.id, mes_txt('dnup1'))
        bot.register_next_step_handler(msg, b_dnup)
    except: bot.send_message(message.chat.id, mes_txt('error1'))

def b_dnup(message):
    try:
        file = f'{str(message.chat.id)}'

        open_file = open(file, 'w')
        open_file.write(str(message.text))
        open_file.close()

        bot.send_message(message.chat.id, text=mes_txt('dnup2'), reply_markup=inline_comand('dnup'))
    except: bot.send_message(message.chat.id, mes_txt('error1'))

def a_dn(message):
    try:
        file = f'{str(message.chat.id)}'

        open_file = open(file, 'r')
        text = open_file.read()
        open_file.close()
        os.remove(file)
        bot.send_message(message.chat.id, f_dn(text))
        bot.send_message(message.chat.id, text=mes_txt('reiteration'), reply_markup=inline_comand('simplecommands'))
    except: bot.send_message(message.chat.id, mes_txt('error1'))

def a_up(message):
    try:
        file = f'{str(message.chat.id)}'

        open_file = open(file, 'r')
        text = open_file.read()
        open_file.close()
        os.remove(file)
        bot.send_message(message.chat.id, f_up(text))
        bot.send_message(message.chat.id, text=mes_txt('reiteration'), reply_markup=inline_comand('simplecommands'))
    except: bot.send_message(message.chat.id, mes_txt('error1'))

def a_pund(message):
    try:
        file = f'{str(message.chat.id)}'

        open_file = open(file, 'r')
        text = open_file.read()
        open_file.close()
        os.remove(file)
        bot.send_message(message.chat.id, f_pund(text))
        bot.send_message(message.chat.id, text=mes_txt('reiteration'), reply_markup=inline_comand('simplecommands'))
    except: bot.send_message(message.chat.id, mes_txt('error1'))
########################################################################################################################
def a_ms(message):
    try:
        msg = bot.send_message(message.chat.id, mes_txt('ms1'))
        bot.register_next_step_handler(msg, b_ms)
    except: bot.send_message(message.chat.id, mes_txt('error1'))

def b_ms(message):
    try:
        file = 'xyz/ms.txt'
        text = str('@' + message.chat.username) + ' - ' + str(message.text)+'\n'
        try:
            open_file = open(file, 'a')
        except:
            open_file = open(file, 'w')
        open_file.write(str(text))
        open_file.close()

        bot.send_message(message.chat.id, text=mes_txt('ms2'))
        bot.send_message(message.chat.id, text=mes_txt('reiteration'), reply_markup=inline_comand('simplecommands'))
        bot.send_message(adm, text=text)
    except: bot.send_message(message.chat.id, mes_txt('error1'))

########################################################################################################################
@bot.message_handler(commands=['Help', 'help', 'Start', 'start'])
def c_start(message): a_start(message)

@bot.message_handler(commands=['Settings', 'settings'])
def c_gmenu(message): a_settings(message)

@bot.message_handler(commands=['Gmenu', 'gmenu'])
def c_gmenu(message): bot.send_message(message.chat.id, text='gmenu:', reply_markup=inline_comand('gmenu'))

@bot.message_handler(commands = ['Menu', 'menu'])
def c_menu(message):
    a_menu(message)


########################################################################################################################
@bot.message_handler(commands=['Image', 'image'])
def c_image(message): bot.send_message(message.chat.id, text='image:', reply_markup=inline_comand('image'))

@bot.message_handler(commands=['Caes', 'caes'])
def c_caes(message): a_caesar(message)

@bot.message_handler(commands=['Vigenere', 'vigenere'])
def c_vigenere(message): bot.send_message(message.chat.id, text='vigenere:', reply_markup=inline_comand('vigenere'))

@bot.message_handler(commands=['Morse', 'morse'])
def c_morse(message): bot.send_message(message.chat.id, text='morse', reply_markup=inline_comand('morse'))

@bot.message_handler(commands=['Transn', 'transn'])
def c_transn(message): bot.send_message(message.chat.id, text=mes_txt('transn1')+'\n__ -> __', reply_markup=inline_comand('transn1'))

@bot.message_handler(commands=['Bin', 'bin'])
def c_bin(message): bot.send_message(message.chat.id, text=mes_txt('bin'), reply_markup=inline_comand('bin'))

@bot.message_handler(commands=['Url', 'url'])
def c_url(message): bot.send_message(message.chat.id, text=mes_txt('url'), reply_markup=inline_comand('url'))

@bot.message_handler(commands=['Qr', 'qr'])
def c_qrcode(message): a_qr(message)

@bot.message_handler(commands=['Color', 'color'])
def c_color(message): a_color(message)

@bot.message_handler(commands=['Randp', 'randp'])
def c_randpass(message): a_randp(message)

@bot.message_handler(commands=['Dnup', 'dnup'])
def c_dnup(message): a_dnup(message)

@bot.message_handler(commands=['Ms', 'ms'])
def c_dnup(message): a_ms(message)

@bot.message_handler(commands=['101'])
def one_zero_one(message):
    bot.send_audio(message.chat.id, open(music, 'rb'), '', '', vocalist)
    for i in range(len(adm)):
        bot.send_message(adm[i], f'music - @{message.chat.username}')
########################################################################################################################
def a_bot(message):
    try:
        bot.send_message(message.chat.id, text='user files', reply_markup=inline_comand('user'))
    except: bot.send_message(message.chat.id, mes_txt('error1'))

def a_mesuser(message):
    try:
        file = f'dok/mes_user'

        open_file = open(file, 'r')
        text = open_file.read()
        open_file.close()
        bot.send_message(message.chat.id, text=text)
    except: bot.send_message(message.chat.id, mes_txt('error1'))

def a_staruser(message):
    try:
        file = f'dok/star_user'

        open_file = open(file, 'r')
        text = open_file.read()
        open_file.close()
        bot.send_message(message.chat.id, text=text)
    except: bot.send_message(message.chat.id, mes_txt('error1'))

def a_error(message):
    try:
        file = f'dok/error'

        open_file = open(file, 'r')
        text = open_file.read()
        open_file.close()
        bot.send_message(message.chat.id, text=text)
    except: bot.send_message(message.chat.id, mes_txt('error1'))

def a_msuser(message):
    try:
        file = 'xyz/ms.txt'

        open_file = open(file, 'r')
        text = open_file.read()
        open_file.close()
        bot.send_message(message.chat.id, text=text)

    except: bot.send_message(message.chat.id, mes_txt('error1'))

def a_mes(message):
    try:
        my_file = open('dok/mes_user', 'r')
        id_user = (my_file.read()).split(';')

        for i in range(len(id_user) - 1):
            bot.send_message(id_user[i], text=message)
    except: bot.send_message(message.chat.id, mes_txt('error1'))

@bot.message_handler(commands = ['Bot', 'bot'])
def c_user(message):
    if str(message.chat.id) == adm: a_bot(message)
    else: pass

@bot.message_handler(commands = ['Mes', 'mes'])
def c_mes(message):
    if str(message.chat.id) == adm: a_mes((message.text)[4:])
    else: pass
########################################################################################################################
@bot.message_handler(commands=['Wacker', 'wacker'])
def c_wacker(message):
    bot.send_message(message.from_user.id, f'{message.text} - {mes_txt("wac1")}')
    bot.register_next_step_handler(bot.send_message(message.chat.id, mes_txt('locat')), a_location)

def a_location(message): bot.send_location(message.chat.id, (message.text).split()[0], (message.text).split()[1])

@bot.message_handler(commands=['EA', 'ea', 'Ea', 'eA', '234', '11101010'])
def c_ea(message): bot.send_message(message.from_user.id, f'{message.text} - ' + mes_txt('234'))

@bot.message_handler(commands=['101'])
def c_ea(message): bot.send_message(message.from_user.id, mes_txt('101') + f'\n/{message.text}')

@bot.message_handler(commands=['error'])
def error(message): print(e)
########################################################################################################################
@bot.message_handler(content_types=['text'])
def textmessages(message):
    if message.text.lower() == '101': bot.send_message(message.from_user.id, mes_txt('101') + f'\n/{message.text}')

    elif message.text.lower() == keyboard('coding'):
        bot.send_message(message.chat.id, text= mes_txt('coding'), reply_markup=inline_comand('coding'))
        pass
    elif message.text.lower() == keyboard('conversion'):
        bot.send_message(message.chat.id, text= mes_txt('conversion'), reply_markup=inline_comand('conversion'))
        pass
    elif message.text.lower() == keyboard('simplecommands'):
        bot.send_message(message.chat.id, text= mes_txt('simplecommands'), reply_markup=inline_comand('simplecommands'))
        pass
    elif message.text.lower() == keyboard('menu'): a_menu(message)

    elif message.text.lower() == keyboard('about'):
        bot.send_message(message.chat.id, text= mes_txt('about'))
        bot.send_message(message.chat.id, text=mes_txt('links'))

    else:
        bot.send_message(message.chat.id, message.text + mes_txt('mirror'))
##########################################################################################################################
def inline_comand(comand):
    try:
        markup = types.InlineKeyboardMarkup()

        item_innotice = (types.InlineKeyboardButton(text=inline_text('innotice'), callback_data='innotice'))
        item_ofnotice = (types.InlineKeyboardButton(text=inline_text('ofnotice'), callback_data='ofnotice'))

        item_coding = (types.InlineKeyboardButton(text=inline_text('coding'), callback_data='coding'))
        item_conversion = (types.InlineKeyboardButton(text=inline_text('conversion'), callback_data='conversion'))
        item_simplecommands = (types.InlineKeyboardButton(text=inline_text('simplecommands'), callback_data='simplecommands'))
        item_settings = (types.InlineKeyboardButton(text=inline_text('settings'), callback_data='settings'))
        item_gmenu = (types.InlineKeyboardButton(text=inline_text('gmenu'), callback_data='gmenu'))
        item_menu = (types.InlineKeyboardButton(text=inline_text('menu'), callback_data='menu'))

        item_image = (types.InlineKeyboardButton(text=inline_text('image'), callback_data='image'))
        item_caesar = (types.InlineKeyboardButton(text=inline_text('caesar'), callback_data='caesar'))
        item_vigenere = (types.InlineKeyboardButton(text=inline_text('vigenere'), callback_data='vigenere'))

        item_morse = (types.InlineKeyboardButton(text=inline_text('morse'), callback_data='morse'))
        item_transnumb = (types.InlineKeyboardButton(text=inline_text('transn'), callback_data='transn'))
        item_bin = (types.InlineKeyboardButton(text=inline_text('bin'), callback_data='bin'))
        item_url = (types.InlineKeyboardButton(text=inline_text('url'), callback_data='url'))

        item_qr = (types.InlineKeyboardButton(text=inline_text('qr'), callback_data='qr'))
        item_randp = (types.InlineKeyboardButton(text =inline_text('randp'), callback_data='randp'))
        item_dnup = (types.InlineKeyboardButton(text=inline_text('dnup'), callback_data='dnup'))

        item_inimage = (types.InlineKeyboardButton(text=inline_text('inimage'), callback_data='inimage'))
        item_ofimage = (types.InlineKeyboardButton(text=inline_text('ofimage'), callback_data='ofimage'))

        item_invigenere = (types.InlineKeyboardButton(text=inline_text('invigenere'), callback_data='invigenere'))
        item_ofvigenere = (types.InlineKeyboardButton(text=inline_text('ofvigenere'), callback_data='ofvigenere'))

        item_inmorse = (types.InlineKeyboardButton(text=inline_text('inmorse'), callback_data='inmorse'))
        item_ofmorse = (types.InlineKeyboardButton(text=inline_text('ofmorse'), callback_data='ofmorse'))

        item_inbin = (types.InlineKeyboardButton(text=inline_text('inbin'), callback_data='inbin'))
        item_ofbin = (types.InlineKeyboardButton(text=inline_text('ofbin'), callback_data='ofbin'))

        item_inurl = (types.InlineKeyboardButton(text=inline_text('inurl'), callback_data='inurl'))
        item_ofurl = (types.InlineKeyboardButton(text=inline_text('ofurl'), callback_data='ofurl'))

        item_dn = (types.InlineKeyboardButton(text=inline_text('dn'), callback_data='dn'))
        item_up = (types.InlineKeyboardButton(text=inline_text('up'), callback_data='up'))
        item_pund = (types.InlineKeyboardButton(text=inline_text('pund'), callback_data='pund'))

        item_ru = (types.InlineKeyboardButton(text=inline_text('ru'), callback_data='ru'))
        item_en = (types.InlineKeyboardButton(text=inline_text('en'), callback_data='en'))

        item_mesuser = (types.InlineKeyboardButton(text='mes_user', callback_data='mes_user'))
        item_staruser = (types.InlineKeyboardButton(text='star_user', callback_data='star_user'))
        item_error = (types.InlineKeyboardButton(text='error', callback_data='error'))
        item_mesofuser = (types.InlineKeyboardButton(text='ms_user', callback_data='mesofuser'))

        if comand == 'menu':
            markup.add(item_coding)
            markup.add(item_conversion)
            markup.add(item_simplecommands)
            markup.add(item_gmenu, item_settings)
            return markup

        elif comand == 'gmenu':
            markup.add(item_image, item_qr)
            markup.add(item_caesar, item_vigenere)
            markup.add(item_morse, item_transnumb)
            markup.add(item_bin, item_url)
            markup.add(item_randp)
            markup.add(item_menu, item_settings)
            return markup

        elif comand == 'settings':
            markup.add(item_settings, item_menu)
            return markup

        elif comand == 'innotice':
            markup.add(item_innotice, item_menu)
            return markup

        elif comand == 'ofnotice':
            markup.add(item_ofnotice, item_menu)
            return markup

        elif comand == 'coding':
            markup.add(item_image)
            markup.add(item_caesar)
            markup.add(item_vigenere)
            return markup

        elif comand == 'conversion':
            markup.add(item_morse)
            markup.add(item_transnumb)
            markup.add(item_bin)
            markup.add(item_url)
            return markup

        elif comand == 'simplecommands':
            markup.add(item_qr)
            markup.add(item_randp)

            return markup
########################################################################################################################
        elif comand == 'image':
            markup.add(item_inimage, item_ofimage)
            markup.add(item_coding)
            return markup

        elif comand == 'vigenere':
            markup.add(item_invigenere, item_ofvigenere)
            markup.add(item_coding)
            return markup

        elif comand == 'morse':
            markup.add(item_inmorse, item_ofmorse)
            markup.add(item_conversion)
            return markup

        elif comand == 'bin':
            markup.add(item_inbin, item_ofbin)
            markup.add(item_conversion)
            return markup

        elif comand == 'url':
            markup.add(item_inurl, item_ofurl)
            markup.add(item_conversion)
            return markup

        elif comand == 'dnup':
            markup.add(item_dn, item_up)
            markup.add(item_pund)
            markup.add(item_simplecommands)
            return markup
########################################################################################################################
        elif comand == 'ofmorse':
            markup.add(item_ru, item_en)
            markup.add(item_morse)
            return markup

        elif comand == 'caesar':
            item_numb = []
            for i in range(33):
                item_numb.append((types.InlineKeyboardButton(text=str(i), callback_data=str(i))))
            markup.row(item_numb[1], item_numb[2], item_numb[3], item_numb[4], item_numb[5], item_numb[6], item_numb[7], item_numb[8])
            markup.row(item_numb[9], item_numb[10], item_numb[11], item_numb[12], item_numb[13], item_numb[14], item_numb[15], item_numb[16])
            markup.row(item_numb[17], item_numb[18], item_numb[19], item_numb[20], item_numb[21], item_numb[22], item_numb[23], item_numb[24])
            markup.row(item_numb[25], item_numb[26], item_numb[27], item_numb[28], item_numb[29], item_numb[30], item_numb[31], item_numb[32])
            return markup

        elif comand == 'transn1':
            item_numb = []
            for i in range(68):
                item_numb.append((types.InlineKeyboardButton(text=str(i-31), callback_data=str(i))))
            markup.row(item_numb[33], item_numb[34], item_numb[35], item_numb[36], item_numb[37], item_numb[38], item_numb[39], item_numb[40])
            markup.row(item_numb[41], item_numb[42], item_numb[43], item_numb[44], item_numb[45], item_numb[46], item_numb[47], item_numb[48])
            markup.row(item_numb[49], item_numb[50], item_numb[51], item_numb[52], item_numb[53], item_numb[54], item_numb[55], item_numb[56])
            markup.row(item_numb[57], item_numb[58], item_numb[59], item_numb[60], item_numb[61], item_numb[62], item_numb[63], item_numb[64])
            markup.row(item_numb[65], item_numb[66], item_numb[67])
            return markup

        elif comand == 'transn2':
            item_numb = []
            for i in range(104):
                item_numb.append((types.InlineKeyboardButton(text=str(i-67), callback_data=str(i))))
            markup.row(item_numb[69], item_numb[70], item_numb[71], item_numb[72], item_numb[73], item_numb[74], item_numb[75], item_numb[76])
            markup.row(item_numb[77], item_numb[78], item_numb[79], item_numb[80], item_numb[81], item_numb[82], item_numb[83], item_numb[84])
            markup.row(item_numb[85], item_numb[86], item_numb[87], item_numb[88], item_numb[89], item_numb[90], item_numb[91], item_numb[92])
            markup.row(item_numb[93], item_numb[94], item_numb[95], item_numb[96], item_numb[97], item_numb[98], item_numb[99], item_numb[100])
            markup.row(item_numb[101], item_numb[102], item_numb[103])
            return markup

        elif comand == 'user':
            markup.row(item_mesuser)
            markup.row(item_staruser)
            markup.row(item_error)
            markup.row(item_mesofuser)
            return markup

    except: pass
########################################################################################################################
@bot.callback_query_handler(func = lambda call: True)
def inline_comand_in(call):

        bot.answer_callback_query(callback_query_id=call.id, text='')
        answer = ''

        if call.data == 'gmenu':
            markup = inline_comand('gmenu')
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id, text = mes_txt('gmenu'), reply_markup = markup)

        elif call.data == 'menu':
            markup = inline_comand('menu')
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id, text = mes_txt('menu'), reply_markup = markup)

        elif call.data == 'settings':
            a_settings(call.message)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)  # после этого клавиатура исчезает

        elif call.data == 'coding':
            markup = inline_comand('coding')
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id, text = mes_txt('coding'), reply_markup = markup)

        elif call.data == 'conversion':
            markup = inline_comand('conversion')
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id, text = mes_txt('conversion'), reply_markup = markup)

        elif call.data == 'simplecommands':
            markup = inline_comand('simplecommands')
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id, text = mes_txt('simplecommands'), reply_markup = markup)

        elif call.data == 'image':
            markup = inline_comand('image')
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id, text = mes_txt('image'), reply_markup = markup)

        elif call.data == 'vigenere':
            markup = inline_comand('vigenere')
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id, text = mes_txt('vigenere'), reply_markup = markup)

        elif call.data == 'bin':
            markup = inline_comand('bin')
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id, text = mes_txt('bin'), reply_markup = markup)

        elif call.data == 'url':
            markup = inline_comand('url')
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id, text = mes_txt('url'), reply_markup = markup)

        elif call.data == 'morse':
            markup = inline_comand('morse')
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id, text = mes_txt('morse'), reply_markup = markup)

        elif call.data == 'ofmorse':
            markup = inline_comand('ofmorse')
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id, text = mes_txt('ofmorse'), reply_markup = markup)

        elif call.data == 'transn':
            markup = inline_comand('transn1')
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id, text = f'__ -> __', reply_markup = markup)

        elif call.data == 'transn2':
            markup = inline_comand('transn2')
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id, text = f'__ -> __', reply_markup = markup)
########################################################################################################################
        elif call.data == 'innotice':
            a_innotice(call.message)

            markup = inline_comand('ofnotice')
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id, text=mes_txt('ofnotice'), reply_markup=markup)

        elif call.data == 'ofnotice':
            a_ofnotice(call.message)

            markup = inline_comand('innotice')
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id, text=mes_txt('innotice'), reply_markup=markup)
########################################################################################################################
        elif call.data == 'inimage':
            a_inimage(call.message)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)  # после этого клавиатура исчезает

        elif call.data == 'ofimage':
            a_ofimage(call.message)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

        elif call.data == 'caesar':
            print(1)
            a_caesar(call.message)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

        elif call.data == 'invigenere':
            a_invigenere(call.message)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

        elif call.data == 'ofvigenere':
            a_ofvigenere(call.message)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

        elif call.data == 'inmorse':
            a_inmorse(call.message)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

        elif call.data == 'ru':
            a_ofmorse(call.message, call.data)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

        elif call.data == 'en':
            a_ofmorse(call.message, call.data)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

        elif call.data == 'inbin':
            a_inbin(call.message)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

        elif call.data == 'ofbin':
            a_ofbin(call.message)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

        elif call.data == 'inurl':
            a_inurl(call.message)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

        elif call.data == 'ofurl':
            a_ofurl(call.message)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

        elif call.data == 'qr':
            a_qr(call.message)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

        elif call.data == 'randp':
            a_randp(call.message)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

        elif call.data == 'dnup':
            a_dnup(call.message)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)


        elif call.data == 'dn':
            a_dn(call.message)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

        elif call.data == 'up':
            a_up(call.message)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

        elif call.data == 'pund':
            a_pund(call.message)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
########################################################################################################################
        elif call.data == '1' or call.data == '2' or call.data == '3' or call.data == '4' or call.data == '5' or \
                call.data == '6' or call.data == '7' or call.data == '8' or call.data == '9' or call.data == '10' or \
                call.data == '11' or call.data == '12' or call.data == '13' or call.data == '14' or call.data == '15' or \
                call.data == '16' or call.data == '17' or call.data == '18' or call.data == '19' or call.data == '20' or \
                call.data == '21' or call.data == '22' or call.data == '23' or call.data == '24' or call.data == '25' or \
                call.data == '26' or call.data == '27' or call.data == '28' or call.data == '29' or call.data == '30' or\
                call.data == '31' or call.data == '32':
            c_caesar(call.message, call.data)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

        elif call.data == '33' or call.data == '34' or call.data == '35' or call.data == '36' or call.data == '37' or \
                call.data == '38' or call.data == '39' or call.data == '40' or call.data == '41' or call.data == '42' or \
                call.data == '43' or call.data == '44' or call.data == '45' or call.data == '46' or call.data == '47' or \
                call.data == '48' or call.data == '49' or call.data == '50' or call.data == '51' or call.data == '52' or \
                call.data == '53' or call.data == '54' or call.data == '55' or call.data == '56' or call.data == '57' or \
                call.data == '58' or call.data == '59' or call.data == '60' or call.data == '61' or call.data == '62' or \
                call.data == '63' or call.data == '64' or call.data == '65' or call.data == '66' or call.data == '67':

            n = int(call.data) - 31
            file = f'{call.message.chat.id}'

            open_file = open(file, 'w')
            open_file.write(f'{n};')
            open_file.close()


            markup = inline_comand('transn2')
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id, text=f'{mes_txt("transn2")}\n\n{n} -> __', reply_markup=markup)

        elif call.data == '69' or call.data == '70' or call.data == '71' or call.data == '72' or call.data == '73' or \
                call.data == '74' or call.data == '75' or call.data == '76' or call.data == '77' or call.data == '78' or \
                call.data == '79' or call.data == '80' or call.data == '81' or call.data == '82' or call.data == '83' or \
                call.data == '84' or call.data == '85' or call.data == '86' or call.data == '87' or call.data == '88' or \
                call.data == '89' or call.data == '90' or call.data == '91' or call.data == '92' or call.data == '93' or \
                call.data == '94' or call.data == '95' or call.data == '96' or call.data == '97' or call.data == '98' or \
                call.data == '99' or call.data == '100' or call.data == '101' or call.data == '102' or call.data == '103':

            k = int(call.data) - 67
            file = f'{call.message.chat.id}'

            open_file = open(file, 'a')
            open_file.write(f'{k};')
            open_file.close()

            a_transn(call.message)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

        elif call.data == 'mes_user':
            a_mesuser(call.message)

        elif call.data == 'star_user':
            a_staruser(call.message)

        elif call.data == 'error':
            a_error(call.message)

        elif call.data == 'mesofuser':
            a_msuser(call.message)

########################################################################################################################
bot.polling(none_stop=True)