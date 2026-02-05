from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.environ["BOT_TOKEN"]

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            text="🎮 Играть",
            web_app=WebAppInfo(url="https://rninecraftpidoor-hub.github.io/Cazik/")
        )]
    ])

    await update.message.reply_text(
        "Запусти мини-приложение 👇",
        reply_markup=keyboard
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("play", play))
app.add_handler(CommandHandler("start", play))

app.run_polling(allowed_updates=Update.ALL_TYPES)
