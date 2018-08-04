import csv

# Total Revenue Parameters
ttlMnths = 0
ttlRev = 0
preMonRev = 0
revChgList = []
greatestInc = ["",0]
greatestDec = ["",9999999999999999999]

with open ("resources/budget_data.csv") as Data:
    reader = csv.DictReader(Data)

    for item in reader:
        ttlMnths += 1
        print(item)
        thisMonthRev = int(item['Profit/Losses'])
        thisMonth = item['Date']
        ttlRev = ttlRev + thisMonthRev

        thisChange = thisMonthRev - preMonRev
        preMonRev = thisMonthRev

        revChgList.append(thisChange)

        #Calculate Greatest Increase
        if (thisChange > greatestInc[1]):
            greatestInc[0] = thisMonth
            greatestInc[1] = thisChange

        #Calculate Greatest Decrease
        if (thisChange < greatestDec[1]):
            greatestDec[0] = thisMonth
            greatestDec[1] = thisChange

    print(sum(revChgList))
    avgRevChange = sum(revChgList) / len(revChgList)

    print(ttlMnths) 
    print(ttlRev)
    print(greatestInc)
    print(greatestDec)
    print(round(avgRevChange),2)

# output to a txt file
with open("PyBank.txt", "w") as BankResult:
    BankResult.write("Financial Analysis \n")
    BankResult.write("----------------------------- \n")
    BankResult.write("Total months: " + str(ttlMnths) + "\n")
    BankResult.write("Total: " + str(f"${ttlRev}") + "\n")
    BankResult.write("Average Change: " + str(f"${avgRevChange}") + "\n")
    BankResult.write("Greatest Increase in Profits: " + str(greatestInc) + "\n")
    BankResult.write("Greatest Decrease in Profits: " + str(greatestDec) + "\n")



    

