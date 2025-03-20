import datetime as date
from parser import *
WEEK = { "Monday": "Понедельник",
        "Tuesday": "Вторник",
        "Wednesday": "Среда",
        "Thursday": "Четверг",
        "Friday": "Пятница",
        "Saturday": "Суббота",
        "Sunday": "Воскресенье"
}

def table_everyday(day, month, year):
    name_day = date.datetime(year=year, month=month, day=day).strftime("%A")
    name_day = WEEK.get(name_day)
    next_day = date.datetime(year=year, month=month, day=day) + date.timedelta(days=1)
    next_day_name = WEEK.get(next_day.strftime("%A"))
    today = timetable_now_pars(name_day, next_day_name)
    party = party_week_everyday(day, month, year)
    if len(today) == 0:
        return f"пар нет. Отдыхай"
    
    else:
        timetable_today = []
        flag = False
        for i in range(len(today)):
            if len(timetable_today) == 0:
                timetable_today.append(today[i])
            elif today[i] == "▲" or today[i] == "▼":
                if party == today[i]:
                    if "пара" in today[i-1] or "пара" in today[i-1]:
                        timetable_today.append(today[i-1])
                    elif "гр:" in today[i-1]:
                        if len(timetable_today) <= 3:
                            index_couple = 0
                            today_temp_list = today[:i-1]
                            for j in range(len(today_temp_list)):
                                if "пара" in today_temp_list[j]:
                                    index_couple = max(index_couple, j)
                            timetable_today.append(today_temp_list[index_couple])
                        else:
                            today_temp_list = today[today.index(timetable_today[-3]):i-1]
                            for j in range(len(today_temp_list)):
                                if "пара" in today_temp_list[j]:
                                    timetable_today.append(today_temp_list[j])
                            del today_temp_list

                        
                        
            elif "пара" in today[i-1]:
                timetable_today.append(today[i-1])
                        
            elif "пара" in timetable_today[-1]:
                if today[i] != "▲" or today[i] != "▼":
                    timetable_today.append(today[i-1])
                timetable_today.append(today[i])

                flag = True
            
            elif flag == True and "ауд." in today[i]:
                flag = False
                flag_1 = False
                text_append = ""
                for j in range(len(today[i])):
                    if "(" in today[i][j]:
                        if text_append == "":
                            timetable_today.append("(Спортзал")
                        else:
                            timetable_today.append(text_append)
                        text_append = ""
                        flag_1 = True
                    elif today[i][j].isdigit() or today[i][j] == "-":
                        text_append += today[i][j]
                        
                    elif ")" in today[i][j]:
                        flag_1 = False
                        if text_append in ("Гастелло 15", "Ленсовета 14", "Б. Морская 67"):
                            if "Гастелло 15" in text_append:
                                text_append = "Гаста"
                            elif "Ленсовета 14" in text_append:
                                text_append = "Ленса"
                            elif "Б. Морская 67" in text_append:
                                text_append = "Б.М."
                        timetable_today.append(text_append)
                        text_append = ""

                    elif flag_1:
                        text_append += today[i][j]

                    

            elif flag:
                timetable_today.append(today[i])

        if len(timetable_today) <= 1:
            return "Пар нет, отдыхай"
        return timetable_today

