from aiogram import Bot, Dispatcher, types, executor
from asyncio import sleep

bot = Bot('Token')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def on_message(message: types.Message):
    await bot.send_message(message.from_user.id, f'hi, {message.from_user.username}! Start game..')
    await sleep(1)

    bot_data = await bot.send_dice(message.from_user.id)
    bot_data = bot_data['dice']['value']
    await sleep(5)

    user_data = await bot.send_dice(message.from_user.id)
    user_data = user_data['dice']['value']
    await sleep(5)

    if bot_data > user_data:
        await bot.send_message(message.from_user.id, 'You are lose!')
    elif bot_data < user_data:
        await bot.send_message(message.from_user.id, 'You are won!')
    else:
        await bot.send_message(message.from_user.id, 'Draw!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
