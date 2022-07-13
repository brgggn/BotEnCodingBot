import glob
import os
import zipfile
import urllib.parse
import random
from qrcode import QRCode
from PIL import Image

#######################################################################################################################
def f_inimage(user_id, text):
    try:
        fimg = f'{user_id}.bmp'

        # создание zip с текстом в папке user_id
        ftxt = f'{user_id}'
        f = open(ftxt, 'w')
        f.write(text)
        f.close()

        fzip = f'{user_id}.zip'
        jungle_zip = zipfile.ZipFile(fzip, 'w')
        jungle_zip.write(f'{user_id}', compress_type=zipfile.ZIP_DEFLATED)

        jungle_zip.close()

        # создание bat файла. совмещение png и zip
        out = open(f"{user_id}new.gif", "wb")
        out.write(open(f"{user_id}.bmp", "rb").read())
        out.write(open(f"{user_id}.zip", "rb").read())
        out.close()

        # удаление файлов
        os.remove(ftxt)
        os.remove(fzip)
        os.remove(fimg)

    except: pass

def f_ofimage(user_id):
    try:
        # перевод из png в zip
        fnpng = f'{user_id}new.gif'
        base = os.path.splitext(fnpng)[0]
        os.rename(fnpng, base + ".zip")

        # распаковка zip
        fzip = f'{user_id}new.zip'
        fantasy_zip = zipfile.ZipFile(fzip)
        fantasy_zip.extractall(user_id)
        fantasy_zip.close()
        # чтение txt из zip

        ftxt = glob.glob(f"{user_id}/*")[0]

        ftxt_open = open(ftxt, 'r')
        text = ftxt_open.read()
        ftxt_open.close()

        # удаление файлов
        os.remove(fzip)
        os.remove(ftxt)
        os.rmdir(user_id)  # удаление папки

        return (text)

    except: pass
########################################################################################################################
def f_caesar(shag, text):
    try:
        shag = int(shag)
        alf =  'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'*2 + 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'.upper()*2 + \
               'abcdefghijklmnopqrstuvwxyz'*3 + 'abcdefghijklmnopqrstuvwxyz'.upper()*3 + '0123456789'*4

        if int(shag) < 0:
            alf = alf[::-1]
            shag *= -1
        caesar = ''
        for i in text:
            numb = alf.find(i)
            new_numb = numb + shag
            if i in alf:
                caesar += alf[new_numb]
            else:
                caesar += i
        return caesar

    except: pass
########################################################################################################################
def f_vigenere(direct, key, text):
    try:
        keykey = ''
        while len(keykey) < len(text):
            keykey += key
        lang = check_lang(key)

        if lang == '0': return 'ошибка'
        else:
            key_numb = []
            for i in range(len(keykey)):
                key_numb.append(serial_number(keykey[i]))
        vigenere = ''
        for i in range(len(text)):
            vigenere += f_caesar(direct + key_numb[i], text[i])
        return vigenere

    except: pass
########################################################################################################################
def f_inmorse(fraza):

    frazaq = ''
    for i in range(len(fraza)):
        lang = check_lang(fraza[i])
        if lang == 'en': frazaq += morse_en(fraza[i]) + ' '
        elif lang == 'ru': frazaq += morse_ru(fraza[i]) + ' '
        elif lang == 'simv': frazaq += morse_ru(fraza[i]) + ' '
        elif lang == 'numb': frazaq += morse_ru(fraza[i]) + ' '
    return frazaq
########################################################################################################################
def f_ofmorse(fraza, lang):
    if check(fraza, '•―/ ') == '0': return 'error'

    frazaq = ''
    fraza = fraza.split(' ')

    if lang == 'ru':
        for i in range(len(fraza)):
            frazaq += morse_ru(fraza[i])

    elif lang == 'en':
        for i in range(len(fraza)):
            frazaq += morse_en(fraza[i])
    return frazaq
