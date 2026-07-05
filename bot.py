import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.request import HTTPXRequest

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN", "PASTE_YOUR_BOT_TOKEN_HERE")  
CHANNEL_LINK = "https://t.me/FOREXEMIRE_UASSS"
ADMIN_LINK = "https://t.me/asifnawaz3646"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    
    keyboard = [
        [InlineKeyboardButton("📊 SUBSCRIBE 🤝", url=CHANNEL_LINK)],
        [InlineKeyboardButton("📈 FREE SIGNALS 📊", url=CHANNEL_LINK)],
        [InlineKeyboardButton("💬 DM ME", url=ADMIN_LINK)]
    ]
    
    text = (
        f"Hi, {user_name} 👋\n\n"
        "😔 <b>Are you in LOSS?</b>\n"
        "📉 Tired of blowing accounts and fake signals?\n\n"
        "<b>Join Now GOLDSNIPER</b> - 9 Years of Pro Forex Trading\n"
        "Recover accounts and turn them into profits.\n"
        "High Accuracy daily Signals with proper SL & TP.\n\n"
        "Stop gambling. Start trading with a professional 👇\n\n"
        f"🔔 {CHANNEL_LINK}\n"
        f"🔔 {CHANNEL_LINK}\n"
        f"🔔 {CHANNEL_LINK}\n\n"
        "❗ <b>IMPORTANT:</b>\n"
        "After you subscribe, I'll tell you more about how you can start making money with trading alongside me."
    )
    
    await update.message.reply_text(
        text, 
        reply_markup=InlineKeyboardMarkup(keyboard), 
        parse_mode='HTML',
        disable_web_page_preview=True
    )

def main():
    request = HTTPXRequest(connect_timeout=30.0, read_timeout=30.0)
    
    app = ApplicationBuilder().token(BOT_TOKEN).request(request).build()
    
    app.add_handler(CommandHandler("start", start))
    
    print("Bot running on Polling... ✅")
    app.run_polling(allowed_updates=Update.ALL_TYPES)  # yahi final line hai

if __name__ == "__main__":
    main()
