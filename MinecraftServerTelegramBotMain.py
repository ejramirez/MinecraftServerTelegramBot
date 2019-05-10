import logging, json
from src.mcsrvstat import getJSON, isOnline, getPlayerList
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

isProdEnvironment = False
loggingLevel = logging.INFO if isProdEnvironment else logging.DEBUG
logFileName = "MinecraftServerTelegramBot.log" if isProdEnvironment else "MinecraftServerTelegramBot_Debug.log"

# Enable logging
logging.basicConfig(filename=logFileName,
                    filemode="a",
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt="%H:%M:%S", 
                    level=loggingLevel)
logging.info("Running MinecraftServerTelegramBot...")
logging = logging.getLogger("MinecraftServerTelegramBot")

# Getting bot token
with open('bot_properties.json' ,'r') as f:
    properties_dict = json.load(f)
bot_token = properties_dict["credentials"]["bot_token"] if isProdEnvironment else properties_dict["credentials"]["devl_bot_token"]

def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="TODO Help Menu")

def error(bot, update):
    logging.warning('Bot "%s" casued error "%s"', bot, update.error)

def main():
    logging.info("Starting Bot...")

    updater = Updater(bot_token)

    dp = updater.dispatcher

    # Command Handlers
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("json", getJSON, pass_args=True))
    dp.add_handler(CommandHandler("check", isOnline, pass_args=True))
    dp.add_handler(CommandHandler("players", getPlayerList, pass_args=True))

    # Message Handlers

    # Error Handler
    dp.add_error_handler(error)

    # Start Bot
    updater.start_polling()
    logging.info("Bot Started!")

    updater.idle()

if __name__  == '__main__':
    main()