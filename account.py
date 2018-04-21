
def balanceCheck(request = None, option = None):
    balanceAmount = 0
    totalAssetValue = 0

    if request == None:
        balances = binanceClient.get_account()
        stop = balances['balances']
        for asset in stop:
            total = float(asset['free']) + float(asset['locked'])
            if total == 0.00000000:
                continue
            total = format(total, "f")
            name = asset['asset']
            # name = name.replace("'", "") #could be not needed
            price = getPriceFromTicker(name)
            if price == -1:
                continue
            assetValue = float(total) * float(price)
            totalAssetValue += assetValue

            print("{}{}{}{}{}{}".format(name, ": ", price, "$", " ", total))
            if  option in acceptedOptions:
                if checkIfTradable(name, option) is True:
                    optionPrice = getPriceFromTicker(name, option)
                    if optionPrice == -1:
                        continue
                    # print("{}{}".format("optionPrice: ", optionPrice))
                    # print("{}{}".format("option: ", optionAmount))
                    singleAssetQty= float(optionPrice)*float(total)
                    # print(balanceAmount)
                # if amount > 10.0:
                    # print("{}{}{}{}".format(asset['asset'], " ", "Quantity: ", total))
                    print(singleAssetQty)
                else:
                    continue
        totalAssetValue = format(totalAssetValue, '.2f')
        print(totalAssetValue + '$')

    else:
        #TODO single
        balance = binanceClient.get_asset_balance(asset = request)
        free = float(balance['free'])
        inOrder = float(balance['locked'])
        total = free + inOrder

        if free != 0.00000000:
            print("{}{}{}{}".format("Available: ", free, " ", request))
        if inOrder != 0.0000000:
            print("{}{}{}{}".format("In order: ", inOrder, " ", request))
        if free != 0.0 and inOrder != 0.0:
            print("{}{}{}{}".format("Total: ", total, " ", request))
