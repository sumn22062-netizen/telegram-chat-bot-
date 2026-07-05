from ai_helper import analyze_message

import os 
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
load_dotenv()
TOKEN= os.getenv("TELEGRAM_BOT_TOKEN")


async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "hello Rishabh Assistant is Here"
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    receviced_text = update.message.text
    
    analysis = analyze_message(receviced_text)
    

    if analysis.category == "expense":
        reply = (
            f"💰 **Expense Detected!**\n"
            f"• Item: {analysis.item_name}\n"
            f"• Amount: ₹{analysis.amount}"
        )
        await update.message.reply_text(reply, parse_mode="Markdown")
        
    elif analysis.category == "note":
        reply = (
            f"📝 **Note Saved!**\n"
            f"• Summary: {analysis.summary}"
        )
        await update.message.reply_text(reply, parse_mode="Markdown")
        
    else:
        await update.message.reply_text(
            "🤖 Main aapke messages ko scan kar raha hoon. "
            "Aap mujhe apna expense (e.g. '₹200 pizza') ya note (e.g. 'yaad rakhna kal gym jana hai') bhej sakte hain!"
        )
    

if __name__ == '__main__': 

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    app.run_polling()