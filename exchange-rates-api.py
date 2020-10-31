import requests
import pandas as pd

# create function to get data from the API
def get_exchange_rates(input):
    # connect to the API to get exchange rates for GBP during October 2020. The base currency is EUR.
    response = requests.get("https://api.exchangeratesapi.io/history?start_at=2020-10-01&end_at=2020-10-31&symbols=GBP")
    # create new variable 'rates' for the response from the API
    rates = response.json()
    # create a Pandas dataframe from the 'rates' level of the response
    df=pd.DataFrame(rates['rates'])
    # create a new variable 'rates_table' to hold the dataframe and transpose the table
    rates_table = df.T
    # rename the index column to be called 'Date'
    rates_table=rates_table.rename_axis('Date')
    # turn index to a column
    rates_table.reset_index(inplace=True)
    # rename the 'GBP' column to be called 'EURGBP'
    rates_table = rates_table.rename(columns={'GBP':'EURGBP'})
    # change data types
    rates_table['EURGBP'] = rates_table['EURGBP'].astype('float')
    rates_table['Date'] = rates_table['Date'].astype('str')
    return rates_table

# define the columns and their data types that are brought into Tableau Prep
def get_output_schema():
    return pd.DataFrame({
        'Date' : prep_string(),
        'EURGBP' : prep_decimal()
    })