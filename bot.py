import os
import asyncio
import traceback
from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

# 🔑 Берем токен из переменных окружения (Render → Environment Variables)
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN не найден! Убедись, что переменная установлена в Render.")

# Инициализация бота
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# 📩 Обработка команды /start
@dp.message(CommandStart())
async def start(message: types.Message):
    kb = InlineKeyboardBuilder()
    kb.button(text="Открыть в приложении", url="https://trepall.github.io/Portal-market/")
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

# 🌐 Мини веб-сервер, чтобы Render не «засыпал»
async def handle_root(request):
    return web.Response(text="Portals bot is alive!")

async def start_web_server():
    app = web.Application()
    app.add_routes([web.get("/", handle_root)])

    port = int(os.environ.get("PORT", 10000))
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    print(f"🌐 Web server running on port {port}")
    await site.start()

# ♻️ Бесконечный цикл с перезапуском при ошибке
async def run_bot():
    while True:
        try:
            print("✅ Bot is running...")
            await dp.start_polling(bot)
        except Exception as e:
            print("⚠️ Ошибка в работе бота:", e)
            traceback.print_exc()
            print("♻️ Перезапуск через 5 секунд...")
            await asyncio.sleep(5)

# 🚀 Запуск обоих процессов: Telegram + web-сервер
async def main():
    await asyncio.gather(start_web_server(), run_bot())

if __name__ == "__main__":
    asyncio.run(main())
