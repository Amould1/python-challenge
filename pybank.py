import os
import csv

csvpath = os.path.join(r'C:\Users\tiffa\downloads\budget_data.csv')
with open(csvpath) as csvfile:
    
    csvreader=csv.reader(csvfile,delimiter=',')
    
    months=0
    rev=0
    
    rows=[r for r in csvreader]
    
    change_rev=int(rows[1][1])
    min=rows[1]
    max = rows[1]
    
    for i in range(1,len(rows)):
        
        months=months+1
        row=rows[i]
        rev= int(row[1]) + rev
        
        if i > 1:
            change_rev=change_rev + int(row[1])-int(rows[i-1][1])
        
        if int(min[1]) > int(row[1]):
            min=row
        
        if int(max[1]) < int(row[1]):
            max=row

avg= int(rev /months)

print("Financial Analysis")
print("------------------")
print("Total Months: " + str(months))
print("Total : " +"$" +str(rev))       
print("Average Change: " +"$"+ str(avg))
print("Greatest Increase in Profits: " + str(max[0])+" ($" + str(max[1])+")")
print("Greatest Decrease in Profits: " + str(min[0])+" ($" + str(min[1])+")")



