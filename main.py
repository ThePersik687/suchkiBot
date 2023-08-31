from aiogram import Bot, Dispatcher, executor, types
from config import startCommand, helpCommand

ma_shluha_tupogolovaya_photo = ["https://i.imgur.com/huvFVMV.jpg", "https://i.imgur.com/BFnD8XZ.jpg", "https://i.imgur.com/Qyl5tsj.jpg",
'https://i.imgur.com/IpMOvCe.jpg', 'https://i.imgur.com/BfGr8Fg.jpg', 'https://i.imgur.com/UGBXTe4.jpg', 'https://i.imgur.com/8QpmUSv.jpg',
'https://i.imgur.com/gPEuauC.jpg','https://i.imgur.com/Mgtgk20.jpg', 'https://i.imgur.com/V8t1Pti.jpg']

ol_photo = ['https://i.imgur.com/nzQeGIO.jpg', 'https://i.imgur.com/uDL4w05.jpg', 'https://i.imgur.com/9KfolJb.jpg', 'https://i.imgur.com/mBe3x0i.jpg']

ma_bars_photo = ['https://i.imgur.com/S7w6OsV.jpg', 'https://i.imgur.com/3dm8dBF.jpg']


TOKEN_API = ''

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def Starter(_):
    print('Бот успешно запущен.')



@dp.message_handler(commands=['start'])
async def StartComm(message: types.message):
    await message.answer(startCommand, parse_mode='HTML')
    await message.delete()

@dp.message_handler(commands=['help'])
async def HelpComm(message: types.message):
    await message.answer(helpCommand, parse_mode='HTML')
    await message.delete()

@dp.message_handler(commands=['anna'])
async def anna(message: types.message):
    await bot.send_photo(chat_id=message.from_user.id, photo='https://i.imgur.com/yQa45Cq.jpg')   #анна с
    await bot.send_photo(chat_id=message.from_user.id, photo='https://i.imgur.com/6RSYBeU.jpg')
    await bot.send_photo(chat_id=message.from_user.id, photo='https://i.imgur.com/LCMW96W.jpg')
    await message.answer('оцени от 1 до 10')
    await message.delete()

@dp.message_handler(commands=['marina'])
async def marina_shluha(message: types.message):
     for i in ma_shluha_tupogolovaya_photo:
        await bot.send_photo(message.from_user.id, photo=i)
     await message.answer('оцени от 1 до 10')
     await message.delete()

@dp.message_handler(commands=['olga'])
async def olga(message: types.message):
    for i in ol_photo:
        await bot.send_photo(message.from_user.id, photo=i)
    await message.answer('оцени от 1 до 10')
    await message.delete()

@dp.message_handler(commands=['mashka'])
async def mashaB(message: types.message):
    for i in ma_bars_photo:
       await bot.send_photo(message.from_user.id, photo=i)
    await message.answer('оцени от 1 до 10')
    await message.delete()

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=Starter)