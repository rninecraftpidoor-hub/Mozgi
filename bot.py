from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.environ["BOT_TOKEN"]
WEBAPP_URL = "https://rninecraftpidoor-hub.github.io/Cazik/"

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    user_id = update.effective_user.id
    chat_type = update.effective_chat.type

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            text="🎮 Играть",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )]
    ])

    # Если команда в ЛС — просто открываем игру
    if chat_type == "private":
        await update.message.reply_text(
            "Запусти мини-игру 👇",
            reply_markup=keyboard
        )
        return

    # Если команда в группе — пытаемся написать в ЛС
    try:
        await context.bot.send_message(
            chat_id=user_id,
            text="🎮 Вот твоя мини-игра:",
            reply_markup=keyboard
        )

        await update.message.reply_text(
            "Я отправил игру тебе в личные сообщения 📩"
        )

    except:
        await update.message.reply_text(
            "Напиши мне в ЛС /start, чтобы я мог отправлять тебе игру:\n"
            "https://t.me/Cazino"
        )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("play", play))
app.add_handler(CommandHandler("start", play))

app.run_polling()
