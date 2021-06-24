import pandas as pd

csv_data = r"C:/Users/nelson/Desktop/apollo_3/covid.csv"
covid_data = pd.read_csv(csv_data)

covid_data.drop(['Province/State', 'Latitude', 'Longitude'], axis=1, inplace=True)
# print("Data columns:\n ", covid_data.columns)
covid_data['Last Update'] = pd.to_datetime(covid_data['Last Update'])

unique_countries = covid_data.groupby(covid_data['Country/Region']).sum()

date_df = covid_data[['Country/Region', 'Last Update']]

last_update = date_df.sort_values('Last Update').groupby('Country/Region').last()
filtered_data = pd.merge(unique_countries, last_update, on='Country/Region')
sorted = filtered_data.sort_values('Confirmed', ascending=False)
print(unique_countries)
ranked = sorted.head(20)
print("Top 20 Countries: \n", ranked)




