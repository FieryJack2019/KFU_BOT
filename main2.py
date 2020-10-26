from selenium import webdriver
import telebot
from telebot import types
from telebot import TeleBot
import pdfkit
import time
bot=telebot.TeleBot('')

yes = types.KeyboardButton('Да')
no = types.KeyboardButton('Нет')

role1 = types.KeyboardButton('Абитуриент')
role2 = types.KeyboardButton('Бакалавр')
role3 = types.KeyboardButton('Магистрант')

abiturient1=types.KeyboardButton('Направления подготовки')
abiturient2=types.KeyboardButton('Подробно о направлениях подготовки (Баллы)')
abiturient3=types.KeyboardButton('Список поданных заявлений')
abiturient4=types.KeyboardButton('Информация для поступивших (Общежитие)')
abiturient5=types.KeyboardButton('Учебные планы')
abiturient6=types.KeyboardButton('До вузовская подготовка')
abiturient7=types.KeyboardButton('Информация об ИВМиИТ')
abiturient8=types.KeyboardButton('Назад')

bacalavr1=types.KeyboardButton('Доступное Расписание')
bacalavr2=types.KeyboardButton('Назад')

magistr1=types.KeyboardButton('Темы научных исследований последних лет')
magistr2=types.KeyboardButton('Назад')

yesno = types.ReplyKeyboardMarkup(True)
abiturients=types.ReplyKeyboardMarkup(True)
bacalavriat=types.ReplyKeyboardMarkup(True)
magistrs=types.ReplyKeyboardMarkup(True)
roles = types.ReplyKeyboardMarkup(True)

yesno.row(yes,no)
abiturients.row(abiturient1)
abiturients.row(abiturient2)
abiturients.row(abiturient3)
abiturients.row(abiturient4)
abiturients.row(abiturient5)
abiturients.row(abiturient6)
abiturients.row(abiturient7)
abiturients.row(abiturient8)
roles.row(role1, role2, role3)
bacalavriat.row(bacalavr1)
bacalavriat.row(bacalavr2)
magistrs.row(magistr1)
magistrs.row(magistr2)

#Реализация функций для абитуриентов!
#Создание пдф файла 
'''config= pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
pdfkit.from_url('https://kpfu.ru/computing-technology/abiturientam/napravleniya-podgotovki','napravl.pdf',configuration=config)
pdfkit.from_url('https://kpfu.ru/computing-technology/abiturientam/dovuzovskaya-podgotovka','dovuzpodgotovka.pdf',configuration=config)
pdfkit.from_url('https://kpfu.ru/computing-technology/abiturientam/informaciya-dlya-postupivshih','infapostupivshim.pdf',configuration=config)
#создал'''

#Основная инфа про кфу, по абзацам для сообщений
f = open('osnovinfa.txt', 'r')
VMKinf=[str(i)for i in f.read().split('\n')]
f.close()
#записал для опр переменной данные, закрыл файл



'''#парсинг направленйи подготовки
a,b,c=[],['0','1','2','3','4','5','6','7','8','9'],[]
driver=webdriver.Chrome('C:/Users/ghali/chromedriver.exe')
driver.get("https://kpfu.ru/computing-technology/abiturientam/abiturientam.html")
infa=driver.find_element_by_class_name('visit_link')
items=infa.find_elements_by_class_name("menu_list")
for item in items:
    text=item.text
    a.append(text)
for i in range(len(a)):
    a[i]=list(a[i])
for i in range(len(a)-2):
    if a[i][0] in b:
        c.append(a[i])
for i in range (len(c)):
    c[i]=''.join(c[i])
f = open('napravl.txt', 'w')
for i in range (len(c)):
    f.write(c[i]+'\n')
f.close()
driver.quit()

#парсинг ссылок на презентации направлений
driver=webdriver.Chrome('C:/Users/ghali/chromedriver.exe')
driver.get("https://kpfu.ru/computing-technology/abiturientam/abiturientam.html")
f = open('napravl.txt', 'r')
napr,ssilki=[str(i)for i in f.read().split('\n')],[]
for i in range(len(napr)-1):
    href=driver.find_element_by_link_text(napr[i]).get_attribute("href")
    ssilki.append(href)
for i in range(len(napr)-1):
    napr[i]+='\nКраткая информация о направлении:\n'+ssilki[i]

#Беру ссылки из бокового меню кнопок для заявок и учеб плана
zayavki=driver.find_element_by_link_text('Список поданных заявлений').get_attribute("href")
uchplan=driver.find_element_by_link_text('Учебные планы').get_attribute("href")
driver.quit()
#Завершине парсинга
#Все Реализованные функции для абитуриентов!


#Реализация Функций для бакалавриата!
#parsing raspisaniya
driver=webdriver.Chrome('C:/Users/ghali/chromedriver.exe')
driver.get("https://kpfu.ru/computing-technology")
spisok,raspisanie,ssilkiekz=[],[],[]
infa=driver.find_element_by_class_name('visit_link')
items=infa.find_elements_by_class_name("menu_list")
for item in items:
    text=item.text
    spisok.append(text)
for i in range (len(spisok)):
    spisok[i]=spisok[i].split()
for i in range (len(spisok)):
    if 'Расписание' in spisok[i]:
        raspisanie.append(spisok[i])
for i in range (len(raspisanie)):
    raspisanie[i]=' '.join(raspisanie[i])
for i in range(len(raspisanie)):
    href=driver.find_element_by_link_text(raspisanie[i]).get_attribute("href")
    ssilkiekz.append(href)
for i in range(len(ssilkiekz)):
    raspisanie[i]=raspisanie[i]+'\n'+ssilkiekz[i]
driver.quit()
#Спарсили доступное рассписание и ссылки на них (соеденили в ласт цикле)
#Все Реализованные функции для Бакалвриата!


#Реализация Функций для бакалавриата!
#Парсинг Тем научных исследований для студентов магистратуры
a,c,f,ms=[],[],[],[]
driver=webdriver.Chrome('C:/Users/ghali/chromedriver.exe')
driver.get("https://kpfu.ru/computing-technology/master")
infa=driver.find_element_by_class_name('visit_link')
items=infa.find_elements_by_class_name("li_spec")
for item in items:
    text=item.text
    a.append(text)
for i in range (len(a)):
    a[i]=a[i].split()
for i in range (len(a)):
    if 'Кафедра' in a[i][0]:
        c.append(a[i])
for i in range (len(c)):
    c[i]=' '.join(c[i])
    
for i in range (len(c)):
    f.append(driver.find_element_by_link_text(c[i]).get_attribute("href"))
for i in range(len(f)):
    ms.append(c[i]+'\n'+f[i])
driver.quit()
#Спарсили темы в magan(название,\n,ссылка)'''

