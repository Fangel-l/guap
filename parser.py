import requests
from bs4 import BeautifulSoup
import datetime
from math import ceil
import datetime as date

# constant
MONTH = {
     "января": "1",
     "февраля": "2",
     "марта": "3",
     "апреля": "4",
     "мая": "5",
     "июня": "6",
     "июля": "7",
     "августа": "8",
     "сентября": "9",
     "октября": "10",
     "ноября": "11",
     "декабря": "12",
}

# pars timetable
def timetable_now_pars(now_day, next_day):
     url = "https://guap.ru/rasp/?gr=7074"
     st_accept = "text/html"
     st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"

     headers = {
     "Accept": st_accept,
     "User-Agent": st_useragent}

     req = requests.get(url=url, headers=headers)

     scr = req.text
     soup = BeautifulSoup(scr, "html.parser")
     lessons = soup.find_all(["div", "h4"], ["lead lh-sm", "week2", "week1", "text-danger border-bottom border-danger border-2 px-0 py-2 my-5", "mt-3 text-danger", "opacity-75", "fs-6 lh-sm opacity-50"])

     lessons_list= []
     # preprocessing timetable
     for i in range(len(lessons)):
          if "\n" in lessons[i]:
               b = lessons[i].text.split("\n") 
               for j in range(len(b)):
                    if len(b[j].strip().replace("\xa0", "")) != 0:
                         lessons_list.append(b[j].strip().replace("\xa0", ""))

               
          else:
               lessons_list.append(str(lessons[i].text).strip())

     today = tomorow = -1
     for i in range(len(lessons_list)):
          if now_day in  lessons_list[i]:
               today = i

          elif next_day in lessons_list[i]:
               tomorow = i


     return lessons_list[today:tomorow]


# party week 
def party_week_everyday(day, month, year):
     date_user = date.date(year=year, month=month, day=day)
     if 1 <= month < 9:
          date_old = date.date(year=year-1, month=9, day=1)
     else:
          date_old = date.date(year=year, month=9, day=1)

     delta = (max(date_old, date_user) - min(date_old, date_user)).total_seconds()



     party = ceil(int(delta) / 60 / 60 / 24 / 7)
     if party % 2 == 0:
          return "▼"
     else:
          return "▲"

# pars session(not work)
def session():
     url = "https://raspsess.guap.ru/?g=479"
     st_accept = "text/html"
     st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"

     headers = {
     "Accept": st_accept,
     "User-Agent": st_useragent}

     req = requests.get(url=url, headers=headers)

     scr = req.text
     soup = BeautifulSoup(scr, "html.parser")
     exam = soup.find("div", "result")
     exam_list = exam.text.split()
     return exam_list

