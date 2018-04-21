# from orders import binanceClient
from binance.client import Client

binanceClient = Client(api_key = "", api_secret="")

def printOpenOrders(request):

    allOpenOrders = binanceClient.get_open_orders(symbol = request)
    openOrderNumber = 1
    for openOrder in allOpenOrders:
        # print(openOrder.keys()
        print("{}{}{}".format("Order number ", openOrderNumber, ":"))
        print("{}{}{}".format(openOrder["type"], " ", openOrder["side"]))
        print("{}{}".format("Pair: " , openOrder["symbol"]))
        print("{}{}".format("Price: " ,openOrder["price"]))
        print("{}{}".format("Full order quantity: " ,openOrder["origQty"]))
        if (openOrder["executedQty"] != "0.00000000"):
            print("{}{}".format("Filled: " ,openOrder["executedQty"]))
            print("{}{}".format("Percentage filled: ", calculateFilledAmount(openOrder, 2)))
        openOrderNumber +=1
        print("\n")


def separatePair(pair):
    basePair = pair[-3:]
    if basePair == 'SDT':
        basePair = 'USTD'
    tradePair = pair.replace(basePair, "")
    pair = tradePair + "/" + basePair
    nicePair = {'pair': pair, 'tradePair': tradePair, 'basePair': basePair}
    return nicePair

def printRecentTrades(symbol, number=None):
# The magic number is 500 trades, r
    nicePair = separatePair(symbol)
    allTrades = binanceClient.get_my_trades(symbol = symbol)
    tradeNumber = 1

    for trade in reversed(allTrades):
        if (number !=None and tradeNumber == number+1):
            return
        else:
            if(trade["isBuyer"]):
                type = "BUY"
            else:
                type = "SELL"

            if(trade["isMaker"]): #Not sure if this really means is a market order
                #Confirmed, not
                #TODO
                type = 'LIMIT ' + type
            else:
                type = 'MARKET ' + type
            print("\n")
            print("{}{}{}{}".format("Trade number ", tradeNumber, ":", "\n"))
            print(type)
            print("{}{}".format("Pair: ", nicePair['pair']))
            print("{}{}{}{}".format("Price: ", trade["price"], " ", nicePair["basePair"]))
            print("{}{}{}{}".format("Quantity: ", trade["qty"], " ", nicePair["tradePair"]))
            total = format(float(trade["price"])*(float(trade["qty"])), '.5f')
            print("{}{}{}{}".format("Total: ", total, " ",  nicePair['basePair']))
            # print("\n")

        tradeNumber += 1


printRecentTrades('NEOETH', 5)
