import csv
import matplotlib.pyplot as plt
import numpy as np


with open('C:/Users/snake/OneDrive/Documents/GitHub/cs2900-python-ToddJewellMyers/Projects/Project1/crash_catalonia.csv') as File:
    reader = csv.reader(File)
    header = next(reader)
    crashes = []
    weeks = []
    for row in reader:
        crash = int(row[1])
        crashes.append(crash)
        week = row[0]
        weeks.append(week)

legend = ['crashes']
#making graph 
plt.style.use('ggplot')
fig, axs = plt.subplots(1,1, figsize=(10, 7), tight_layout=True)


# Add x, y gridlines 
axs.grid(b = True, color ='grey', linestyle ='-.', linewidth = 0.5, alpha = 0.6)

axs.plot(weeks, crashes, c="purple")

# setting up the title and the x and y label 
axs.set_title("Car crashes in Catalonia from 2000 to 2011, by day of week", fontsize=24)
axs.set_ylabel("Number of Crashes", fontsize=18)
axs.set_xlabel('Days of The Week', fontsize=18)
plt.legend(legend)


axs.tick_params(axis='both', which='major', labelsize=16)



plt.show()