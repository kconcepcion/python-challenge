#importing the libraries
import os
import csv

#reading the file into the code
financialCSV = os.path.join("..", "Resources", "budget_data.csv")

#all variables used
monthCount = 0
monthTotalList = []
monthTotal = 0
monthAverageList = []
monthAverage = 0
financialList = []
greatIncMonth = " "
greatDecMonth = " "
greatIncPrice = 0
greatDecPrice = 0

with open(financialCSV, 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    
    header = next(csvReader)

    #counting how many months are in the list and compiling list with months and their totals
    for row in csvReader:
        monthCount += 1
        monthTotalList.append(int(row[1]))
        financialList.append(row[0])

    #compiling a list of the monthly differences
    for i in range(len(monthTotalList)-1):
        monthAverageList.append((monthTotalList[i+1]) - (monthTotalList[i]))

#these two lines get the greatest increase/decrease from the list of monthly averages
greatIncPrice = max(monthAverageList)
greatDecPrice = min(monthAverageList)

#these two lines are using the greatest increased/deccreased price that we just found, using it as in index to find the corresponding month in the financial list, however we have to plus one to get the correct place in the list
greatIncMonth = financialList[monthAverageList.index((greatIncPrice))+1]
greatDecMonth = financialList[monthAverageList.index((greatDecPrice))+1]

#summing all the month totals
monthTotal = sum(monthTotalList)

#getting the averages of the monthly differences
monthAverage = (sum(monthAverageList)/len(monthAverageList))

#printing out the results
print("Financial Analysis")
print("------------------------------")
print("Month total:", monthCount)
print("Total: $", monthTotal)
print("Average Change: $ %0.2f"% (monthAverage))
print("Greatest Increase in Profits: " + greatIncMonth + " (" + str(greatIncPrice) + ")")
print("Greatest Decrease in Profits: " + greatDecMonth + " (" + str(greatDecPrice) + ")")
#print(header)

#exporting results as a text file
outputFilePyBank = "finalResultPyBank.txt"

with open(outputFilePyBank,"w") as file:
    file.write("Financial Analysis\n")
    file.write("------------------------------\n")
    file.write("Month total: %d\n" % monthCount)
    file.write("Total: $%d\n" % monthTotal)
    file.write("Average Change: $" + (str(monthAverage)) + " \n")
    file.write("Greatest Increase in Profits: " + greatIncMonth + " (" + str(greatIncPrice) + ") \n")
    file.write("Greatest Decrease in Profits: " + greatDecMonth + " (" + str(greatDecPrice) + ") \n")