@bot.message_handler(commands=['start'])
def start(message):
    if message.text=='/start':
            bot.send_sticker(message.from_user.id,'CAADAgADRzYAAmOLRgzs4VDLw9luYRYE' )
            bot.send_message(message.from_user.id,'Привет!\nЯ ИВМиИТ БОТ, надеюсь я смогу тебе чем нибудь помочь!\nВыбери свою роль?', reply_markup=roles )
            bot.register_next_step_handler(message,get_name)
    else:
        bot.send_message(message.from_user.id,"Напиши /start")


        
@bot.message_handler(content_types=['text'])
def get_name(message):
    name=message.text.lower()
    if name=='абитуриент':
        bot.send_sticker(message.chat.id,'CAADAgADczYAAmOLRgzFSAUXM5PFfBYE')
        bot.send_message(message.from_user.id,'Окей. Я помогу тебе. Выбери то, что тебе нужно',reply_markup=abiturients)
        bot.register_next_step_handler(message,abitur)
    elif name=='бакалавр':
        bot.send_sticker(message.chat.id,'CAADAgADczYAAmOLRgzFSAUXM5PFfBYE')
        bot.send_message(message.from_user.id,'Окей. Я помогу тебе. Выбери то, что тебе нужно',reply_markup=bacalavriat)
        bot.register_next_step_handler(message,bacalavr)
    elif name=='магистрант':
        bot.send_sticker(message.chat.id,'CAADAgADczYAAmOLRgzFSAUXM5PFfBYE')
        bot.send_message(message.from_user.id,'Окей. Я помогу тебе. Выбери то, что тебе нужно',reply_markup=magistrs)
        bot.register_next_step_handler(message,magistr)
    else:
        bot.send_message(message.from_user.id,"Напиши /start")
        
def magistr(message):
    name=message.text.lower()
    if name == 'темы научных исследований последних лет':
        bot.send_sticker(message.chat.id,'CAADAgADczYAAmOLRgzFSAUXM5PFfBYE')
        bot.send_message(message.from_user.id,'Вот все темы, которые я смог найти на сайте!')
        for i in range(len(ms)):
            bot.send_message(message.from_user.id,ms[i])
        bot.send_message(message.from_user.id,'Могу я еще тебе помочь?',reply_markup=yesno)
        bot.register_next_step_handler(message,napap)
    elif name =='назад':
        bot.send_sticker(message.chat.id,'CAADAgADczYAAmOLRgzFSAUXM5PFfBYE',reply_markup=roles)
        bot.register_next_step_handler(message,get_name)
    else:
        bot.send_message(message.from_user.id,"Я тебя не понял. Напиши /start")

