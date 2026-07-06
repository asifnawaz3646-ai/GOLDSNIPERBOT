import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.request import HTTPXRequest

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable nahi mila!")

CHANNEL_LINK = "https://t.me/FOREXEMIRE_UASSS"
ADMIN_LINK = "https://t.me/XAUUSBLOWPIPS"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    keyboard = [
        [InlineKeyboardButton("📊 SUBSCRIBE 🤝", url=CHANNEL_LINK)],
        [InlineKeyboardButton("📈 FREE SIGNALS 📊", url=CHANNEL_LINK)],
        [InlineKeyboardButton("💬 DM ME", url=ADMIN_LINK)]
    ]
    text = (
        f"Hi, {user_name} 👋\n\n"
        "😔 <b>Are you in LOSS ?</b>\n"
        "📉 Tired of blowing accounts ??\n\n"
        "<b>Join Now GOLDSNIPER</b> - \n"
        
        "Start trading with a professional 👇\n\n"
       
        f"🔔 {CHANNEL_LINK}\n"

        
        "❗ <b>IMPORTANT:</b>\n"
        "Subscribe and make profits with me."
    )
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='HTML', disable_web_page_preview=True)

def main():
    request = HTTPXRequest(connect_timeout=30.0, read_timeout=30.0)
    app = ApplicationBuilder().token(BOT_TOKEN).request(request).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot running on Polling... ✅")
    # YE LINE SABSE IMPORTANT HAI
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
