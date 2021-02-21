import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename="../../files/death_valley_2014.csv"
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    
#     for index,column_header in enumerate(header_row):
#         print(index,column_header)
    dates=[]
    highs=[]
    lows=[]
    for row in reader:
        try:
            current_date=datetime.strptime(row[0],'%Y-%m-%d')
            high=int(row[1])
            low=int(row[3])
        except ValueError:
            print(current_date,'missiing date')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            
#     print(highs)
    
    fig=plt.figure(dpi=100,figsize=(20,20))
    plt.plot(dates,highs,c='red',alpha=0.5)
    plt.plot(dates,lows,c='blue',alpha=0.5)
    plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
    plt.title("Daily high and low temperatures 2014",fontsize=24)
    plt.xlabel('',fontsize=10)
    fig.autofmt_xdate()
    plt.ylabel('Temperature(F)',fontsize=16)
    plt.tick_params(axis='both',which='major',labelsize=16)
    plt.show()