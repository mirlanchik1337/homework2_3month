from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from os import getenv


load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(
            f"Hello {message.from_user.full_name}\n"
            f"пока что все ))))))))))))))))))))))))"
                )


@dp.message_handler()
async def start(message: types.Message):
    print(message)
    await message.answer(
        message.text
    )

executor.start_polling(dp)