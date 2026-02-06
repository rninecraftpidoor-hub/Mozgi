from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os

TOKEN = os.environ["BOT_TOKEN"]

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("PLAY CALLED", update.effective_chat.id)

    if not update.message:
        print("NO MESSAGE OBJECT")
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

# Ловим ВСЕ сообщения в группе и проверяем текст вручную
async def group_listener(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text.lower()

    if text.startswith("/play"):
        await play(update, context)

app = ApplicationBuilder().token(TOKEN).build()

# Команды
app.add_handler(CommandHandler("start", play))
app.add_handler(CommandHandler("play", play))

# Фикс для групп
app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.GROUPS, group_listener))

app.run_polling()
