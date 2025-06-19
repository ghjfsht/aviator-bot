from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio
import os
from scraper import get_latest_coef

TOKEN = os.getenv("BOT_TOKEN")

async def start(update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! /watch deb yozing, men 2x dan yuqori koeffitsiyentni kutaman.")

async def watch(update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id, "Kuzatish boshlandi...")
    while True:
        try:
            coef = get_latest_coef()
            print(f"Koeffitsiyent: {coef}")
        except Exception as e:
            await context.bot.send_message(chat_id, f"Xatolik: {e}")
            break
        if coef >= 2.0:
            await context.bot.send_message(chat_id, f"🔔 Diqqat! {coef}x chiqdı!")
            break
        await asyncio.sleep(15)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("watch", watch))
app.run_polling()