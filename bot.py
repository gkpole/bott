# -*- coding: utf-8 -*-
import logging
import sqlite3
import random
import time
import config
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import quote_html
from datetime import datetime, timedelta
from decimal import Decimal
import keyboard as kb
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.exceptions import Throttled
import os
#слито @END_SOFT
logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()

class info(StatesGroup):
  name = State()
  rasst = State()

# bot init
bot = Bot(token='5957645814:AAEpBGnjlDNSZp_WjdLHRU76SaDz7m1DixI')
dp = Dispatcher(bot)

# datebase
connect = sqlite3.connect("users.db")
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id BIGINT,
    balance INT,
    bank BIGINT,
    user_name STRING,
    user_status STRING,
    rating INT
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS bot(
    chat_id INT,
    last_stavka INT
)
""")

# start command
@dp.message_handler(commands=['start'])
async def start_cmd(message):
    msg = message
    user_id = msg.from_user.id
    user_name = msg.from_user.full_name
    user_status = "Player"
    chat_id = message.chat.id
    cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?);", (user_id, 10000, 0, user_name, user_status, 0))
        cursor.execute("INSERT INTO bot VALUES(?, ?);", (chat_id, 0))
        connect.commit()
    else:
        cursor.execute("INSERT INTO bot VALUES(?, ?);", (chat_id, 0))
        connect.commit()
        return
    
    name1 = message.from_user.get_mention(as_html=True)
    await message.reply("бот является примером для канала портфолио пользователя @noziss")
    await message.reply( f'👋 Привет, {name1} \nЯ бот для игры в различные игры.\nТебе выдан подарок в размере 10000$.\nТак же ты можешь добавить меня в беседу для игры с друзьями.\n🆘 Чтобы узнать все команды введи "Помощь"', parse_mode='html')

###########################################БАЛАНС###########################################
@dp.message_handler()
async def prof_user(message: types.Message):
    if message.text.lower() in ["баланс", "Баланс", "Б", "б"]:
       msg = message
       user_id = msg.from_user.id
       user_name = msg.from_user.full_name
       chat_id = message.chat.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = int(balance[0])
       balance2 = '{:,}'.format(balance)
       bank = cursor.execute("SELECT bank from users where user_id = ?",(message.from_user.id,)).fetchone()
       bank = round(int(bank[0]))
       bank2 = '{:,}'.format(bank)
       c = 999999999999999999999999
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       else:
        pass
       if bank >= 999999999999999999999999:
          bank = 999999999999999999999999
          cursor.execute(f'UPDATE users SET bank = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          bank2 = '{:,}'.format(bank) 
       else:
        pass
       await bot.send_message(message.chat.id, f"👫Ник: {user_name} \n💰Деньги: {balance2}$ \n🏦Банк: {bank2}$")
#слито @END_SOFT
    if message.text.lower() in ["профиль", "Профиль"]:
       msg = message
       chat_id = message.chat.id
       name1 = message.from_user.get_mention(as_html=True)
       user_name = msg.from_user.full_name
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       bank = cursor.execute("SELECT bank from users where user_id = ?",(message.from_user.id,)).fetchone()
       rating = cursor.execute("SELECT rating from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = int(balance[0])
       bank = int(bank[0])
       rating = int(rating[0])
       c = 999999999999999999999999
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit() 
       else:
        pass
       if int(balance) in range(0, 1000):
          balance3 = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
          balance3 = int(balance3[0])
       if int(balance) in range(1000, 999999):
          balance1 = balance / 1000
          balance2 = round(balance1)
          balance3 = f'{balance2} тыс'
       if int(balance) in range(1000000, 999999999):
          balance1 = balance / 1000000
          balance2 = round(balance1)
          balance3 = f'{balance2} млн'
       if int(balance) in range(1000000000, 999999999999):
          balance1 = balance / 1000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} млрд'
       if int(balance) in range(1000000000000, 999999999999999):
          balance1 = balance / 1000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} трлн'
       if int(balance) in range(1000000000000000, 999999999999999999):
          balance1 = balance / 1000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} квдр'
       if int(balance) in range(1000000000000000000, 999999999999999999999):
          balance1 = balance / 1000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} квнт'
       if int(balance) in range(1000000000000000000000, 999999999999999999999999):
          balance1 = balance / 1000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} скст'
       if bank >= 999999999999999999999999:
          bank = 999999999999999999999999
          cursor.execute(f'UPDATE users SET bank = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()   
       else:
        pass
       if int(bank) in range(0, 1000):
          bank3 = cursor.execute("SELECT bank from users where user_id = ?",(message.from_user.id,)).fetchone()
          bank3 = int(bank3[0])
       if int(bank) in range(1000, 999999):
          bank1 = bank / 1000
          bank2 = round(bank1)
          bank3 = f'{bank2} тыс'
       if int(bank) in range(1000000, 999999999):
          bank1 = bank / 1000000
          bank2 = round(bank1)
          bank3 = f'{bank2} млн'
       if int(bank) in range(1000000000, 999999999999):
          bank1 = bank / 1000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} млрд'
       if int(bank) in range(1000000000000, 999999999999999):
          bank1 = bank / 1000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} трлн'
       if int(bank) in range(1000000000000000, 999999999999999999):
          bank1 = bank / 1000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} квдр'
       if int(bank) in range(1000000000000000000, 999999999999999999999):
          bank1 = bank / 1000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} квнт'
       if int(bank) in range(1000000000000000000000, 999999999999999999999999):
          bank1 = bank / 1000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} скст'
       if rating >= 999999999999999999999999:
          rating = 999999999999999999999999
          cursor.execute(f'UPDATE users SET rating = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
       else:
        pass
       if int(rating) in range(0, 1000):
          rating3 = cursor.execute("SELECT rating from users where user_id = ?",(message.from_user.id,)).fetchone()
          rating3 = int(rating3[0])
       if int(rating) in range(1000, 999999):
          rating1 = rating / 1000
          rating2 = round(rating1)
          rating3 = f'{rating2} тыс'
       if int(rating) in range(1000000, 999999999):
          rating1 = rating / 1000000
          rating2 = round(rating1)
          rating3 = f'{rating2} млн'
       if int(rating) in range(1000000000, 999999999999):
          rating1 = rating / 1000000000
          rating2 = round(rating1) 
          rating3 = f'{rating2} млрд'
       if int(rating) in range(1000000000000, 999999999999999):
          rating1 = rating / 1000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} трлн'
       if int(rating) in range(1000000000000000, 999999999999999999):
          rating1 = rating / 1000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} квдр'
       if int(rating) in range(1000000000000000000, 999999999999999999999):
          rating1 = rating / 1000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} квнт'
       if int(rating) in range(1000000000000000000000, 999999999999999999999999):
          rating1 = rating / 1000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} скст'
       await bot.send_message(message.chat.id, f"{name1}, ваш профиль:\n 🔎 ID: {user_id}\n 💰 Деньги: {balance3}$\n 🏦 В банке: {bank3}$\n 👑 Рейтинг: {rating3}",  parse_mode='html')   

###########################################рассылка#######################################
@dp.callback_query_handler(lambda call: call.data.startswith('rass'))    
async def usender(call):
  await call.message.answer('Введите текст для рассылки.\n\nДля отмены нажмите кнопку ниже 👇', reply_markup=kb.back)
  await info.rasst.set()

@dp.message_handler(state=info.rasst)
async def process_name(message: types.Message, state: FSMContext):
  q.execute(f'SELECT user_id FROM users')
  row = q.fetchall()
  connection.commit()
  if message.text == 'Отмена':
    await message.answer('Отмена! Возвращаю в главное меню.', reply_markup=kb.keyboard)
    await state.finish()
  else:
    info = row
    await message.answer('Начинаю рассылку...')
    for i in range(len(info)):
      try:
        await bot.send_message(info[i][0], str(message.text))
      except:
        pass
    await message.answer('Рассылка завершена.', reply_markup=kb.keyboard)
    await state.finish()
###########################################БАНК###########################################
    # bank
    if message.text.startswith("+банк"):
       msg = message
       chat_id = message.chat.id
       user_id = msg.from_user.id
       name = msg.from_user.last_name 
       user_name = message.from_user.get_mention(as_html=True)

       bank_p = int(msg.text.split()[1])
       print(f"{name} положил в банк: {bank_p}")

       cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
       bank = round(int(bank[0]))
       bank2 = '{:,}'.format(bank_p)
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       if bank_p > 0:
          if balance >= bank_p:  
             await bot.send_message(message.chat.id, f'{user_name}, вы успешно положили в банк {bank2}$ {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - bank_p} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET bank = {bank + bank_p} WHERE user_id = "{user_id}"') 
             connect.commit()    
   
          elif int(balance) < int(bank_p):
             await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}', parse_mode='html')

       if bank_p <= 0:
          await bot.send_message(message.chat.id, f'{user_name}, нельзя положить в банк отрицательное число! {rloser}', parse_mode='html')  

    if message.text.startswith("-банк"):
       msg = message
       chat_id = message.chat.id
       user_id = msg.from_user.id
       name = msg.from_user.last_name 
       user_name = message.from_user.get_mention(as_html=True)

       bank_s = int(msg.text.split()[1])
       print(f"{name} снял с банка: {bank_s}")

       cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
       bank = round(int(bank[0]))
       bank2 = '{:,}'.format(bank_s)
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)

       if bank_s > 0:
          if bank >= bank_s:  
             await bot.send_message(message.chat.id, f'{user_name}, вы успешно сняли с банковского счёта {bank2}$ {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET bank = {bank - bank_s} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET balance = {balance + bank_s} WHERE user_id = "{user_id}"') 
             connect.commit()    
   
          elif int(bank) < int(bank_s):
             await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств на банковском счету! {rloser}', parse_mode='html')

       if bank_s <= 0:
          await bot.send_message(message.chat.id, f'{user_name}, нельзя снять с банка отрицательное число! {rloser}', parse_mode='html')  

    if message.text.startswith("+Банк"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       name = msg.from_user.last_name 
       user_name = message.from_user.get_mention(as_html=True)

       bank_p = int(msg.text.split()[1])
       print(f"{name} положил в банк: {bank_p}")

       cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
       bank = round(int(bank[0]))
       bank2 = '{:,}'.format(bank_p)
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       if bank_p > 0:
          if balance >= bank_p:  
             await bot.send_message(message.chat.id, f'{user_name}, вы успешно положили в банк {bank2}$ {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - bank_p} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET bank = {bank + bank_p} WHERE user_id = "{user_id}"') 
             connect.commit()    
   
          elif int(balance) < int(bank_p):
             await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}', parse_mode='html')

       if bank_p <= 0:
          await bot.send_message(message.chat.id, f'{user_name}, нельзя положить в банк отрицательное число! {rloser}', parse_mode='html')  
#слито @END_SOFT
    if message.text.startswith("-Банк"):
       msg = message
       user_id = msg.from_user.id
       name = msg.from_user.last_name 
       chat_id = message.chat.id
       user_name = message.from_user.get_mention(as_html=True)

       bank_s = int(msg.text.split()[1])
       print(f"{name} снял с банка: {bank_s}")

       cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
       bank = round(int(bank[0]))
       bank2 = '{:,}'.format(bank_s)
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       if bank_s > 0:
          if bank >= bank_s:  
             await bot.send_message(message.chat.id, f'{user_name}, вы успешно сняли с банковского счёта {bank2}$ {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET bank = {bank - bank_s} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET balance = {balance + bank_s} WHERE user_id = "{user_id}"') 
             connect.commit()    
   
          elif int(bank) < int(bank_s):
             await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств на банковском счету! {rloser}', parse_mode='html')

       if bank_s <= 0:
          await bot.send_message(message.chat.id, f'{user_name}, нельзя снять с банка отрицательное число! {rloser}', parse_mode='html')  

###########################################АДМИН КОМАНДЫ###########################################
    if message.text.startswith("выдать"):
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       perevod = int(msg.text.split()[1])
       reply_user_id = msg.reply_to_message.from_user.id
       perevod2 = '{:,}'.format(perevod)
       user_id = msg.from_user.id
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])
       if user_status[0] == 'Admin':
          await message.reply(f"💰 | Вы выдали {perevod2}$ игроку <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Owner':
          await message.reply(f"💰 | Вы выдали {perevod2}$ игроку <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота!", parse_mode='html')  

    if message.text.startswith("Выдать"):
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       perevod = int(msg.text.split()[1])
       reply_user_id = msg.reply_to_message.from_user.id
       perevod2 = '{:,}'.format(perevod)
       user_id = msg.from_user.id
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])
       if user_status[0] == 'Admin':
          await message.reply(f"💰 | Вы выдали {perevod2}$ игроку <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Owner':
          await message.reply(f"💰 | Вы выдали {perevod2}$ игроку <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота!", parse_mode='html')  

    if message.text.startswith("забрать"):
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       perevod = int(msg.text.split()[1])
       reply_user_id = msg.reply_to_message.from_user.id
       perevod2 = '{:,}'.format(perevod)
       user_id = msg.from_user.id
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])
       if user_status[0] == 'Admin':
          await message.reply(f"💰 | Вы забрали {perevod2}$ у игрока <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 - perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Owner':
          await message.reply(f"💰 | Вы забрали {perevod2}$ у игрока <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 - perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота!", parse_mode='html')  

    if message.text.startswith("Забрать"):
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       perevod = int(msg.text.split()[1])
       reply_user_id = msg.reply_to_message.from_user.id
       perevod2 = '{:,}'.format(perevod)
       user_id = msg.from_user.id
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])
       if user_status[0] == 'Admin':
          await message.reply(f"💰 | Вы забрали {perevod2}$ у игрока <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 - perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Owner':
          await message.reply(f"💰 | Вы забрали {perevod2}$ у игрока <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 - perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота!", parse_mode='html')  

    if message.text.lower() in ["обнулить", "Обнулить"]:
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       reply_user_id = msg.reply_to_message.from_user.id
       user_id = msg.from_user.id
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       if user_status[0] == 'Admin':
          await message.reply(f"💰 | Вы обнулили игрока <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET rating = {0} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Owner':
          await message.reply(f"💰 | Вы обнулили игрока <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET rating = {0} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота!", parse_mode='html')

    if message.text.lower() in ["забанить", "Забанить"]:
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       reply_user_id = msg.reply_to_message.from_user.id
       user_id = msg.from_user.id
       user_status2 = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_status = "Blocked"
       if user_status2[0] == "Admin":
          await message.reply(f"🛑 | Вы забанили игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET rating = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
          connect.commit()
       if user_status2[0] == "Owner":
          await message.reply(f"🛑 | Вы забанили игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET rating = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
          connect.commit()
       if user_status2[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота!", parse_mode='html')

    if message.text.lower() in ["повысить", "Повысить"]:
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       reply_user_id = msg.reply_to_message.from_user.id
       user_id = msg.from_user.id
       user_status2 = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_status = "Admin"
       if user_status2[0] == "Owner":
          await message.reply(f"🛑 | Вы выдали админа бота игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
          connect.commit()
       if user_status2[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь создателем бота!", parse_mode='html')
       if user_status2[0] == 'Admin':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь создателем бота!", parse_mode='html')
    
    if message.text.lower() in ["разжаловать", "Разжаловать"]:
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       reply_user_id = msg.reply_to_message.from_user.id
       user_id = msg.from_user.id
       user_status2 = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_status = "Player"
       if user_status2[0] == "Owner":
          await message.reply(f"🛑 | Вы забрали админа бота у игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
          connect.commit()
       if user_status2[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь создателем бота!", parse_mode='html')
       if user_status2[0] == 'Admin':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь создателем бота!", parse_mode='html')
       
    if message.text.lower() in ["разбанить", "Разбанить"]:
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       reply_user_id = msg.reply_to_message.from_user.id
       user_id = msg.from_user.id
       user_status = "Player"
       user_status2 = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       if user_status2[0] == "Admin":
          await message.reply(f"✅ | Вы разбанили игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
          connect.commit()
       if user_status2[0] == "Owner":
          await message.reply(f"✅ | Вы разбанили игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
          connect.commit()
       if user_status2[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота!", parse_mode='html')
 
###########################################ПОМОЩЬ###########################################
    if message.text.lower() in ["помощь", "Помощь"]:
       await bot.send_message(message.chat.id, f'🧨Мои команды: \n 💡 Разное: \n 📒 Профиль \n 💸Б/Баланс \n 🌐+/-Биткоины \n 🌐Биткоин курс \n 👑+/-Рейтинг \n  👑Топ \n 🤝 Передать [сумма] [команда работает ответом на сообщение] \n 💭 РП-команды - вывести список РП-команд  \n  🚀 Игры: \n 🎰 Казино [ставка] \n 🎮 Спин [ставка]')

###########################################КАЗИНО###########################################
    if message.text.startswith("Казино"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id

       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rx = random.randint(0,110)
       rwin = random.choice(win)
       rloser = random.choice(loser)

       msg = message
       name1 = message.from_user.get_mention(as_html=True)
       name = msg.from_user.last_name 
       summ = int(msg.text.split()[1])
       print(f"{name} поставил в казино: {summ} и выиграл/проиграл: {rx}")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       period = 5
       get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       if stavkatime > period:
          if balance >= summ:
             if summ > 0:
                if int(rx) in range(0,9):
                   c = Decimal(summ)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}$ (x0) {rloser}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()   
                   return                           
                if int(rx) in range(10,29):
                   c = Decimal(summ - summ * 0.25)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}$ (x0.25) {rloser}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.75} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()  
                   return   
                if int(rx) in range(30,44):
                   c = Decimal(summ * 0.5)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}$ (x0.5) {rloser}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.5} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return  
                if int(rx) in range(45,54):
                   c = Decimal(summ - summ * 0.75)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}$ (x0.75) {rloser}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.25} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return  
                if int(rx) in range(55,64):
                   c = summ * 1
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, ваши деньги остаются при вас {c2}$ (x1) {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()
                   return 
                if int(rx) in range(65,69):
                   c = Decimal(summ * 1.25)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x1.25) {rwin}', parse_mode='html')

                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.25)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()           
                   return 
                if int(rx) in range(70,74):
                   c = Decimal(summ * 1.5)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x1.5) {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.5)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()  
                   return 
                if int(rx) in range(75,84):
                   c = Decimal(summ * 1.75)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x1.75) {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.75)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()  
                   return 
                if int(rx) in range(85,95):
                   c = Decimal(summ * 2)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x2) {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return 
                if int(rx) in range(100,108):
                   c = Decimal(summ * 3)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x3) {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 3)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return 
                if int(rx) == 109:
                   c = Decimal(summ * 5)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x5) {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 5)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                if int(rx) == 100:
                   c = Decimal(summ * 10)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x10) {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 10)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return 
             elif summ <= 0:
                  await bot.send_message(chat_id, f'{name1}, нельзя ставить отрицательное число! {rloser}', parse_mode='html')                                      
          elif int(balance) <= int(summ):
               await bot.send_message(chat_id, f'{name1}, недостаточно средств! {rloser}', parse_mode='html')
       else:
        await bot.send_message(chat_id, f'{name1}, играть играть можно каждые 5 секунд! {rloser}', parse_mode='html')
        return

    if message.text.startswith("казино"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id

       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rx = random.randint(0,110)
       rwin = random.choice(win)
       rloser = random.choice(loser)

       msg = message
       name1 = message.from_user.get_mention(as_html=True)
       name = msg.from_user.last_name 
       summ = int(msg.text.split()[1])
       print(f"{name} поставил в казино: {summ} и выиграл/проиграл: {rx}")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       period = 5
       get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       if stavkatime > period:
          if balance >= summ:
             if summ > 0:
                if int(rx) in range(0,9):
                   c = Decimal(summ)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}$ (x0) {rloser}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()   
                   return                           
                if int(rx) in range(10,29):
                   c = Decimal(summ - summ * 0.25)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}$ (x0.25) {rloser}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.75} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()  
                   return   
                if int(rx) in range(30,44):
                   c = Decimal(summ * 0.5)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}$ (x0.5) {rloser}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.5} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return  
                if int(rx) in range(45,54):
                   c = Decimal(summ - summ * 0.75)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}$ (x0.75) {rloser}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.25} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return  
                if int(rx) in range(55,64):
                   c = summ * 1
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, ваши деньги остаются при вас {c2}$ (x1) {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()
                   return 
                if int(rx) in range(65,69):
                   c = Decimal(summ * 1.25)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x1.25) {rwin}', parse_mode='html')

                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.25)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()           
                   return 
                if int(rx) in range(70,74):
                   c = Decimal(summ * 1.5)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x1.5) {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.5)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()  
                   return 
                if int(rx) in range(75,84):
                   c = Decimal(summ * 1.75)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x1.75) {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.75)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()  
                   return 
                if int(rx) in range(85,95):
                   c = Decimal(summ * 2)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x2) {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return 
                if int(rx) in range(100,108):
                   c = Decimal(summ * 3)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x3) {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 3)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return 
                if int(rx) == 109:
                   c = Decimal(summ * 5)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x5) {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 5)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                if int(rx) == 100:
                   c = Decimal(summ * 10)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}$ (x10) {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 10)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return 
             elif summ <= 0:
                  await bot.send_message(chat_id, f'{name1}, нельзя ставить отрицательное число! {rloser}', parse_mode='html')                                      
          elif int(balance) <= int(summ):
               await bot.send_message(chat_id, f'{name1}, недостаточно средств! {rloser}', parse_mode='html')
       else:
        await bot.send_message(chat_id, f'{name1}, играть играть можно каждые 5 секунд! {rloser}', parse_mode='html')
        return

###########################################РЕЙТИНГ###########################################
    if message.text.startswith("+рейтинг"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       user_name = message.from_user.get_mention(as_html=True)
       summ = int(msg.text.split()[1])
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
       rating = int(rating[0])
       rating2 = '{:,}'.format(summ)
       c = summ * 150000000
       c2 = '{:,}'.format(c)
       if summ > 0:
        if int(balance) >= int(summ * 150000000):
          await bot.send_message(message.chat.id, f'{user_name}, вы повысили количество вашего рейтинга на {rating2}👑 за {c2}$! {rwin}', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"')
          cursor.execute(f'UPDATE users SET rating = {rating + summ} WHERE user_id = "{user_id}"')
          connect.commit()

 
        if int(balance) < int(summ * 150000000):
          await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}', parse_mode='html')

       if summ <= 0:
         await bot.send_message(message.chat.id, f'{user_name}, нельзя купить отрицательное число! {rloser}', parse_mode='html')
    
    if message.text.startswith("-рейтинг"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       user_name = message.from_user.get_mention(as_html=True)
       summ = int(msg.text.split()[1])
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
       rating = int(rating[0])
       c = summ * 100000000
       c2 = '{:,}'.format(c)
       rating2 = '{:,}'.format(summ)
       if summ > 0:
        if int(rating) >= int(summ):
          await bot.send_message(message.chat.id, f'{user_name}, вы понизили количество вашего рейтинга на {rating2}👑 за {c2}$! {rwin}', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + c} WHERE user_id = "{user_id}"')
          cursor.execute(f'UPDATE users SET rating = {rating - summ} WHERE user_id = "{user_id}"')
          connect.commit()

        if int(rating) < int(summ):
          await bot.send_message(message.chat.id, f'{user_name}, у вас недостаточно рейтинга для его продажи! {rloser}', parse_mode='html')

       if summ <= 0:
          await bot.send_message(message.chat.id, f'{user_name}, нельзя продать отрицательное число! {rloser}', parse_mode='html')
#слито @END_SOFT
    if message.text.startswith("+Рейтинг"):
       msg = message
       user_id = msg.from_user.id
       user_name = message.from_user.get_mention(as_html=True)
       summ = int(msg.text.split()[1])
       chat_id = message.chat.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
       rating = int(rating[0])
       rating2 = '{:,}'.format(summ)
       c = summ * 150000000
       c2 = '{:,}'.format(c)
       if summ > 0:
        if int(balance) >= int(summ * 150000000):
          await bot.send_message(message.chat.id, f'{user_name}, вы повысили количество вашего рейтинга на {rating2}👑 за {c2}$! {rwin}', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"')
          cursor.execute(f'UPDATE users SET rating = {rating + summ} WHERE user_id = "{user_id}"')
          connect.commit()

 
        if int(balance) < int(summ * 150000000):
          await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}', parse_mode='html')

       if summ <= 0:
         await bot.send_message(message.chat.id, f'{user_name}, нельзя купить отрицательное число! {rloser}', parse_mode='html')
    
    if message.text.startswith("-Рейтинг"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       user_name = message.from_user.get_mention(as_html=True)
       summ = int(msg.text.split()[1])
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
       rating = int(rating[0])
       c = summ * 100000000
       c2 ='{:,}'.format(c)
       rating2 = '{:,}'.format(summ)
       if summ > 0:
        if int(rating) >= int(summ):
          await bot.send_message(message.chat.id, f'{user_name}, вы понизили количество вашего рейтинга на {rating2}👑 за {c2}$! {rwin}', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + c} WHERE user_id = "{user_id}"')
          cursor.execute(f'UPDATE users SET rating = {rating - summ} WHERE user_id = "{user_id}"')
          connect.commit()
 
        if int(rating) < int(summ):
          await bot.send_message(message.chat.id, f'{user_name}, у вас недостаточно рейтинга для его продажи! {rloser}', parse_mode='html')

       if summ <= 0:
          await bot.send_message(message.chat.id, f'{user_name}, нельзя продать отрицательное число! {rloser}', parse_mode='html')

###########################################ПЕРЕВОДЫ###########################################
    if message.text.startswith("дать"):
       msg = message
       user_id = msg.from_user.id
       name = msg.from_user.last_name 
       rname =  msg.reply_to_message.from_user.last_name 
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply_user_id = msg.reply_to_message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)

       perevod = int(msg.text.split()[1])
       perevod2 = '{:,}'.format(perevod)
       print(f"{name} перевел: {perevod} игроку {rname}")

       cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])

       if not message.reply_to_message:
          await message.reply("Эта команда должна быть ответом на сообщение!")
          return
       
       if reply_user_id == user_id:
          await message.reply_to_message.reply(f'Вы не можете передать деньги сами себе! {rloser}', parse_mode='html')
          return

       if perevod > 0:
          if balance >= perevod:  
             await message.reply_to_message.reply(f'Вы передали {perevod2}$ игроку {reply_user_name} {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - perevod} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
             connect.commit()    
   
          elif int(balance) <= int(perevod):
             await message.reply( f'{user_name}, недостаточно средств! {rloser}', parse_mode='html')

       if perevod <= 0:
          await message.reply( f'{user_name}, нельзя перевести отрицательное число! {rloser}', parse_mode='html')  

    if message.text.startswith("Дать"):
       msg = message
       user_id = msg.from_user.id
       name = msg.from_user.last_name 
       rname =  msg.reply_to_message.from_user.last_name 
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply_user_id = msg.reply_to_message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)

       perevod = int(msg.text.split()[1])
       perevod2 = '{:,}'.format(perevod)
       print(f"{name} перевел: {perevod} игроку {rname}")

       cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])

       if not message.reply_to_message:
          await message.reply("Эта команда должна быть ответом на сообщение!")
          return
       
       if reply_user_id == user_id:
          await message.reply_to_message.reply(f'Вы не можете передать деньги сами себе! {rloser}', parse_mode='html')
          return

       if perevod > 0:
          if balance >= perevod:  
             await message.reply_to_message.reply(f'Вы передали {perevod2}$ игроку {reply_user_name} {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - perevod} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
             connect.commit()    
   
          elif int(balance) <= int(perevod):
             await message.reply( f'{user_name}, недостаточно средств! {rloser}', parse_mode='html')

       if perevod <= 0:
          await message.reply( f'{user_name}, нельзя перевести отрицательное число! {rloser}', parse_mode='html')  

    if message.text.startswith("передать"):
       msg = message
       user_id = msg.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_id = int(msg.text.split()[2])
       ruser_name = cursor.execute("SELECT user_name from users where user_id = ?",(reply_user_id,)).fetchone()
       ruser_name = ruser_name[0] 
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)

       perevod = int(msg.text.split()[1])
       perevod2 = '{:,}'.format(perevod)

       cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (reply_user_id,)).fetchone()
       balance2 = round(balance2[0])
       
       if reply_user_id == user_id:
          await message.reply_to_message.reply(f'ℹ | Вы не можете передать деньги сами себе! {rloser}', parse_mode='html')
          return

       if perevod > 0:
          if balance >= perevod:  
             await bot.send_message(message.chat.id, f"💸 | Вы передали {perevod2}$ игроку <a href='tg://user?id={reply_user_id}'>{ruser_name}</a> {rwin}", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - perevod} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
             connect.commit()    
   
          elif int(balance) <= int(perevod):
             await message.reply( f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')

       if perevod <= 0:
          await message.reply( f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя перевести отрицательное число! {rloser}", parse_mode='html')   

###########################################ТОП###########################################
    if message.text.lower() in ["топ", "Топ"]:
       list = cursor.execute(f"SELECT * FROM users ORDER BY rating DESC").fetchmany(10)
       top_list = []
       chat_id = message.chat.id
       name = message.from_user.get_mention(as_html=True)
       num = 0
       for user in list:
           if user[5] >= 999999999999999999999999:
              c6 = 999999999999999999999999
           else:
              c6 = user[5]
           num += 1
           c = Decimal(c6)
           c2 = '{:,}'.format(c)
           
           top_list.append(f"{num}. {user[3]}  — 👑{c2}")
       top = "\n".join(top_list)
       await bot.send_message(message.chat.id, f"{name}, топ 10 игроков бота:\n" + top , parse_mode='html')
#слито @END_SOFT
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
