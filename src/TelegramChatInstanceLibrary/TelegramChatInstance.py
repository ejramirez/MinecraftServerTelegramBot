import logging, json

class TelegramChatInstance:
    dataType = None
    chatId = None

    def __init__(self, dataType, chatId):
        self.dataType = None
        self.chatId = None

    def getDataType(self):
        return self.dataType

    def setDataType(self, dataType):
        self.dataType = dataType

    def getChatId(self):
        return self.chatId

    def setChatId(self, chatId):
        self.chatId = chatId

    def create(self):
        return

    def read(self):
        return

    def update(self):
        return

    def delete(self):
        return