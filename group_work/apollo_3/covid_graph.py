import pandas as pd
# this library is used for creating the graph
import matplotlib.pyplot as plt
# convert the csv file to dataframe
covid_data = pd.read_csv('covid.csv', usecols=['Last Update', 'Country/Region', 'Confirmed', 'Deaths', 'Recovered'])
# this creates a new collum for active cases
covid_data['Active'] = covid_data['Confirmed'] - covid_data['Deaths'] - covid_data['Recovered']
# we have to get the total number of case in every country
r_data = covid_data.groupby(["Country/Region"]).sum().reset_index()
# sort the grouped  data  by death
r_data = r_data.sort_values(by='Deaths', ascending=False)
# use data that has more than 200
r_data = r_data[r_data['Deaths'] > 200]
# gives the size for graphic output
plt.figure(figsize=(15, 5))
# creates the lines in the graph  for ech information wanted
plt.plot(r_data['Country/Region'], r_data['Deaths'], color='red')
plt.plot(r_data['Country/Region'], r_data['Confirmed'], color='green')
plt.plot(r_data['Country/Region'], r_data['Recovered'], color='blue')
plt.plot(r_data['Country/Region'], r_data['Active'], color='black')
# method to add title
plt.title('Total Deaths(>200), Confirmed, Recovered and Active Cases by Country')
# labeling x and y
plt.xlabel('Country')
plt.ylabel('Numbers of cases')
# ask user if to convert into pdf
answer =input("do you want pdf:yes/no")
if answer =="yes":
    # saves graph as pdf format
    plt.savefig('squares1.pdf')
else:
    print('ok')
# method to show the graph created
plt.show()
