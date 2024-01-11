from telebot import TeleBot
from telebot.types import Message, InlineKeyboardMarkup
from weather.ob_havo import Obhavo
from keyboards import *

bot = TeleBot("1990895290:AAFnjSJKrC20fhMTNkma6oucNT_nSv8K-0A")


@bot.message_handler(commands=['start'])
def start(message: Message):
    user = message.from_user
    bot.send_message(message.chat.id,
                     f"""Assalomu Alaykum\nQaysi vaqtlardagi ob havo ma'lumotlarini bilishni hohlaysiz 👇""",
                     reply_markup=InlineKeyboardMarkup(weakly_or_daily()))


@bot.callback_query_handler(func=lambda call: True)
def inline_handlerlar(call):
    data = call.data.split("|")
    if data[0] == 'daily':
        bot.set_state(call.message.chat.id, 'daily')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=f"🌡️ Shahar lardan birontasini tanlang 👇",
                              reply_markup=InlineKeyboardMarkup(city()))

    elif data[0] == 'weakly':
        bot.set_state(call.message.chat.id, 'weakly')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=f"🌡️ Shahar lardan birontasini tanlang 👇",
                              reply_markup=InlineKeyboardMarkup(city()))



    elif data[0] == 'back1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=f"Bu yerdan Shahar yoki viloyatni tanla 👇",
                              reply_markup=InlineKeyboardMarkup(city()))
    elif data[0] == 'back2':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=f"🌡️👇Qaysi vaqtlardagi ob havo ma'lumotlarini bilishni hohlaysiz",
                              reply_markup=InlineKeyboardMarkup(weakly_or_daily()))
    else:
        if bot.get_state(call.message.chat.id) == 'daily':
            bot.set_state(call.message.chat.id, 'daily')
            data = call.data.split("|")
            ob_data = Obhavo(data[0]).main()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f"🌡️ Ob-Havo ma'lumoti: \n"
                                       f"⛪️ {ob_data['city']} shahar\n"
                                       f"🕔 {ob_data['day']}\n"
                                       f"📊 {ob_data['info']}\n\n"
                                       f"Batafsil: {ob_data['description']}",
                                  reply_markup=InlineKeyboardMarkup(back()))
        elif bot.get_state(call.message.chat.id) == 'weakly':
            bot.set_state(call.message.chat.id, 'weakly')
            data = call.data.split("|")
            ob_data = Obhavo(data[0]).main()

            weather_table = ob_data['weakly_day']

            formatted_data = []

            rows = weather_table.find_all('tr')

            for row in rows[1:]:
                columns = row.find_all(['td', 'strong'])
                day = columns[0].text.strip()
                icon = columns[4].find('img')['title'].strip()
                day_temp = columns[5].find(class_='forecast-day').text.strip()
                night_temp = columns[5].find(class_='forecast-night').text.strip()
                condition = columns[6].text.strip()
                precipitation = columns[7].text.strip()

                formatted_data.append(
                    f"{day}            {day_temp}/{night_temp}            {condition}            {precipitation}"
                )

            formatted_message = (
                f"🌡️ Ob-Havo ma'lumoti:\n"
                f"Haftalik ob-havo ma'lumotlari:\n"
                f"Kun              Harorat              Tavsif              Yog'ingarchilik\n"
            )

            for day_info in formatted_data:
                formatted_message += f"{day_info}\n\n"

            bot.send_message(call.message.chat.id, formatted_message, reply_markup=InlineKeyboardMarkup(back()))


if __name__ == '__main__':
    bot.polling()
