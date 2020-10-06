import csv
import os 

#files 
inputfile = os.path.join("budget_data.csv")
outputfile = os.path.join("output.txt")


#financial parameters
totalmonths = 0

#file handling
with open (inputfile, "r") as csvreader:
    reader = csv.reader(csvreader, delimiter = ",")
    header = next(reader)
    firstrow = next(reader)
    totalmonths = totalmonths + 1

    for row in reader :
        totalmonths = totalmonths + 1








#output
output = "financial analysis\n"
output +="-----------------------------------------------------------\n"
output += f"total months{totalmonths}"
print (output)

with open (outputfile,"w") as txtfile:
    txtfile .write(output)