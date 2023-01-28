from aiogram import types

print("Buttons loading...")

print("Add keyboard 1...")
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(types.KeyboardButton('💸 Баланс'), types.KeyboardButton('💎 Топ'))
keyboard.add(types.KeyboardButton('ℹ️ Помощь'))

print("Add keyboard 2...")

apanel = types.InlineKeyboardMarkup(row_width=3)
apanel.add(types.InlineKeyboardButton(text='Рассылка', callback_data='rass'))


print("Add keyboard 3...")
back = types.ReplyKeyboardMarkup(resize_keyboard=True)
back.add(types.KeyboardButton('Отмена'))