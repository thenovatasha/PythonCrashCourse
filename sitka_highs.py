import csv
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Load file and read information
filename_1 = 'data/sitka_weather_2018_simple.csv'
filename_2 = 'data/death_valley_2018_simple.csv'

with open(filename_1) as f, open(filename_2) as f2:
    file = csv.reader(f)
    file2 = csv.reader(f2)
    header = next(file)
    header2 = next(file2)
    #4 , 5 

    for index, title in enumerate(header):
        print(index, title)
    max_temps, min_temps, dates2 = [], [], []
    for data in file2:
        try:
            temp_max = float(data[4])
            temp_min = float(data[5])
            date = datetime.strptime(data[2], '%Y-%m-%d')
        except ValueError:
            print('Error happened, data missing')    
            continue    
        else:
            max_temps.append(temp_max)
            min_temps.append(temp_min)
            dates2.append(date)

    precipitations, precipitations_2, dates = [], [], []
    for index, title in enumerate(header2):
        print(index, title)

        
    for data in file:
        try:
            precipitation = float(data[5])
            precipitation_2 = float(data[6])
            date = datetime.strptime(data[2], '%Y-%m-%d')    
               
        except ValueError:
            print('here')
            continue
            
        else:
            precipitations.append(precipitation)
            precipitations_2.append(precipitation_2)
            dates.append(date) 
plt.style.use('dark_background')
fig, ax = plt.subplots()

plt.plot(dates, precipitations, c='red')
plt.plot(dates, precipitations_2)
plt.plot(dates2, max_temps, c='green')
plt.plot(dates2, min_temps, c='purple')
fig.autofmt_xdate()
plt.fill_between(dates2,max_temps, min_temps, alpha=0.1)
plt.fill_between(dates, precipitations, precipitations_2, alpha=0.5) # type: ignore
# plt.yticks(np.arange(min(precipitations), max(precipitations) + 1, 2))
plt.show()