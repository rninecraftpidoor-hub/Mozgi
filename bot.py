from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Токен берётся ТОЛЬКО из GitHub Secrets
TOKEN = os.getenv("BOT_TOKEN")

# short name игры из BotFather (/newgame)
GAME_SHORT_NAME = "cazik_game"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Напиши /play чтобы запустить мини-игру 🎮"
    )

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_game(
        chat_id=update.effective_chat.id,
        game_short_name=GAME_SHORT_NAME
    )

def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN не найден в Secrets")

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("play", play))
    app.run_polling()

if __name__ == "__main__":
    main()
