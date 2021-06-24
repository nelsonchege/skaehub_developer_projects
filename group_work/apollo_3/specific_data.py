
# import libraries
import pdf_convertor as convert_to_pdf
# import libraries
import pandas as pd

# path to csv
csv_data = r"C:/Users/nelson/Desktop/apollo_3/covid.csv"
# to display all the rows in the csv
covid_data = pd.set_option("display.max_rows", None, "display.max_columns", None)
# read csv
covid_data = pd.read_csv(csv_data)
# convert the date and time to pandas date and time
covid_data['Last Update'] = pd.to_datetime(covid_data['Last Update'])
# select only the columns we need
date_df = covid_data[['Country/Region', 'Province/State', 'Deaths', 'Recovered', 'Last Update']]
# sort last date by country
date_df = date_df.sort_values('Last Update').groupby('Country/Region').last().reset_index()
# output
print(date_df)
# user prompt
answer = input(" Do you want a Pdf ?Enter yes or no: ")
if answer == "yes":
    # function to convert the dataframe to PDF
    convert_to_pdf.convert_to_pdf(date_df, "/home/maina-muriuki/Documents/Python Projects/Group Work/Day 3/",
                                  "last_update.pdf")
elif answer == "no":
    print("Okey.")
else:
    print("Please enter yes or no.")


"""import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

csv_data = r"covid.csv"
covid_data = pd.set_option("display.max_rows", None, "display.max_columns", None)
covid_data = pd.read_csv(csv_data)
covid_data['Last Update'] = pd.to_datetime(covid_data['Last Update'])
date_df = covid_data[['Country/Region', 'Province/State', 'Deaths', 'Recovered', 'Last Update']]
last_update = date_df.sort_values('Last Update').groupby('Country/Region').last()
print(last_update)

answer=input("do you want pdf: yes/no ")
if (answer == "yes"):
    df = pd.DataFrame(covid_data, columns=("Country/Region", "Province/State", "Deaths", "Recovered", "Last Update"))
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.axis('tight')
    ax.axis('off')
    the_table = ax.table(cellText=df.values, colLabels=df.columns, loc='center')

    pp = PdfPages("covid.pdf")
    pp.savefig(fig, bbox_inches='tight')
    pp.close()
else:
    print("ok")"""