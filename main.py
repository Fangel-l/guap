from init import *
from command import *
from timetable import *
import datetime

WEEKDAY = {"0": "Понедельник"}
today = datetime.datetime.today()
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")

@bot.message_handler(content_types=["text"])
def raspr(message):
    global today, day, month, year
    if message.text[:2].lower() == "!р":
        try:
            message_n = message.text.split()[1].split(".")
            day = message_n[0]
            month = message_n[1]
            year = message_n[2] 
            if str(day)[0] == "0":
                day = int(str(day)[1])

            if str(month)[0] == "0":
                month = int(str(month)[1])

            if len(str(year)) == 2:
                year = int("20" + str(year))
            try:
                datetime.datetime(int(year), int(month), int(day))
            except Exception:
                bot.reply_to(message, "Неверная дата")
            
            timetable = table_everyday(int(day), int(month), int(year))

            timetable_message = ""
            for i in range(len(timetable)):
                if i == 0:
                    timetable_message += timetable[0] + "\n"
                elif timetable[i] == "▲" or timetable[i] == "▼":
                    pass
                elif "пара" in timetable[i]:
                    timetable_message +=  "\n" + "\n" + timetable[i] + "\n" + "<i>" + "<u>"
                elif "пара" in timetable[i-1] or timetable[i-1] == "▲" or timetable[i-1] == "▼":
                    timetable_message +=  timetable[i] + "</u>" + "</i>"  + " " 
                elif "-" in timetable[i] and timetable[i][:timetable[i].index("-")].isdigit() and timetable[i][timetable[i].index("-") + 1:].isdigit():
                    timetable_message += "\n" + "(" + timetable[i] + " "
                elif timetable[i] in ("Гаста", "Ленса", "Бм"):
                    timetable_message += "<b>" + timetable[i] + "</b>)" + " "
                else:
                    timetable_message += "<b>" + timetable[i] + "</b>" + " " 
            bot.reply_to(message, timetable_message, parse_mode="HTML")
            
        except Exception:
            try:
                if message.text.split()[1].lower() == "завтра": 
                    today = datetime.date.today()
                    tz_string = str(datetime.datetime.now().astimezone().tzinfo)
                    if tz_string != "+03":
                        if tz_string[1] == "-":
                            today = datetime.datetime.now() + datetime.timedelta(hours=3 + int(tz_string[1:]))
                        elif tz_string[1] == "+":
                            today = datetime.datetime.now() - datetime.timedelta(hours=(int(tz_string[3:]) - 3))
                        else:
                            today = datetime.date.today()

                    else:
                        today = datetime.date.today()

                    tomorrow = today + datetime.timedelta(days=1)
                    day = int(tomorrow.strftime('%d'))
                    month = int(tomorrow.strftime('%m'))
                    year = int(tomorrow.strftime('%y'))

                elif message.text.split()[1].lower() == "сегодня":
                    today = datetime.date.today()
                    tz_string = str(datetime.datetime.now().astimezone().tzinfo)
                    if tz_string != "+03":
                        if tz_string[1] == "-":
                            today = datetime.datetime.now() + datetime.timedelta(hours=3 + int(tz_string[1:]))
                        elif tz_string[1] == "+":
                            today = datetime.datetime.now() - datetime.timedelta(hours=(int(tz_string[3:]) - 3))
                        else:
                            today = datetime.date.today()


                    else:
                        today = datetime.date.today()

                    day = int(today.strftime('%d'))
                    month = int(today.strftime('%m'))
                    year = int(today.strftime('%y'))

                
                elif message.text.split()[1].lower() == "вчера":
                    today = datetime.date.today()
                    tz_string = str(datetime.datetime.now().astimezone().tzinfo)
                    if tz_string != "+03":
                        if tz_string[1] == "-":
                            today = datetime.datetime.now() + datetime.timedelta(hours=3 + int(tz_string[1:]))
                        elif tz_string[1] == "+":
                            today = datetime.datetime.now() - datetime.timedelta(hours=(int(tz_string[3:]) - 3))
                        else:
                            today = datetime.date.today()
                    else:
                        today = datetime.date.today()

                    yesterday = today - datetime.timedelta(days=1)
                    day = int(yesterday.strftime('%d'))
                    month = int(yesterday.strftime('%m'))
                    year = int(yesterday.strftime('%y'))

                elif message.text.split()[1].capitalize() in WEEK.values():
                    today = datetime.date.today()
                    if WEEK.get(datetime.datetime.today().strftime("%A")) == message.text.split()[1].capitalize():
                        tz_string = str(datetime.datetime.now().astimezone().tzinfo)
                        if tz_string != "+03":
                            if tz_string[1] == "-":
                                today = datetime.datetime.now() + datetime.timedelta(hours=3 + int(tz_string[1:]))
                            elif tz_string[1] == "+":
                                today = datetime.datetime.now() - datetime.timedelta(hours=(int(tz_string[3:]) - 3))
                            else:
                                today = datetime.date.today()
                        else:
                            today = datetime.date.today()

                        day = int(today.strftime('%d'))
                        month = int(today.strftime('%m'))
                        year = int(today.strftime('%y'))
                    else:
                        today = datetime.date.today()
                        tz_string = str(datetime.datetime.now().astimezone().tzinfo)
                        if tz_string != "+03":
                            if tz_string[1] == "-":
                                today = datetime.datetime.now() + datetime.timedelta(hours=3 + int(tz_string[1:]))
                            elif tz_string[1] == "+":
                                today = datetime.datetime.now() - datetime.timedelta(hours=(int(tz_string[3:]) - 3))
                            else:
                                today = datetime.date.today()
                        else:
                            today = datetime.date.today()

                        day = int(today.strftime('%d'))
                        month = int(today.strftime('%m'))
                        year = int(today.strftime('%y'))
                        if len(str(year)) == 2:
                            year = int("20" + str(year))


                        for i in range(1, 8):
                            temp_date_next = (datetime.datetime(year=year, month=month, day=day) + datetime.timedelta(days=i)).strftime("%A")
                            temp_date_old = (datetime.datetime(year=year, month=month, day=day) - datetime.timedelta(days=i)).strftime("%A")
                            if WEEK.get(temp_date_next) == message.text.split()[1].capitalize():
                                day_find = datetime.datetime(year=year, month=month, day=day) + datetime.timedelta(days=i)
                                day = int(day_find.strftime('%d'))
                                month = int(day_find.strftime('%m'))
                                year = int(day_find.strftime('%y'))
                                break
                            elif WEEK.get(temp_date_old) == message.text.split()[1].capitalize():
                                day_find = datetime.datetime(year=year, month=month, day=day) - datetime.timedelta(days=i)
                                day = int(day_find.strftime('%d'))
                                month = int(day_find.strftime('%m'))
                                year = int(day_find.strftime('%y'))
                                break


                timetable = table_everyday(day, month, year)
                timetable_message = ""
                for i in range(len(timetable)):
                    if i == 0:
                        timetable_message += timetable[0] + "\n"
                    elif timetable[i] == "▲" or timetable[i] == "▼":
                        pass
                    elif "пара" in timetable[i]:
                        timetable_message +=  "\n" + "\n" + timetable[i] + "\n" + "<i>" + "<u>"
                    elif "пара" in timetable[i-1] or timetable[i-1] == "▲" or timetable[i-1] == "▼":
                        timetable_message +=  timetable[i] + "</u>" + "</i>"  + " " 
                    elif "-" in timetable[i] and timetable[i][:timetable[i].index("-")].isdigit() and timetable[i][timetable[i].index("-") + 1:].isdigit():
                        timetable_message += "\n" + "(" + timetable[i] + " "
                    elif timetable[i] in ("Гаста", "Ленса", "Бм"):
                        timetable_message += "<b>" + timetable[i] + "</b>)" + " "
                    else:
                        timetable_message += "<b>" + timetable[i] + "</b>" + " " 

                bot.reply_to(message, timetable_message, parse_mode="HTML")

            except Exception        :
                bot.reply_to(message, "неверный ввод")

@bot.message_handler(content_types=["new_chat_members"])
def new_member(message):
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



@bot.message_handler(content_types=['left_chat_member'])
def new_member(message):
    tg_id = message.from_user.id
    name_group = str(message.chat.title).replace(" ", "")
    del_user_db(tg_id, name_group)
        


bot.infinity_polling()
