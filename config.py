
# def createConfigFileMode():
#     configFile = open("BinanceBot.txt", "w")
#     print("Config file created, it's currently empty")
#
# def readConfigFIleMode():
#     configFile = open("BinanceBot.txt", "r")
#     if configFile.mode == 'r':
#         firstLine = configFile.readline()
#         api = True if 'A' in firstLine else False
#         snapshot = True if 'S' in firstLine else False
#         configState = {"api" = api, "snapshot" = snapshot}
#     else:
#         print("couldn't open the file")
#         return (-1)    #snapshot is present
#
#
# def checkConfig():
#     if os.path.isFile("BinanceBot.txt")
#         print("config file found")
#         configState = readConfigFIleMode()
#         if configState == -1:
#             print("error")
#         else:
#             if configState["api"]:
#                 api_key = configFile.readline(4)
#                 api_secret = configFile.readline(5)
#             if configState["snapshot"]:
#                 #do something
