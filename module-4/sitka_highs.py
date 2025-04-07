import csv, os
from datetime import datetime
from matplotlib import pyplot as plt
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent

filename = 'sitka_weather_2018_simple.csv'
with open(os.path.join(BASE_DIR,filename)) as f: ## included BASE_DIR to handle current path
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)

# Plot the high temperatures.
#plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Format plot.
plt.title("Daily high temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()