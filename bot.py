from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, ChatJoinRequest, InlineKeyboardMarkup, InlineKeyboardButton as ib
from logging import basicConfig

basicConfig()

bot = Bot(token="6930280525:AAGp3ndEd2F4-hs-AFuET6c2vNhHBcs9vyc", parse_mode="HTML")
dp = Dispatcher(bot)

@dp.chat_join_request_handler()
async def join(request: ChatJoinRequest):
    await request.approve()

@dp.message_handler(commands="start")
async def start(m: Message):
	await m.answer(f"Привет, {m.from_user.get_mention()}")

if __name__ == "__main__":
	executor.start_polling(dp)