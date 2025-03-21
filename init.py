import telebot
import toke

# init bot 
bot = telebot.TeleBot(toke.Token)
bot.set_my_commands([telebot.types.BotCommand("/start", "Регистрация в боте"),
                    telebot.types.BotCommand("/all", "пингует всех"),
                    telebot.types.BotCommand("/help", "Информация о боте"),
                    telebot.types.BotCommand("/update", "Обновление тг id"),
                    telebot.types.BotCommand("/exam", "Рассписание экзаменов")])