########################################################################################################################
"""
def f_trans(n, A, k):
    A.upper()
    abc = '0123456789'+'abcdefghijklmnopqrstuvwxyz'.upper()
    i = 0
    for a in A:
        z = abc.find(a)
        i = i * n + z
    trans = ''
    while(i != 0):
        z = i % k
        trans = abc[z] + trans
        i = i // k
    return trans
"""
def f_trans(n, A, k):
    A = A.upper()
    abc = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    q = 0
    trans_A = 0
    A = A[::-1]
    for i in range(len(A)):
        q = abc.index(A[i])

        trans_A += (n ** i * int(q))

    trans = trans10(trans_A, k)
    return trans

def trans10(A, k):
    abc='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d = int(A)
    trans_A = ''
    while (d*k >= k):
        m = d%k
        d = d//k
        if (m > 9):
            m = abc[m]
        trans_A += str(m)
    trans_A = trans_A[::-1]
    return trans_A
########################################################################################################################
def f_inbin(fraza):
    A = []
    for i in range(len(list(fraza))):
        A = A + list(((list(map(int, (bin(ord(fraza[i]))[2:]).zfill(12))))),)
        i+=1
    A = ''.join(map(str, A))
    return A

def f_ofbin(code):
    ono = '01'
    for i in range(len(str(code))):
        if str(code)[i] not in ono: return 'Ошибка.\nДопускаются только нули и единицы.'
        elif len(code) < 12: return 'Ошибка.\nДлина одного символа составляет 12 едениц.'
        else:
            list(code)
            code = (list(map(int, code)))
            B = tuple()
            for i in range(len(code)//12):
                B = B +((code[:12]),)
                del code[0:12]
            code = B

            fraza_ten = str()
            for i in range(len(code)):
                fraza_ten = fraza_ten + (chr(int(((''.join(map(str, code[i])))), 2)))
                i+=1
            return fraza_ten
########################################################################################################################
def f_inurl(not_url): return (urllib.parse.quote_plus(not_url))
def f_ofurl(url): return (urllib.parse.unquote_plus(url))
########################################################################################################################
def f_qr(data, qr_name):

    qr = QRCode()  # Создаем объект QR-кода
    qr.add_data(data)  # Установить данные QR-кода
    img = qr.make_image()  # Создать изображение QR-кода
    img.save(qr_name)  # Сохранить картинку с QR-кодом
    '''
    myqr.run(
        words=data,  # Содержит информацию
        #picture='lbxx.jpg',  # Фоновое изображение
        colorized=False,  # Есть ли цвет, если False, то он черно-белый
        save_name=qr_name  # Имя выходного файла
    )
    '''
    '''
    img = qrcode.make(data)
    img.save(qr_name)
    return img
    '''

########################################################################################################################
def color(r, g, b, name):
    im = Image.open("xyz/BotEnCoding.png")
    pixels = im.load()

    for i in range(1024):
        for j in range(1024):
            pixels[i, j] = r, g, b

    im.save(name)


########################################################################################################################
def f_randp(m):
    alph = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k m n p q r s t u v w x y z'.split()
    res = ''
    for x in range(m):
        res += alph[random.randint(0,(len(alph)) - 1)]
    return res
########################################################################################################################
# прочитать в обратном порядке
def f_pund(text): return text[::-1]

# поднять все символы строки
def f_up(text): return text.upper()

# опустить все сиволы строки
def f_dn(text): return text.lower()
########################################################################################################################
def check_lang(abc):
    if check(abc, 'abcdefghijklmnopqrstuvwxyz ' + 'abcdefghijklmnopqrstuvwxyz '.upper()) != '0': return 'en'
    elif check(abc, 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя ' + 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '.upper()) != '0': return 'ru'
    elif check(abc, 'abcdefghijklmnopqrstuvwxyz ' + 'abcdefghijklmnopqrstuvwxyz '.upper() +
                        'абвгдеёжзийклмнопрстуфхцчшщъыьэюя ' + 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '.upper()) != '0': return 'enru'
    elif check(abc, '0123456789 '): return 'numb'
    elif check(abc, '.,;:?!-"(/) '): return 'simv'
    else: return '0'

def check(value, alf):
    for i in range(len(str(value))):
        if str(value)[i] not in alf: return '0'
    else: return (value)

def serial_number(mean):
    serial_number = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9',
                    'j': '10',
                    'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19',
                    't': '20',
                    'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26',

                    'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5', 'F': '6', 'G': '7', 'H': '8', 'I': '9',
                    'J': '10',
                    'K': '11', 'L': '12', 'M': '13', 'N': '14', 'O': '15', 'P': '16', 'Q': '17', 'R': '18', 'S': '19',
                    'T': '20',
                    'U': '21', 'V': '22', 'W': '23', 'X': '24', 'Y': '25', 'Z': '26',

                    'а': '1', 'б': '2', 'в': '3', 'г': '4', 'д': '5', 'е': '6', 'ё': '7', 'ж': '8', 'з': '9',
                    'и': '10',
                    'й': '11', 'к': '12', 'л': '13', 'м': '14', 'н': '15', 'о': '16', 'п': '17', 'р': '18', 'с': '19',
                    'т': '20',
                    'у': '21', 'ф': '22', 'х': '23', 'ц': '24', 'ч': '25', 'ш': '26', 'щ': '27', 'ъ': '28', 'ы': '29',
                    'ь': '30',
                    'э': '31', 'ю': '32', 'я': '33',

                    'А': '1', 'Б': '2', 'В': '3', 'Г': '4', 'Д': '5', 'Е': '6', 'Ё': '7', 'Ж': '8', 'З': '9',
                    'И': '10',
                    'Й': '11', 'К': '12', 'Л': '13', 'М': '14', 'Н': '15', 'О': '16', 'П': '17', 'Р': '18', 'С': '19',
                    'Т': '20',
                    'У': '21', 'Ф': '22', 'Х': '23', 'Ц': '24', 'Ч': '25', 'Ш': '26', 'Щ': '27', 'Ъ': '28', 'Ы': '29',
                    'Ь': '30',
                    'Э': '31', 'Ю': '32', 'Я': '33',

                    '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '0': '0'
                    }
    return serial_number.get(mean)

def morse_ru(text):
    morse_ru =  {'а': '•―', 'б': '―•••', 'в': '•――', 'г': '――•', 'д': '―••', 'е': '•', 'ё': '•','ж': '•••―', 'з': '――••',
            'и': '••', 'й': '•―――', 'к': '―•―', 'л': '•―••', 'м': '――', 'н': '―•', 'о': '―――', 'п': '•――•',
            'р': '•―•', 'с': '•••', 'т': '―', 'у': '••―', 'ф': '••―•', 'х': '••••', 'ц': '―•―•', 'ч': '―――•',
            'ш': '――――', 'щ': '――•―', 'ъ': '•――•―•', 'ы': '―•――', 'ь': '―••―', 'э': '••―••', 'ю': '••――',
            'я': '•―•―', 'А': '•―', 'Б': '―•••', 'В': '•――', 'Г': '――•', 'Д': '―••', 'Е': '•', 'Ё': '•', 'Ж': '•••―',
            'З': '――••', 'И': '••', 'Й': '•―――', 'К': '―•―', 'Л': '•―••', 'М': '――', 'Н': '―•', 'О': '―――',
            'П': '•――•', 'Р': '•―•', 'С': '•••', 'Т': '―', 'У': '••―', 'Ф': '••―•', 'Х': '••••', 'Ц': '―•―•',
            'Ч': '―――•', 'Ш': '――――', 'Щ': '――•―', 'Ъ': '•――•―•', 'Ы': '―•――', 'Ь': '―••―', 'Э': '••―••',
            'Ю': '••――', 'Я': '•―•―',

            '•―': 'а', '―•••': 'б', '•――': 'в', '――•': 'г', '―••': 'д', '•': 'е', '•••―': 'ж', '――••': 'з',
            '••': 'и', '•―――': 'й', '―•―': 'к', '•―••': 'л', '――': 'м', '―•': 'н', '―――': 'о', '•――•': 'п',
            '•―•': 'р', '•••': 'с', '―': 'т', '••―': 'у', '••―•': 'ф', '••••': 'х', '―•―•': 'ц', '―――•': 'ч',
            '――――': 'ш', '――•―': 'щ', '•――•―•': 'ъ', '―•――': 'ы', '―••―': 'ь', '••―••': 'э', '••――': 'ю', '•―•―': 'я',

            ' ': '/', '0': '―――――', '1': '•――――', '2': '••―――',
            '3': '•••――', '4': '••••―', '5': '•••••', '6': '―••••', '7': '――•••', '8': '―――••', '9': '――――•',
            '.': '••••••', ',': '•―•―•―', ';': '―•―•―•', ':': '―――•••', '?': '••――••', '!': '――••――',
            '-': '―••••―', '"': '•―••―•', ')(': '―•――•―',  '(': '―•――•―', ')': '―•――•―',


            '/': ' ', '―――――': '0', '•――――': '1', '••―――': '2', '•••――': '3', '••••―': '4', '•••••': '5',
            '―••••': '6', '――•••': '7', '―――••': '8', '――――•': '9',
            '••••••': '.', '•―•―•―': ',', '―•―•―•': ';', '―――•••': ':', '••――••': '?', '――••――': '!',
            '―••••―': '-', '•―••―•': '"', '―•――•―': ')(', '―••―•': '/'
            }
    return morse_ru.get(text)
#
def morse_en(text):
    morse_en =  {'a': '•―', 'b': '―•••', 'c': '―•―•', 'd': '―••', 'e': '•', 'f': '••―•', 'g': '――•', 'h': '••••',
            'i': '••', 'j': '•―――', 'k': '―•―', 'l': '•―••', 'm': '――', 'n': '―•', 'o': '―――', 'p': '•――•',
            'q': '――•―', 'r': '•―•', 's': '•••', 't': '―', 'u': '••―', 'v': '•••―', 'w': '•――', 'x': '―••―',
            'y': '―•――', 'z': '――••', 'A': '•―', 'B': '―•••', 'C': '―•―•', 'D': '―••', 'E': '•', 'F': '••―•',
            'G': '――•', 'H': '••••', 'I': '••', 'J': '•―――', 'K': '―•―', 'L': '•―••', 'M': '――', 'N': '―•',
            'O': '―――', 'P': '•――•', 'Q': '――•―', 'R': '•―•', 'S': '•••', 'T': '―', 'U': '••―', 'V': '•••―',
            'W': '•――', 'X': '―••―', 'Y': '―•――', 'Z': '――••',

            '•―': 'a', '―•••': 'b', '―•―•': 'c', '―••': 'd', '•': 'e', '••―•': 'f', '――•': 'g', '••••': 'h',
            '••': 'i', '•―――': 'j', '―•―': 'k', '•―••': 'l', '――': 'm', '―•': 'n', '―――': 'o', '•――•': 'p',
            '――•―': 'q', '•―•': 'r', '•••': 's', '―': 't', '••―': 'u', '•••―': 'v', '•――': 'w', '―••―': 'x',
            '―•――': 'y', '――••': 'z',

            ' ': '/', '0': '―――――', '1': '•――――', '2': '••―――',
            '3': '•••――', '4': '••••―', '5': '•••••', '6': '―••••', '7': '――•••', '8': '―――••', '9': '――――•',
            '.': '••••••', ',': '•―•―•―', ';': '―•―•―•', ':': '―――•••', '?': '••――••', '!': '――••――',
            '-': '―••••―', '"': '•―••―•', ')(': '―•――•―',  '(': '―•――•―', ')': '―•――•―',


            '/': ' ', '―――――': '0', '•――――': '1', '••―――': '2', '•••――': '3', '••••―': '4', '•••••': '5',
            '―••••': '6', '――•••': '7', '―――••': '8', '――――•': '9',
            '••••••': '.', '•―•―•―': ',', '―•―•―•': ';', '―――•••': ':', '••――••': '?', '――••――': '!',
            '―••••―': '-', '•―••―•': '"', '―•――•―': ')(', '―••―•': '/'}
    return morse_en.get(text)
