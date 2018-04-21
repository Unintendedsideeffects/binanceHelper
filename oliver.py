import binance
import orders
import re
import os.path
import pprint
import math


# binanceClient = Client(api_key = "", api_secret="")
acceptedChoice = 'ETH', 'BTC'



choice = input('ETH, BTC ? \n')
while choice not in acceptedChoice:
    choice = input('retry')

objective = input('Objective? \n')
while objective <= 0:
    objective = input(retry)



# order = binanceClient.create_test_order()