def bacalavr(message):
    name=message.text.lower()
    if name == 'доступное расписание':
        bot.send_message(message.from_user.id,'На данный момент, на сайте ИВМиИТ есть следующая информация:')
        for i in range(len(raspisanie)):
            bot.send_message(message.from_user.id,raspisanie[i])   
        bot.send_message(message.from_user.id,'Могу я еще тебе помочь?',reply_markup=yesno)
        bot.register_next_step_handler(message,napap)
    elif name =='назад':
        bot.send_sticker(message.chat.id,'CAADAgADczYAAmOLRgzFSAUXM5PFfBYE',reply_markup=roles)
        bot.register_next_step_handler(message,get_name)
    else:
        bot.send_message(message.from_user.id,"Я тебя не понял. Напиши /start")
                       
def abitur(message):
    name=message.text.lower()
    if name == 'направления подготовки':
        bot.send_message(message.from_user.id,'На данный момент, у ИВМиИТ есть следующие направления:')
        for i in range(len(napr)-1):
            bot.send_message(message.from_user.id,napr[i])
        bot.send_message(message.from_user.id,'Могу я еще тебе помочь?',reply_markup=yesno)
        bot.register_next_step_handler(message,napap)
    elif name == 'информация об ивмиит':
        bot.send_message(message.from_user.id,'Вот краткая информация об ИВМиИТ')
        for i in range (len(VMKinf)):
            bot.send_message(message.from_user.id,VMKinf[i])
        bot.send_message(message.from_user.id,'Могу я еще тебе помочь?',reply_markup=yesno)
        bot.register_next_step_handler(message,napap)
    elif name == 'подробно о направлениях подготовки (баллы)':
        bot.send_message(message.from_user.id,'Вот вся информация о направлениях подготовки которая есть на сайте:')
        bot.send_document(message.chat.id,open('napravl.pdf','rb'))
        bot.send_message(message.from_user.id,'Кстати, держу в курсе, pdf рабочий!\nТо есть, все кнопки в нем рабочие!\nТы можешь нажать на интересующую тебя кнопку, и она перекинет тебя на оффицальный сайт с нужной информацией :)')
        bot.send_message(message.from_user.id,'Могу я еще тебе помочь?',reply_markup=yesno)
        bot.register_next_step_handler(message,napap)
    elif name == 'список поданных заявлений':
        bot.send_message(message.from_user.id,'Сейчас я скину тебе ссылку, просто выбери необходимые критерии поиска.')
        bot.send_message(message.from_user.id,zayavki)
        bot.send_message(message.from_user.id,'Могу я еще тебе помочь?',reply_markup=yesno)
        bot.register_next_step_handler(message,napap)
    elif name == 'учебные планы':
        bot.send_message(message.from_user.id,'Сейчас я скину тебе ссылку, просто выбери необходимые критерии поиска.')
        bot.send_message(message.from_user.id,uchplan)
        bot.send_message(message.from_user.id,'Могу я еще тебе помочь?',reply_markup=yesno)
        bot.register_next_step_handler(message,napap)
    elif name =='информация для поступивших (общежитие)':
        bot.send_message(message.from_user.id,'Вот вся информация для поступивших, которую мне удалось найти:')
        bot.send_document(message.chat.id,open('infapostupivshim.pdf','rb'))
        bot.send_message(message.from_user.id,'Кстати, держу в курсе, pdf рабочий!\nТо есть, все кнопки в нем рабочие!\nТы можешь нажать на интересующую тебя кнопку, и она перекинет тебя на оффицальный сайт с нужной информацией :)')
        bot.send_message(message.from_user.id,'Могу я еще тебе помочь?',reply_markup=yesno)
        bot.register_next_step_handler(message,napap)
    elif name =='до вузовская подготовка':
        bot.send_message(message.from_user.id,'Вот вся информация о довузовской подготовке, которую мне удалось найти:')
        bot.send_document(message.chat.id,open('dovuzpodgotovka.pdf','rb'))
        bot.send_message(message.from_user.id,'Кстати, держу в курсе, pdf рабочий!\nТо есть, все кнопки в нем рабочие!\nТы можешь нажать на интересующую тебя кнопку, и она перекинет тебя на оффицальный сайт с нужной информацией :)')
        bot.send_message(message.from_user.id,'Могу я еще тебе помочь?',reply_markup=yesno)
        bot.register_next_step_handler(message,napap)
    elif name =='назад':
        bot.send_sticker(message.chat.id,'CAADAgADczYAAmOLRgzFSAUXM5PFfBYE',reply_markup=roles)
        bot.register_next_step_handler(message,get_name)
    else:
        bot.send_message(message.from_user.id,"Я тебя не понял. Напиши /start")


def napap(message):
    name=message.text.lower()
    if name == 'да':  
        bot.send_message(message.from_user.id,'Тогда, пожалуйста выбери свою роль еще раз.',reply_markup=roles)
        bot.register_next_step_handler(message,get_name)
    elif name == 'нет':
        bot.send_message(message.from_user.id,'Спасибо, что пользуешься мной!\nНапиши /start когда я буду тебе нужен!')
        bot.register_next_step_handler(message,start)

bot.polling(none_stop=True)