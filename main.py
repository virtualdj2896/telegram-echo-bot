import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

# .env fayldan tokenni yuklash
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Echo handler funksiyasi
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text(update.message.text)

# Asosiy botni ishga tushirish
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
