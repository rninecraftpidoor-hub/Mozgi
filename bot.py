from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.environ["BOT_TOKEN"]

URL = "https://rninecraftpidoor-hub.github.io/Cazik/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
await send_game(update)

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
await send_game(update)

async def send_game(update: Update):
keyboard = InlineKeyboardMarkup([
[InlineKeyboardButton(
text="🎮 Играть",
web_app=WebAppInfo(url=URL)
)]
])

await update.message.reply_text(
    "Запусти мини-приложение 👇",
    reply_markup=keyboard
)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("play", play))

app.run_polling()
