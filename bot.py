import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

# 🛠 Получаем токен из переменных окружения (Railway → Variables)
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN не найден! Убедись, что переменная установлена в Railway.")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    # Создаём кнопку
    kb = InlineKeyboardBuilder()
    kb.button(text="Открыть в приложении", url="https://ibb.co/NdYtmZz6")
    kb.adjust(1)

    text = (
        "✨ *Welcome to Portals!*\n"
        "Discover, trade, and collect unique digital gifts in our marketplace.\n"
        "_Start exploring now!_"
    )

    photo_url = "https://i.ibb.co/ZpTGYWC6/IMG-7434.jpg"

    await message.answer_photo(
        photo=photo_url,
        caption=text,
        reply_markup=kb.as_markup(),
        parse_mode="Markdown"
    )

async def main():
    print("✅ Bot is running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
