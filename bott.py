import logging
import sqlite3
import random
import time
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import quote_html
from datetime import datetime, timedelta
from decimal import Decimal
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton


logging.basicConfig(level=logging.INFO)

TOKEN = "5581903094:AAEmKc-cgTb_4SL5Uydst0OZgtJ_CbwRk5I"

# bot init
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



# datebase
connect = sqlite3.connect("ussg.db")
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id BIGINT,
    balance INT,
    user_name STRING,
    chat_id INT,
    bank BIGINT
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS bot(
    chat_id INT,
    last_stavka INT
)
""")

@dp.message_handler(lambda message: message.text.lower() == 'игра')
async def process_command_1(message: types.Message):
    
    button1 = InlineKeyboardButton('🗿Камень', callback_data = '1')
    button2 = InlineKeyboardButton('✂️Ножницы', callback_data = '2')
    button3 = InlineKeyboardButton('📄Бумага', callback_data = '3')
    buttons = InlineKeyboardMarkup().add(button1, button2, button3)
    await bot.send_message(message.chat.id, "Я готов играть!\nВыбери предмет, что бы сыграть со мной🎭", reply_markup= buttons)

@dp.callback_query_handler(lambda c: c.data == '1')
async def process_callback_yes(callback: types.CallbackQuery):
    rand = random.choice(["🗿Камень", "✂️Ножницы", "📄Бумага"])

    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer("Я выбрал " + rand + "\nА ты выбрал 🗿Камень")
    if rand == '🗿Камень':
        await callback.message.answer("У нас ничья🤝")
    elif rand == '✂️Ножницы':
        await callback.message.answer("Ты выиграл🥇")
    else:
        await callback.message.answer("Я победил🥇")

@dp.callback_query_handler(lambda c: c.data == '2')
async def process_callback_yes(callback: types.CallbackQuery):
    rand = random.choice(["🗿Камень", "✂️Ножницы", "📄Бумага"])

    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer("Я выбрал " + rand + "\nА ты выбрал ✂️Ножницы")
    if rand == '🗿Камень':
        await callback.message.answer("Я победил🥇")
    elif rand == '✂️Ножницы':
        await callback.message.answer("У нас ничья🤝")
    else:
        await callback.message.answer("Ты победил🥇")
        
# start command
@dp.message_handler(commands=['start','старт','Старт'])
async def start_cmd(message):
    msg = message
    user_id = msg.from_user.id
    user_name = msg.from_user.full_name
    chat_id = message.chat.id
    cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?);", (user_id, 10000, user_name, chat_id, 0))
        cursor.execute("INSERT INTO bot VALUES(?, ?);", (chat_id, 0))
        connect.commit()
    else:
        cursor.execute("INSERT INTO bot VALUES(?, ?);", (chat_id, 0))
        connect.commit()
        return

    photo = open('starts.jpg', 'rb')
    name1 = message.from_user.get_mention(as_html=True)
    await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f'🎍 | Привет {name1}!!\n🎮 | Я бот для игры в различные игры✨\n💡 | Меня зовут Qwerty Bot\nНадеюсь ты меня не бросишь!\n🆘 | Чтобы узнать мои команды напиши: "Помощь" и выбери соответствующую кнопочку.\n\n<a href="https://t.me/BFG755">🗯 | Наш общий чатик</a>\n<a href="https://t.me/Qwertynovosti1">📢 | Наш канал для свежих новостей</a>\n\n🔥 | Бот часто обновляется поэтому ждите добавим очень классных вещей✨', parse_mode='html')
                   
###########################################БАЛАНС###########################################
@dp.message_handler()
async def prof_user(message: types.Message):
    if message.text.lower() in ["баланс", "Баланс", "Б", "БАЛАНС", "б"]:
       msg = message
       photo = open('dengi.jpg', 'rb')
       user_id = msg.from_user.id
       user_name = msg.from_user.full_name
       chat_id = message.chat.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = int(balance[0])
       balance2 = '{:,}'.format(balance)
       bank = cursor.execute("SELECT bank from users where user_id = ?",(message.from_user.id,)).fetchone()
       bank = round(int(bank[0]))
       bank2 = '{:,}'.format(bank)
       c = 999999999999999999999999999
       if balance >= 999999999999999999999999999:
          balance = 999999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       else:
        pass
       if bank >= 999999999999999999999999999:
          bank = 999999999999999999999999999
          cursor.execute(f'UPDATE users SET bank = {999999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          bank2 = '{:,}'.format(bank) 
       else:
        pass
       await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f"🤵‍♂️ | Никнейм: {user_name} \n💵 | Наличные: {balance2}₽\n💳 | На карте: {bank2}₽")

###########################################КАЗИНО###########################################
    if message.text.startswith("Казино"):
        msg = message
        user_id = msg.from_user.id
        chat_id = message.chat.id

        win = ['🙂', '😋', '😄', '😃']
        loser = ['😔', '😕', '😣', '😞', '😢']
        rx = random.randint(0, 110)
        rwin = random.choice(win)
        rloser = random.choice(loser)

        msg = message
        name1 = message.from_user.get_mention(as_html=True)
        name = msg.from_user.last_name
        summ = float(msg.text.split()[1])
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
                    if int(rx) in range(0, 15):
                        c = Decimal(summ)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼|Игрок: {name1}, \n👩‍💼|Игра: Казино\n🎰|Ставка: {summ} \n📃|Результаты: Проиграли: {c2}₽ (x0) {rloser}', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(16, 33):
                        c = Decimal(summ - summ * 0.25)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼|Игрок: {name1},\n👩‍💼|Игра: Казино\n🎰|Ставка:{summ} \n📃|Результаты: Проиграли: {c2}₽ (x0.25) {rloser}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {balance - summ * 0.75} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(34, 54):
                        c = Decimal(summ * 0.5)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼\Игрок: {name1},\n👩‍💼|Игра: Казино\n🎰|Ставка: {summ} \n📃Результаты: Проиграли: {c2}₽ (x0.5) {rloser}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.5} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(54, 62):
                        c = Decimal(summ - summ * 0.75)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼|Игрок: {name1},\n👩‍💼|Игра: Казино\n🎰|Ставка: {summ}\n📃Проиграли: {c2}₽ (x0.75) {rloser}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {balance - summ * 0.25} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(63, 73):
                        c = summ * 1
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼|Ник: {name1}, \n👩‍💼|Игра: Казино\n🎰|Ставка: {summ} \n📃Результаты: Деньги остаются при вас! {c2}₽ (x1) {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(74, 83):
                        c = Decimal(summ * 1.25)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼|Ник: {name1},👩‍💼|Игра: Казино\n🎰|Ставка: {summ}\n📃Результаты: Выиграли {c2}₽ (x1.25) {rwin}', parse_mode='html')

                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 1.25)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(84, 90):
                        c = Decimal(summ * 1.5)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼|Ник: {name1},\n👩‍💼|Игра: Казино\n🎰|Ставка: {summ} \n📃Результаты: Выиграли {c2}₽ (x1.5) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 1.5)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(91, 96):
                        c = Decimal(summ * 1.75)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼|Ник: {name1},\n👩‍💼|Игра: Казино\n🎰|Ставка: {summ} \n📃Результаты: Выиграли {c2}₽ (x1.75) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 1.75)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(97, 102):
                        c = Decimal(summ * 2)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼|Ник: {name1},\n👩‍💼|Игра: Казино\n🎰|Ставка: {summ} \n📃Результаты: Выиграли {c2}₽ (x2) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(103, 106):
                        c = Decimal(summ * 3)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼|Ник: {name1},\n👩‍💼|Игра: Казино\n🎰|Ставка: {summ} \n📃Результаты: Выиграли {c2}₽ (x3) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 3)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) == 110:
                        c = Decimal(summ * 50)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼|Ник: {name1},\n👩‍💼|Игра: Казино\n🎰|Ставка: {summ} \n📃Результаты: Выиграли {c2}₽ (x50) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 50)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                    if int(rx) in range(107, 109):
                        c = Decimal(summ * 10)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼|Ник: {name1},\n👩‍💼|Игра: Казино\n🎰|Ставка: {summ} \n📃Результаты: Выиграли {c2}₽ (x10) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 10)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                elif summ <= 1:
                    await bot.send_message(chat_id, f'{name1}, нельзя ставить отрицательное число! {rloser}',
                                           parse_mode='html')
            elif int(balance) <= int(summ):
                await bot.send_message(chat_id, f'{name1}, недостаточно средств! {rloser}', parse_mode='html')
        else:
            await bot.send_message(chat_id, f'{name1}, извини. но играть можно только каждые 5️⃣ секунд. {rloser}',
                                   parse_mode='html')
            return
            
            

    if message.text.startswith("казино"):
        msg = message
        user_id = msg.from_user.id
        chat_id = message.chat.id

        win = ['🙂', '😋', '😄', '😃']
        loser = ['😔', '😕', '😣', '😞', '😢']
        rx = random.randint(0, 110)
        rwin = random.choice(win)
        rloser = random.choice(loser)

        msg = message
        name1 = message.from_user.get_mention(as_html=True)
        name = msg.from_user.last_name
        summ = float(msg.text.split()[1])
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
                    if int(rx) in range(0, 15):
                        c = Decimal(summ)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼|Игрок: {name1}, \n👩‍💼|Игра: Казино\n🎰|Ставка: {summ} \n📃|Результаты: Проиграли: {c2}₽ (x0) {rloser}', parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(16, 33):
                        c = Decimal(summ - summ * 0.25)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼|Игрок: {name1},\n👩‍💼|Игра: Казино\n🎰|Ставка:{summ} \n📃|Результаты: Проиграли: {c2}₽ (x0.25) {rloser}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {balance - summ * 0.75} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(34, 54):
                        c = Decimal(summ * 0.5)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼\Игрок: {name1},\n👩‍💼|Игра: Казино\n🎰|Ставка: {summ} \n📃Результаты: Проиграли: {c2}₽ (x0.5) {rloser}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.5} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(54, 62):
                        c = Decimal(summ - summ * 0.75)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼|Игрок: {name1},\n👩‍💼|Игра: Казино\n🎰|Ставка: {summ}\n📃Проиграли: {c2}₽ (x0.75) {rloser}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {balance - summ * 0.25} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(63, 73):
                        c = summ * 1
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼|Ник: {name1}, \n👩‍💼|Игра: Казино\n🎰|Ставка: {summ} \n📃Результаты: Деньги остаются при вас! {c2}₽ (x1) {rwin}',
                                               parse_mode='html')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(74, 83):
                        c = Decimal(summ * 1.25)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼|Ник: {name1},👩‍💼|Игра: Казино\n🎰|Ставка: {summ}\n📃Результаты: Выиграли {c2}₽ (x1.25) {rwin}', parse_mode='html')

                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 1.25)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(84, 90):
                        c = Decimal(summ * 1.5)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼|Ник: {name1},\n👩‍💼|Игра: Казино\n🎰|Ставка: {summ} \n📃Результаты: Выиграли {c2}₽ (x1.5) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 1.5)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(91, 96):
                        c = Decimal(summ * 1.75)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼|Ник: {name1},\n👩‍💼|Игра: Казино\n🎰|Ставка: {summ} \n📃Результаты: Выиграли {c2}₽ (x1.75) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 1.75)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(97, 102):
                        c = Decimal(summ * 2)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼|Ник: {name1},\n👩‍💼|Игра: Казино\n🎰|Ставка: {summ} \n📃Результаты: Выиграли {c2}₽ (x2) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) in range(103, 106):
                        c = Decimal(summ * 3)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼|Ник: {name1},\n👩‍💼|Игра: Казино\n🎰|Ставка: {summ} \n📃Результаты: Выиграли {c2}₽ (x3) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 3)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if int(rx) == 110:
                        c = Decimal(summ * 50)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼|Ник: {name1},\n👩‍💼|Игра: Казино\n🎰|Ставка: {summ} \n📃Результаты: Выиграли {c2}₽ (x50) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 50)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                    if int(rx) in range(107, 109):
                        c = Decimal(summ * 10)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼|Ник: {name1},\n👩‍💼|Игра: Казино\n🎰|Ставка: {summ} \n📃Результаты: Выиграли {c2}₽ (x10) {rwin}', parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 10)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                elif summ <= 1:
                    await bot.send_message(chat_id, f'{name1}, нельзя ставить отрицательное число! {rloser}',
                                           parse_mode='html')
            elif int(balance) <= int(summ):
                await bot.send_message(chat_id, f'{name1}, недостаточно средств! {rloser}', parse_mode='html')
        else:
            await bot.send_message(chat_id, f'{name1}, извини. но играть можно только каждые 5️⃣ секунд. {rloser}',
                                   parse_mode='html')
            return
            
###########################################ЧЁТНОЕ\НЕ ЧЁТНОЕ#################################
    if message.text.startswith("Нечётное"):
        msg = message
        user_id = msg.from_user.id
        chat_id = message.chat.id

        win = ['🙂', '😋', '😄', '😃']
        loser = ['😔', '😕', '😣', '😞', '😢']
        rx = random.randint(0, 120)
        rwin = random.choice(win)
        rwin2 = random.choice(win)
        rloser = random.choice(loser)

        msg = message
        name1 = message.from_user.get_mention(as_html=True)
        name = msg.from_user.last_name
        summ = int(msg.text.split()[1])
        kyb = ['🎲1', '🎲2', '🎲3', '🎲4', '🎲5', '🎲6']
        rkyb = random.choice(kyb)
        print(f"👨‍💼Игрок:{name}\n🎲Игра:Кубик поставил на нечётное: \n🎰Ставка: {summ}₽ выпало| {rkyb}")
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = round(int(balance[0]))
        period = 5
        get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
        last_stavka = f"{int(get[0])}"
        stavkatime = time.time() - float(last_stavka)
        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if rkyb in ['🎲2', '🎲4', '🎲6']:
                        c = Decimal(summ)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼 | Игрок: {name1} ,\n🎲 | Игра: Кубик\n🎰 | Ставка: {summ}₽ \n  вам выпало: {rkyb} \n📃 | Проигрыш: {c2}₽ {rloser}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if rkyb in ['🎲1', '🎲3', '🎲5']:
                        c = Decimal(summ * 2)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼 | Игрок: {name1} ,\n🎲 | Игра: Кубик\n🎰 | Ставка: {summ}₽ \n вам выпало: {rkyb} \n📃 | Выигрыш: {c2}₽ {rwin}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                elif summ <= 1:
                    await bot.send_message(chat_id, f'{name1}, нельзя ставить отрицательное число! {rloser}',
                                           parse_mode='html')
            elif int(balance) <= int(summ):
                await bot.send_message(chat_id, f'{name1}, недостаточно средств! {rloser}', parse_mode='html')
        else:
            await bot.send_message(chat_id, f'{name1}, извини. но играть можно только каждые 5️⃣ секунд. {rloser}',
                                   parse_mode='html')
            return
    if message.text.startswith("нечётное"):
        msg = message
        user_id = msg.from_user.id
        chat_id = message.chat.id

        win = ['🙂', '😋', '😄', '😃']
        loser = ['😔', '😕', '😣', '😞', '😢']
        rx = random.randint(0, 120)
        rwin = random.choice(win)
        rwin2 = random.choice(win)
        rloser = random.choice(loser)

        msg = message
        name1 = message.from_user.get_mention(as_html=True)
        name = msg.from_user.last_name
        summ = int(msg.text.split()[1])
        print(f"👨‍💼 | Игрок: {name}\n🎲 | Игра: Кубик:\n поставил на нечётное:\n🎰 | Ставка: {summ}₽ и выиграл/проиграл: {rx}")
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = round(int(balance[0]))
        period = 5
        kyb = ['🎲1', '🎲2', '🎲3', '🎲4', '🎲5', '🎲6']
        rkyb = random.choice(kyb)
        get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
        last_stavka = f"{int(get[0])}"
        stavkatime = time.time() - float(last_stavka)
        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if rkyb in ['🎲2', '🎲4', '🎲6']:
                        c = Decimal(summ)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼 | Игрок: {name1} ,\n🎲 | Игра: Кубик\n🎰 | Ставка: {summ}₽ вам выпало: {rkyb} \n📃 | Проиграли: {c2}₽ {rloser}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if rkyb in ['🎲1', '🎲3', '🎲5']:
                        c = Decimal(summ * 2)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼 | Игрок: {name1} ,\n🎲 | Игра: Кубик\n🎰Ставка: {summ}₽ вам выпало: {rkyb} \n📃 | Выиграли: {c2}$ {rwin}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                elif summ <= 1:
                    await bot.send_message(chat_id, f'{name1}, нельзя ставить отрицательное число! {rloser}',
                                           parse_mode='html')
            elif int(balance) <= int(summ):
                await bot.send_message(chat_id, f'{name1}, недостаточно средств! {rloser}', parse_mode='html')
        else:
            await bot.send_message(chat_id, f'{name1}, извини. но играть можно только каждые 5️⃣ секунд. {rloser}',
                                   parse_mode='html')
            return
    if message.text.startswith("чётное"):
        msg = message
        user_id = msg.from_user.id
        chat_id = message.chat.id

        win = ['🙂', '😋', '😄', '😃']
        loser = ['😔', '😕', '😣', '😞', '😢']
        rx = random.randint(0, 120)
        rwin = random.choice(win)
        rwin2 = random.choice(win)
        rloser = random.choice(loser)

        msg = message
        name1 = message.from_user.get_mention(as_html=True)
        name = msg.from_user.last_name
        summ = int(msg.text.split()[1])
        print(f"👨‍💼Игрок: {name} поставил на Чётное:\n⚙️Результаты|{summ}₽ и выиграл/проиграл: {rx}")
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = round(int(balance[0]))
        period = 5
        kyb = ['🎲1', '🎲2', '🎲3', '🎲4', '🎲5', '🎲6']
        rkyb = random.choice(kyb)
        get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
        last_stavka = f"{int(get[0])}"
        stavkatime = time.time() - float(last_stavka)
        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if rkyb in ['🎲2', '🎲4', '🎲6']:
                        c = Decimal(summ * 2)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼 | Игрок: {name1} ,\n🎲 | Игра: Кубик\n🎰 | Ставка: {summ}₽ вам выпало: {rkyb}\n📃 | Выигрыш: {c2}₽ {rwin}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if rkyb in ['🎲1', '🎲3', '🎲5']:
                        c = Decimal(summ)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼 | Игрок: {name1} ,\n🎲 | Игра: Кубик\n🎰 | Ставка: {summ}₽ вам выпало: {rkyb}\n📃 | Проигрыш: {c2}₽ {rloser}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                elif summ <= 1:
                    await bot.send_message(chat_id, f'{name1}, нельзя ставить отрицательное число! {rloser}',
                                           parse_mode='html')
            elif int(balance) <= int(summ):
                await bot.send_message(chat_id, f'👨‍💼 Игрок: {name1},\n👨‍💼 Игрок увас недостаточно средств! {rloser}', parse_mode='html')
        else:
            await bot.send_message(chat_id, f'{name1}, извини. но играть можно только каждые 5️⃣ секунд. {rloser}',
                                   parse_mode='html')
            return
    if message.text.startswith("Чётное"):
        msg = message
        user_id = msg.from_user.id
        chat_id = message.chat.id

        win = ['🙂', '😋', '😄', '😃']
        loser = ['😔', '😕', '😣', '😞', '😢']
        rx = random.randint(0, 120)
        rwin = random.choice(win)
        rwin2 = random.choice(win)
        rloser = random.choice(loser)

        msg = message
        name1 = message.from_user.get_mention(as_html=True)
        name = msg.from_user.last_name
        summ = int(msg.text.split()[1])
        print(f"👨‍💼 | Игрок: {name}\n🎰 | Ставка: {summ}₽ поставил на Чётное:\n 📃 | Результаты:{summ}₽ и выиграл/проиграл: {rx}")
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = round(int(balance[0]))
        period = 5
        kyb = ['🎲1', '🎲2', '🎲3', '🎲4', '🎲5', '🎲6']
        rkyb = random.choice(kyb)
        get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
        last_stavka = f"{int(get[0])}"
        stavkatime = time.time() - float(last_stavka)
        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if rkyb in ['🎲2', '🎲4', '🎲6']:
                        c = Decimal(summ * 2)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼| Игрок: {name1} ,\n🎲 | Игра: Кубик\n🎰 | Ставка: {summ}₽ вам выпало: {rkyb}\n📃 | Выигрыш: {c2}₽ {rwin}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if rkyb in ['🎲1', '🎲3', '🎲5']:
                        c = Decimal(summ)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'👨‍💼 | Игрок: {name1} ,\n🎰 | Ставка: {summ}₽ вам выпало: {rkyb}\n📃 | Проиграли: {c2}₽ {rloser}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                elif summ <= 1:
                    await bot.send_message(chat_id, f'{name1}, нельзя ставить отрицательное число! {rloser}',
                                           parse_mode='html')
            elif int(balance) <= int(summ):
                await bot.send_message(chat_id, f'{name1}, недостаточно средств! {rloser}', parse_mode='html')
        else:
            await bot.send_message(chat_id, f'{name1}, извини. но играть можно только каждые 5️⃣ секунд. {rloser}',
                                   parse_mode='html')            
            
###########################################ПЕРЕВОДЫ###########################################
    if message.text.startswith("дать наличных"):
        msg = message
        user_id = msg.from_user.id
        name = msg.from_user.last_name
        name1 = message.from_user.get_mention(as_html=True)
        user_name = message.from_user.get_mention(as_html=True)
        reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
        reply_user_id = msg.reply_to_message.from_user.id
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)

        perevod = int(msg.text.split()[2])
        perevod2 = '{:,}'.format(perevod)
        print(f"👨‍💼 | Игрок: {name1}\n⚙️ | Действие: Передача денег\n📃 | Сумма: {perevod}₽\n👨‍💼 | Игроку: {name1}")

        cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = round(int(balance[0]))
        balance2 = cursor.execute("SELECT balance from users where user_id = ?",
                                  (message.reply_to_message.from_user.id,)).fetchone()
        balance2 = round(balance2[0])

        if not message.reply_to_message:
            await message.reply("Эта команда должна быть ответом на сообщение!")
            return

        if reply_user_id == user_id:
            await message.reply_to_message.reply(f'Вы не можете передать деньги сами себе! {rloser}', parse_mode='html')
            return

        if perevod > 0:
            if balance >= perevod:
                await message.reply_to_message.reply(f'👨‍💼 | Игрок: {name1}\n⚙️ | Действие: Передача денег\n📃 | Сумма: {perevod2}₽\n👨‍💼 | Игроку: {reply_user_name} {rwin}',parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - perevod} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
                connect.commit()

            elif int(balance) <= int(perevod):
                await message.reply(f'{user_name}, недостаточно средств!  {rloser}', parse_mode='html')

        if perevod <= 0:
            await message.reply(f'{user_name}, нельзя дать отрицательное число денег! {rloser}', parse_mode='html')
            
    if message.text.startswith("Дать наличных"):
        msg = message
        user_id = msg.from_user.id
        name = msg.from_user.last_name
        name1 = message.from_user.get_mention(as_html=True)
        user_name = message.from_user.get_mention(as_html=True)
        reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
        reply_user_id = msg.reply_to_message.from_user.id
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)

        perevod = int(msg.text.split()[2])
        perevod2 = '{:,}'.format(perevod)
        print(f"👨‍💼 | Игрок: {name1}\n⚙️ | Действие: Передача денег\n📃 | Сумма: {perevod}₽\n👨‍💼 | Игроку: {name1}")

        cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = round(int(balance[0]))
        balance2 = cursor.execute("SELECT balance from users where user_id = ?",
                                  (message.reply_to_message.from_user.id,)).fetchone()
        balance2 = round(balance2[0])

        if not message.reply_to_message:
            await message.reply("Эта команда должна быть ответом на сообщение!")
            return

        if reply_user_id == user_id:
            await message.reply_to_message.reply(f'Вы не можете передать деньги сами себе! {rloser}', parse_mode='html')
            return

        if perevod > 0:
            if balance >= perevod:
                await message.reply_to_message.reply(f'👨‍💼 | Игрок: {name1}\n⚙️ | Действие: Передача денег\n📃 | Сумма: {perevod2}₽\n👨‍💼 | Игроку: {reply_user_name} {rwin}',parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - perevod} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
                connect.commit()

            elif int(balance) <= int(perevod):
                await message.reply(f'{user_name}, недостаточно средств!  {rloser}', parse_mode='html')

        if perevod <= 0:
            await message.reply(f'{user_name}, нельзя дать отрицательное число денег! {rloser}', parse_mode='html')                                               
            
    if message.text.startswith("перевести на карту"):
        msg = message
        photo = open('dat.jpg', 'rb')
        user_id = msg.from_user.id
        name = msg.from_user.last_name
        name1 = message.from_user.get_mention(as_html=True)
        user_name = message.from_user.get_mention(as_html=True)
        reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
        reply_user_id = msg.reply_to_message.from_user.id
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)

        perevod = int(msg.text.split()[3])
        perevod2 = '{:,}'.format(perevod)
        print(f"👨‍💼 | Игрок: {name1}\n⚙️ | Действие: Перевод денег\n📃 | Сумма: {perevod}₽\n👨‍💼 | Игроку: {name1}")

        cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
        bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
        bank = round(int(bank[0]))
        bank2 = cursor.execute("SELECT bank from users where user_id = ?",
                                  (message.reply_to_message.from_user.id,)).fetchone()
        bank2 = round(bank2[0])

        if not message.reply_to_message:
            await message.reply("Эта команда должна быть ответом на сообщение!")
            return

        if reply_user_id == user_id:
            await message.reply_to_message.reply(f'Вы не можете перевести деньги сами себе! {rloser}', parse_mode='html')
            return

        if perevod > 0:
            if bank >= perevod:
                await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f'👨‍💼 | Игрок: {name1}\n⚙️ | Действие: Перевод денег\n📃 | Сумма: {perevod2}₽\n👨‍💼 | Игроку: {reply_user_name} {rwin}',parse_mode='html')
                cursor.execute(f'UPDATE users SET bank = {bank - perevod} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET bank = {bank2 + perevod} WHERE user_id = "{reply_user_id}"')
                connect.commit()

            elif int(bank) <= int(perevod):
                await message.reply(f'{user_name}, недостаточно средств! Положите деньги на карту, чтобы выполнить перевод! {rloser}', parse_mode='html')

        if perevod <= 0:
            await message.reply(f'{user_name}, нельзя перевести отрицательное число! {rloser}', parse_mode='html')

    if message.text.startswith("Перевести на карту"):
        msg = message
        photo = open('dat.jpg', 'rb')
        user_id = msg.from_user.id
        name = msg.from_user.last_name
        name1 = message.from_user.get_mention(as_html=True)
        user_name = message.from_user.get_mention(as_html=True)
        reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
        reply_user_id = msg.reply_to_message.from_user.id
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)

        perevod = int(msg.text.split()[3])
        perevod2 = '{:,}'.format(perevod)
        print(f"👨‍💼 | Игрок: {name1}\n⚙️ | Действие: Перевод денег\n📃 | Сумма: {perevod}₽\n👨‍💼 | Игроку: {name1}")

        cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
        bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
        bank = round(int(bank[0]))
        bank2 = cursor.execute("SELECT bank from users where user_id = ?",
                                  (message.reply_to_message.from_user.id,)).fetchone()
        bank2 = round(bank2[0])

        if not message.reply_to_message:
            await message.reply("Эта команда должна быть ответом на сообщение!")
            return

        if reply_user_id == user_id:
            await message.reply_to_message.reply(f'Вы не можете перевести деньги сами себе! {rloser}', parse_mode='html')
            return

        if perevod > 0:
            if bank >= perevod:
                await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f'👨‍💼 | Игрок: {name1}\n⚙️ | Действие: Перевод денег\n📃 | Сумма: {perevod2}₽\n👨‍💼 | Игроку: {reply_user_name} {rwin}',parse_mode='html')
                cursor.execute(f'UPDATE users SET bank = {bank - perevod} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET bank = {bank2 + perevod} WHERE user_id = "{reply_user_id}"')
                connect.commit()

            elif int(bank) <= int(perevod):
                await message.reply(f'{user_name}, недостаточно средств! Положите деньги на карту, чтобы выполнить перевод! {rloser}', parse_mode='html')

        if perevod <= 0:
            await message.reply(f'{user_name}, нельзя перевести отрицательное число! {rloser}', parse_mode='html')
           
            
            
###########################################БАНК###########################################
    # bank
    if message.text.lower() in ["Карта", "карта"]:
        msg = message
        chat_id = message.chat.id
        name1 = message.from_user.get_mention(as_html=True)
        user_name = msg.from_user.full_name
        user_id = msg.from_user.id
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        bank = int(bank[0])
        balance2 = '{:,}'.format(balance)
        bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
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
        banks = ['🏪', '🏦', '🏛']
        rbanks = random.choice(banks)
        await bot.send_message(message.chat.id,
                               f'🤵 | Игрок:{user_name}\n🏦 | Банковский счёт \n💵 | Сумма наличных: {balance2}₽\n💳 | Сумма на карте: {bank2}₽')

    if message.text.startswith("Положить на карту"):
        msg = message
        chat_id = message.chat.id
        user_id = msg.from_user.id
        name = msg.from_user.last_name
        user_name = message.from_user.get_mention(as_html=True)

        bank_p = int(msg.text.split()[3])
        print(f"{name} положил на карту: {bank_p}")

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
                await bot.send_message(message.chat.id, f'{user_name}, вы успешно положили на карту {bank2}₽ {rwin}',
                                      parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - bank_p} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET bank = {bank + bank_p} WHERE user_id = "{user_id}"')
                connect.commit()

            elif int(balance) < int(bank_p):
                await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}',
                                       parse_mode='html')

        if bank_p <= 0:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, нельзя положить на карту отрицательное число! {rloser}',
                                   parse_mode='html')
    if message.text.startswith("положить на карту"):
        msg = message
        chat_id = message.chat.id
        user_id = msg.from_user.id
        name = msg.from_user.last_name
        user_name = message.from_user.get_mention(as_html=True)

        bank_p = int(msg.text.split()[3])
        print(f"{name} положил на карту: {bank_p}")

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
                await bot.send_message(message.chat.id, f'{user_name}, вы успешно положили на карту {bank2}₽ {rwin}',
                                       parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - bank_p} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET bank = {bank + bank_p} WHERE user_id = "{user_id}"')
                connect.commit()

            elif int(balance) < int(bank_p):
                await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}',
                                       parse_mode='html')

        if bank_p <= 0:
            await bot.send_message(message.chat.id,
                                   f'{user_name}, нельзя положить на карту отрицательное число! {rloser}',
                                   parse_mode='html')

    if message.text.startswith("Снять с карты"):
        msg = message
        chat_id = message.chat.id
        user_id = msg.from_user.id
        name = msg.from_user.last_name
        user_name = message.from_user.get_mention(as_html=True)

        bank_s = int(msg.text.split()[3])
        print(f"{name} снял с карты: {bank_s}")

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
                await bot.send_message(message.chat.id,
                                       f'{user_name}, вы успешно сняли с карты {bank2}₽ {rwin}',
                                       parse_mode='html')
                cursor.execute(f'UPDATE users SET bank = {bank - bank_s} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + bank_s} WHERE user_id = "{user_id}"')
                connect.commit()

            elif int(bank) < int(bank_s):
                await bot.send_message(message.chat.id,
                                       f'{user_name}, недостаточно средств на банковском счету! {rloser}',
                                       parse_mode='html')                                                                                                                                                                                                                                                                                                                    
    if message.text.startswith("снять с карты"):
        msg = message
        chat_id = message.chat.id
        user_id = msg.from_user.id
        name = msg.from_user.last_name
        user_name = message.from_user.get_mention(as_html=True)

        bank_s = int(msg.text.split()[3])
        print(f"{name} снял с карты: {bank_s}")

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
                await bot.send_message(message.chat.id,
                                       f'{user_name}, вы успешно сняли с карты {bank2}₽ {rwin}',
                                       parse_mode='html')
                cursor.execute(f'UPDATE users SET bank = {bank - bank_s} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET balance = {balance + bank_s} WHERE user_id = "{user_id}"')
                connect.commit()

            elif int(bank) < int(bank_s):
                await bot.send_message(message.chat.id,
                                       f'{user_name}, недостаточно средств на банковском счету! {rloser}',
                                       parse_mode='html')

        if bank_s <= 0:
            await bot.send_message(message.chat.id, f'{user_name}, нельзя снять с карты отрицательное число! {rloser}',
                                   parse_mode='html')

    if message.text.lower() in ["помощь", "Помощь"]:
       msg = message 
       chat_id = message.chat.id
       user_name = message.from_user.get_mention(as_html=True)
       await bot.send_message(message.chat.id, f"✨ | Мои команды:\n💸 | Б/Баланс\n🪨✂️📄 | Игра\n💳 | Положить на карту [сумма]\n💳 | Снять с карты [сумма]\n💳 | Карта - узнать всю информацию о вашем счёте\n🎰 | Казино [ставка]\n✅ | Перевести [сумма] - чтобы перевести деньги надо положить их на карту\n💵 | Дать наличных [сумма]\n🎲 | Чётное/Нечётное [сумма]", parse_mode='html')        
    
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)                         
