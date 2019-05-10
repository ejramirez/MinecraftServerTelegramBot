import logging, json

class TelegramChatInstanceJSON:
    chatId = None # Unique Integer
    folder = None # Folder holding chat JSONs
    fileName = None # String file
    completeFileName = None # chatId + filename.json

    # Constructor
    def __init__(self, chatId, folder, filename):
        self.chatId = chatId
        self.folder = folder
        self.fileName = filename
        self.completeFileName = "{}/{}_{}.json".format(self.folder, self.chatId, self.fileName);

    # Class Methods
    def getInstance(self):
        with open(self.completeFileName, 'r') as f:
            json_dict = json.load(f)
        return json_dict

    def updateInstance(self):
        with open(self.completeFileName, 'w') as f:
            f.write(json.dumps(self.completeFileName, indent=4))

    # Getters and Setters
    def getChatId(self):
        return self.chatId

    def setChatId(self, chatId):
        self.chatId = chatId

    def getFolder(self):
        return self.folder

    def setFolder(self, folder):
        self.folder = folder

    def getFileName(self):
        return self.fileName

    def setFileName(self, fileName):
        self.fileName = fileName

    def getCompleteFileName(self):
        return self.completeFileName

    def setCompleteFileName(self, completeFileName):
        self.completeFileName = completeFileName