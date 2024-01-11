from telebot.types import InlineKeyboardButton


def city():
    return [
        [InlineKeyboardButton("Toshkent", callback_data=f"toshkent")],
        [InlineKeyboardButton("Andijon", callback_data=f"andijon")],
        [InlineKeyboardButton("Buxoro", callback_data=f"buxoro")],
        [InlineKeyboardButton("Farg`ona", callback_data=f"fargona")],
        [InlineKeyboardButton("Jizzax", callback_data=f"jizzax")],
        [InlineKeyboardButton("Urganch", callback_data=f"urganch")],
        [InlineKeyboardButton("Namangan", callback_data=f"namangan")],
        [InlineKeyboardButton("Navoi", callback_data=f"navoi")],
        [InlineKeyboardButton("Qarshi", callback_data=f"qarshi")],
        [InlineKeyboardButton("Nukus", callback_data=f"nukus")],
        [InlineKeyboardButton("Samarqand", callback_data=f"samarqand")],
        [InlineKeyboardButton("Xiva", callback_data=f"xiva")],
        [InlineKeyboardButton("Termiz", callback_data=f"termiz")],
        [InlineKeyboardButton("Orqaga", callback_data=f"back2")]
    ]


def back():
    return [
        [InlineKeyboardButton("Orqaga", callback_data=f"back1")]
    ]


def weakly_or_daily():
    return [
        [InlineKeyboardButton("Haftalik", callback_data=f"weakly")],
        [InlineKeyboardButton("Kunlik", callback_data=f"daily")],
    ]