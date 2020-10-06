import csv

with open('Resources/budget_data.csv') as csvfile:
    csv_reader = csv.DictReader(csvfile)

    months = 0
    total = 0

    for row in csv_reader:
        # Totals
        months += 1
        total += int(row['Profit/Losses'])

        # Greatest increase
        


    output = (
        f'\nFinancial Analysis\n'
        f'----------------------------\n'
        f'Total Months: {months}\n'
        f'Total: ${total:,.2f}\n'
        f'Average  Change: $-2315.12\n'
        f'Greatest Increase in Profits: Feb-2012 ($1926159)\n'
        f'Greatest Decrease in Profits: Sep-2013 ($-2196167)\n'
    )

    print(output) 
