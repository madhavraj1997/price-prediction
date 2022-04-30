import numpy as np
import pandas as pd
#import csv
#from csv import writer



def stock_name():
    data=[]
    stock=[]
    today_stock=[]
    index=0
    pos=[1]
    for i in range(1,13):
        ticker = pd.read_html('http://www.nepalstock.com/main/todays_price/index/'+ str(i) +'/')[0]
        for j in range(2,22):
            data.append(index)    
            index = index + 1
    
            if index == 227:
                break
        
            for k in range(1,10):
                data.append(ticker[k][j])
        #print(data)
        
            for i in range(0,1):
                stock.append(data[pos[i]])
        #print(stock)
            today_stock.append(stock)

            stock = []
            data = []
        #today_stock=[]
    print(today_stock)
    return today_stock