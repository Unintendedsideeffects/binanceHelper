from binance.client import Client
import re
import os.path
import pprint
import math
import visualization
binanceClient = Client(api_key = "", api_secret="")
acceptedOptions = 'ETH', 'BTC' 'USDT'


def calculateFilledAmount(openOrder, i=None):
    filledPercentage = ((float)(openOrder["executedQty"])/(float)(openOrder["origQty"]))*100
    filledPercentage = format(filledPercentage, '.2f')
    if i is not None:
        filledPercentage = "{}{}".format(filledPercentage, "%")
    return filledPercentage



def getPriceFromTicker(ticker, destinationTicker = None):
    acceptedDT = 'USDT, ETH, BTC, BNB'
    if destinationTicker is not None and destinationTicker in acceptedDT and ticker != destinationTicker:
        if ticker == 'BTC' and destinationTicker == 'ETH':
            ticker = 'ETH'
            destinationTicker = 'BTC'
        elif ticker == 'USDT':
            tmp = destinationTicker
            destinationTicker = ticker
            ticker = tmp
        ticker += destinationTicker
        # if ticker not in binance.get_all_tickers():
        #     return -1

        info = binanceClient.get_ticker(symbol = ticker)
        lastPrice = info['lastPrice']
        return lastPrice
        # print(lastPrice + " " + destinationTicker)

    else:
        return checkIfTradable(ticker)






# def sumofAllBalances(ticker):


#TODO redo
def checkIfTradable(ticker, option = None):
        if ticker == 'USDT':
            return 1
        try:
            #ETH
            # print("we're in the ETH branch")
            ethereumPrice = binanceClient.get_ticker(symbol = 'ETHUSDT')
            priceETHUSDT = float(ethereumPrice['lastPrice'])
            tickerETH = ticker + 'ETH'
            firstTicker = binanceClient.get_ticker(symbol = tickerETH)
            tickerPrice = float(firstTicker['lastPrice'])
            priceInUSDT = tickerPrice * priceETHUSDT
            priceInUSDT = format(priceInUSDT, '.2f')
            # print('We succeded in the ETH branch')
            resultList.append('ETH')

        except:
            try:
                # print("We're in the BTC branch now")
                bitcoinPrice = binanceClient.get_ticker(symbol = 'BTCUSDT')
                priceBTCUSDT = float(bitcoinPrice['lastPrice'])
                tickerBTC = ticker + 'BTC'
                firstTicker = binanceClient.get_ticker(symbol = tickerBTC)
                tickerPrice = float(firstTicker['lastPrice'])
                priceInUSDT = tickerPrice * priceBTCUSDT
                priceInUSDT = format(priceInUSDT, '.2f')
                return priceInUSDT
            except:
                try:
                    # print("We're in the USDT branch now")
                    tickerUSDT = ticker + 'USDT'
                    firstTicker = binanceClient.get_ticker(symbol = tickerUSDT)
                    tickerPrice = float(firstTicker['lastPrice'])
                    tickerPrice = format(tickerPrice, '.2f')
                    return tickerPrice
                except:
                    # print('THIS IS NOT A TRADABLE TICKER')
                    return False


def checkIfTradableETH(ticker):
    ethereumPrice = binanceClient.get_ticker(symbol = 'ETHUSDT')
    priceETHUSDT = float(ethereumPrice['lastPrice'])
    tickerETH = ticker + 'ETH'
    firstTicker = binanceClient.get_ticker(symbol = tickerETH)
    tickerPrice = float(firstTicker['lastPrice'])
    priceInUSDT = tickerPrice * priceETHUSDT
    priceInUSDT = format(priceInUSDT, '.2f')
    return priceInUSDT

def checkIfTradableBTC(ticker):
    bitcoinPrice = binanceClient.get_ticker(symbol = 'BTCUSDT')
    priceBTCUSDT = float(bitcoinPrice['lastPrice'])
    tickerBTC = ticker + 'BTC'
    firstTicker = binanceClient.get_ticker(symbol = tickerBTC)
    tickerPrice = float(firstTicker['lastPrice'])
    priceInUSDT = tickerPrice * priceBTCUSDT
    priceInUSDT = format(priceInUSDT, '.2f')
    return priceInUSDT
def checkIfTradableUSDT(ticker):
    tickerUSDT = ticker + 'USDT'
    firstTicker = binanceClient.get_ticker(symbol = tickerUSDT)
    tickerPrice = float(firstTicker['lastPrice'])
    tickerPrice = format(tickerPrice, '.2f')
    return tickerPrice

    # else:



    # nonTradable = []
    # for ticker in allTickers:
    #     try:
    #         #ETH
    #         # print("we're in the ETH branch")
    #         ethereumPrice = binance.get_ticker(symbol = 'ETHUSDT')
    #         priceETHUSDT = float(ethereumPrice['lastPrice'])
    #         tickerETH = ticker + 'ETH'
    #         firstTicker = binance.get_ticker(symbol = tickerETH)
    #         tickerPrice = float(firstTicker['lastPrice'])
    #         priceInUSDT = tickerPrice * priceETHUSDT
    #         priceInUSDT = format(priceInUSDT, '.2f')
    #         # print('We succeded in the ETH branch')
    #         continue
    #     except:
    #         try:
    #             # print("We're in the BTC branch now")
    #             bitcoinPrice = binance.get_ticker(symbol = 'BTCUSDT')
    #             priceBTCUSDT = float(bitcoinPrice['lastPrice'])
    #             tickerBTC = ticker + 'BTC'
    #             firstTicker = binance.get_ticker(symbol = tickerBTC)
    #             tickerPrice = float(firstTicker['lastPrice'])
    #             priceInUSDT = tickerPrice * priceBTCUSDT
    #             priceInUSDT = format(priceInUSDT, '.2f')
    #             continue
    #         except:
    #             try:
    #                 # print("We're in the USDT branch now")
    #                 tickerUSDT = ticker + 'USDT'
    #                 firstTicker = binance.get_ticker(symbol = tickerUSDT)
                    # tickerPrice = float(firstTicker['lastPrice'])
    #                 tickerPrice = format(tickerPrice, '.2f')
    #                 continue
    #             except:
    #                 # print('THIS IS NOT A TRADABLE TICKER')
    #                 nonTradable.append(ticker)
    #
    #
    # pprint.pprint(nonTradable)

# getNonTradableTickers()
# balanceCheck()

# print(getPriceFromTicker('REQ', 'ETH'))
# pprint.pprint(binance.get_all_tickers())
# print(getPriceFromTicker('BNB'))
visualization.printRecentTrades('NEOETH', 5)
# pprint.pprint(binance.get_ticker(symbol = 'BTCUSDT'))
