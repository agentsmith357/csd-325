
import csv, os, sys
from datetime import datetime
from matplotlib import pyplot as plt
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent

def read_weather_data(filename, high_or_low):
    dates = []
    temps = []
    with open(os.path.join(BASE_DIR,filename)) as f:  ## included BASE_DIR to handle current path
        reader = csv.reader(f)
        header_row = next(reader)
        for row in reader:
            try:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                if high_or_low == 'high':
                    temp = int(row[5])
                else:
                    temp = int(row[6])
            except Exception as e:
                print(f"Error: {e}")
                continue
            dates.append(current_date)
            temps.append(temp)
    return dates, temps

def plot_temps(dates, temps, label):
    fig, ax = plt.subplots()
    '''
    When the user selects 'lows', they should see a graph, in blue, that reflects the lows for those dates.
    '''
    color = 'red' if label == 'High' else 'blue'
    ax.plot(dates, temps, c=color)
    plt.title(f"Daily {label.lower()} temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

filename = 'sitka_weather_2018_simple.csv'

while True:
    print("\nMenu:")
    print("1. Highs")
    print("2. Lows")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    ''' 
    Open the program with instructions on how to use the menu; Highs, Lows, or Exit.
    When the program starts, allow the user to select whether they want to see the high temperatures or the low temperatures, or to exit.
    Allow the program to loop until the user selects exit.
    '''

    if choice == '1':
        dates, temps = read_weather_data(filename, 'high')
        plot_temps(dates, temps, 'High')
    elif choice == '2':
        dates, temps = read_weather_data(filename, 'low')
        plot_temps(dates, temps, 'Low')
    elif choice == '3':
        print("Exiting the program. Thanks for exploring Sitka weather!")
        sys.exit() 
        ''' When the user exits, provide an exit message.'
         Use what elements you can from previous programs, perhaps including sys to help the exit process.'''
    else:
        print("Invalid input. Please choose 1, 2, or 3.")
