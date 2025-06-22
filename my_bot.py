from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    ContextTypes, filters
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Hey {update.effective_user.first_name} 0! Welcome to Skill Zenic 💻✨")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.lower()

    if user_text == "ok":
        await update.message.reply_text("Great! Let's move ahead. 🚀")
    elif user_text == "hi":
        await update.message.reply_text("Hello there! 👋")
    elif user_text == "do you love me":
        await update.message.reply_text("Of course I do! ❤️ (In a bot way 🤖)")
    elif user_text == "help":
        await update.message.reply_text("How can I assist you? You can say 'hi', 'ok', or 'do you love me'.")
    elif user_text == "hey":
        await update.message.reply_text("Hey! How's it going? 😊")
    elif user_text == "what's my name":
        user_name = update.effective_user.first_name
        await update.message.reply_text(f"Your name is {user_name}!")
    elif user_text == "love you":
        await update.message.reply_text("I love you too! 💖 Bngru")
    elif user_text == "who are you":
        await update.message.reply_text("Neku enduku ra pottoda!!")
    elif user_text == "bye":
        await update.message.reply_text("Goodbye! See you next time! 👋")
    else:
        await update.message.reply_text("I'm not sure how to respond to that. Try saying 'hi', 'ok', or 'do you love me'.")

app = ApplicationBuilder().token("7605731387:AAHNzuM7jhidwzNT5x7FR-uXUoQi3I3DCfA").build()

# Command handler
app.add_handler(CommandHandler("start", start))

# Message handler for all texts
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot is running... 🚀")
app.run_polling()
