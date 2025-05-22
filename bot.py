from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
import os

message_counts = {}

def count_messages(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    username = update.effective_user.username or update.effective_user.first_name

    if user_id in message_counts:
        message_counts[user_id]["count"] += 1
    else:
        message_counts[user_id] = {"count": 1, "username": username}

    count = message_counts[user_id]["count"]
    update.message.reply_text(f"{username}, you've sent {count} messages.")

def main():
    TOKEN = os.getenv("BOT_TOKEN")
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, count_messages))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
