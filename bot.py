from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)
import os

# === НАСТРОЙКИ ===
TOKEN = os.environ.get("BOT_TOKEN")
GAME_URL = "https://rninecraftpidoor-hub.github.io/Cazik/"

# === КОМАНДЫ ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "👋 Привет!\n\n"
        "🎮 Это мини-игра Cazik\n"
        "Напиши /play чтобы открыть меню"
    )
    await update.message.reply_text(text)

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎮 Играть", url=GAME_URL)],
        [
            InlineKeyboardButton("🛒 Магазин", callback_data="shop"),
            InlineKeyboardButton("👤 Авторы", callback_data="authors")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Выбери действие 👇",
        reply_markup=reply_markup
    )

# === ЗАПУСК БОТА ===
def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN не найден в переменных окружения")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("play", play))

    print("🤖 Бот запущен")
    app.run_polling()

if __name__ == "__main__":
    main()
