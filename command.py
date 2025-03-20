from init import *
from db_request import *
from session_raspr import *

@bot.message_handler(commands=["start"])
def command_start(message):
    user_name = message.from_user.first_name
    tg_id = message.from_user.id
    nikname = message.from_user.username
    ret_list = [0, user_name, tg_id, str(nikname)]
    if str(message.chat.title) != "None":
        name_group = str(message.chat.title).replace(" ", "")
        add_db(ret_list, name_group)
        if str(nikname) == "None":
            bot.send_message(message.chat.id, f"Спасибо, [{user_name}](tg://user?id={tg_id}), ваши данные добавлены", parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, f"Спасибо, @{nikname}, ваши данные добавлены")

    else:
        bot.send_message(message.chat.id, "Добавьте бота в группу в которой хотите его использовать, а затем в этой группе введите команду старт.")

@bot.message_handler(commands=["all"])
def command_all(message):
    name_group = str(message.chat.title).replace(" ", "")
    all_users = db_get(name_group)
    str_all_users_nik = ""
    str_all_users_id = ""
    for i in range(len(all_users)):
        if str(all_users[i][-1]) != "None":
            if str(message.from_user.username) != str(all_users[i][-1]): 
                str_all_users_nik +=f"@{all_users[i][-1]} " 
        else:
            if str(message.from_user.id) != str(all_users[i][1]): 
                str_all_users_id += f"[{all_users[i][0]}](tg://user?id={all_users[i][1]}) "
    if len(str_all_users_nik) != 0:
        lis_all_users_nik = str_all_users_nik.split()
        str_all_users_nik_sec = ""
        for i in range(len(lis_all_users_nik)):
            str_all_users_nik_sec += lis_all_users_nik[i] + "\n"
            if str_all_users_nik_sec.count("@") == 5:
                bot.send_message(message.chat.id, str_all_users_nik_sec)
                str_all_users_nik_sec = ""

        if str_all_users_nik_sec != "":
            bot.send_message(message.chat.id, str_all_users_nik_sec)

    if len(str_all_users_id) != 0:
        lis_all_users_id = str_all_users_id.split()
        str_all_users_id_sec = ""
        for i in range(len(lis_all_users_id)):
            str_all_users_id_sec += lis_all_users_id[i] + "\n"
            if str_all_users_id_sec.count("@") == 5:
                bot.send_message(message.chat.id, str_all_users_id_sec)
                str_all_users_id_sec = ""

        if str_all_users_id_sec != "":
            bot.send_message(message.chat.id, str_all_users_id_sec, parse_mode="Markdown")

@bot.message_handler(commands=["update"])
def command_update(message):
    if str(message.chat.title) != "None":
        name_group = str(message.chat.title).replace(" ", "")
        update_username(name_group, str(message.from_user.username), str(message.from_user.id))
        bot.reply_to(message, "Ваши данные обновлены")
    else:
        bot.send_message(message.chat.id, "Эту функцию можно использовать только в группе")
    
@bot.message_handler(commands=["help"])
def command_help(message):
    bot.reply_to(message, """Этот бот предназначен для вывода рассписания, а так же является альтернативой функции all.

Чтобы пользоваться функцией all, нужно чтоб 
ВСЕ(СУКА БЛЯТЬ ВСЕ НАХУЙ КАЖДЫЙ БЛЯТЬ ДО ЕДИНОГО) написали /start в чат группы.Это надо для того чтобы бот занес ваш айдишник в телеге в свою базу и потом отмечал вас

Команда /update предназначена для того чтобы бот мог всех отмечать. ЕСЛИ вы изменили свой никнейм, то напишите эту команду, чтоб бот обновил свою базу данных.
                 

Чтобы пользоваться рассписанием надо ввести 
!р и написать либо дату в формате(дд.мм.гг) либо написать сегодня или завтра. 
!р это скоращение от рассписание. оно пишется с маленькой буквы на РУССКОМ языке.


ОБНОВЛЕНИЕ!!!!!
Появилась команда /exam кооторая выдает рассписание экзаменов

Убедительная просьба стараться не ломать бота, отправляя то на что он не расчитан.(Если у меня будет время и я захочу найти баги в боте, то я обязательно попрошу вас потестить)
                     """)

@bot.message_handler(commands=["exam"])
def command_C(message):
    return_message = ""
    exam = session_rasp()
    temp_flag = False
    for i in range(len(exam)):
        if i == 0:
            return_message += "<b>" + "<i>" + exam[i] + "</i>" + "</b>" + "\n" + "\n"
            temp_flag = True

        elif i == 1:
            return_message += exam[i] + " "
        elif temp_flag == True and "(" in exam[i]:
            return_message += exam[i] + "</i>" + "\n"

        elif exam[i] in ("Гаста", "Ленса", "БМ"):
            return_message += "(" + exam[i] + " "

        elif exam[i-1] in ("Гаста", "Ленса", "БМ"):
            return_message += exam[i] + ")" + "\n" + "<i>"

        elif len(exam[i]) == 2 and exam[i].isdigit():
            return_message += "</i>" + "\n" + "\n" + exam[i] + " "

        elif len(exam[i-1]) == 2 and exam[i-1].isdigit():
            return_message += exam[i] + " "

        elif len(exam[i-1]) == 1 and exam[i-1].isdigit():
            return_message += exam[i] + " "
        elif temp_flag == True:
            if len(exam[i] )== 1 and exam[i].isdigit():
                return_message += "\t" + "\t" +  "\t" +  "\t" +  "\t" +  "\t" +  "\t" +  "\t" +  "\t" +  "\t" +  "\t" +  "<i>" + exam[i] + " "
            elif len(return_message) != 0 and return_message[-1] == ">":
                return_message += exam[i] + " "
            elif len(exam[i]) == 4 and exam[i].count(".") == 2:
                 return_message += exam[i] + " "
            else:
                return_message += "<b>" + exam[i] + "</b>" + " "

    return_message += "</i>"
    bot.reply_to(message, return_message, parse_mode="HTML")
    