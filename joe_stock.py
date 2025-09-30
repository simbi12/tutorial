noOfStockPurchased = 2000
amountPerStock = 40.00
amountPaidForStoch = noOfStockPurchased * amountPerStock
amountInitiallyPaidToBroker = 0.03 * amountPaidForStoch
sellingPricePerStock = 42.75
totalSellingPriceOfStock = sellingPricePerStock * noOfStockPurchased
amountPaidToBrokerAfterStockSales = 0.03 * totalSellingPriceOfStock
totalSumPaidToBRoker = amountInitiallyPaidToBroker + amountPaidToBrokerAfterStockSales
amountAfterDeductionOfCommission = totalSellingPriceOfStock - totalSumPaidToBRoker
print('The amount of money Joe paid for the stock ', amountPaidForStoch)
print('The amount of commission Joe paid his broker when he bought the stock', amountInitiallyPaidToBroker)
print('The amount that Joe sold the stock for.', totalSellingPriceOfStock)
print('The amount of commission Joe paid his broker when he sold the stock.', amountPaidToBrokerAfterStockSales)
print('Balance after dedcution', amountAfterDeductionOfCommission)
