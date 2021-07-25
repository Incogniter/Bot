import constants as keys
from telegram.ext import *
import Response as R

print("the bot as started!.......")

# to start the bot


def start_command(update, context):
    update.message.reply_text('type something to get started')

# if help needed


def help_command(update, context):
    update.message.reply_text('if any help ask google')


def cancel_command(update, context):
    update.message.reply_text('shut downing....!!')


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_response(text)

    update.message.reply_text(response)

# if error


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("cancel", cancel_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling(1)
    updater.idle()


main()
