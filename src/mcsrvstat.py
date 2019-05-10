import logging, json, requests

with open("./bot_properties.json", "r") as f:
    properties_dict = json.load(f)
mcSvrStatEndpoint = properties_dict["resources"]["mcsrvstat_endpoint"]

instance = None;

# Bot Functions
def start(bot, update):
    return

# 73.176.137.243
def getJSON(bot, update, args):
    if args:
        ip = args[0]
        r = requests.get(mcSvrStatEndpoint.format(ip))
        bot.send_message(chat_id=update.message.chat_id, text=r.json(), reply_to_message_id=update.message.message_id)
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Empty Argument!", reply_to_message_id=update.message.message_id)

def isOnline(bot, update, args):
    if args:
        ip = args[0]
        r = requests.get(mcSvrStatEndpoint.format(ip))
        rJson = r.json()
        serverStatus = rJson["online"]
        statusText = "online" if serverStatus else "offline"
        messageText = "{} is {}.".format(ip, statusText)
        bot.send_message(chat_id=update.message.chat_id, text=messageText, reply_to_message_id=update.message.message_id)
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Empty Argument!", reply_to_message_id=update.message.message_id)

def getPlayerList(bot, update, args):
    if args:
        ip = args[0]
        r = requests.get(mcSvrStatEndpoint.format(ip))
        rJson = r.json()
        if rJson["players"]["list"]:
            pListArr = []
            pList = rJson["players"]["list"]
            for player in pList:
                pListArr.append(player)
            message = '/n'.join(pListArr)
            bot.send_message(chat_id=update.message.chat_id, text=message, reply_to_message_id=update.message.message_id)
        else:
            bot.send_message(chat_id=update.message.chat_id, text="No Players Online!", reply_to_message_id=update.message.message_id)
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Empty Argument!", reply_to_message_id=update.message.message_id)