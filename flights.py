# %%

import pandas as pd
import numpy as np
# %%

csv_files = ['1987.csv', '1989.csv', '1990.csv', '1991.csv', '1992.csv', '1993.csv', '1994.csv', '1995.csv', '1996.csv']
df_dict = {}

def data_cleaning(flight_df):
    # remove columns that contain NA values in all records 
    flight_df.replace('NULL', np.nan, inplace=True)
    flight_df.dropna(axis=1, how='all', inplace=True)
    # any records that still contain NA, replace with zeros
    flight_df.replace(np.nan, '0', inplace=True)
    return flight_df

def create_flight_dfs():
    # read csv files and add to dict
    for file in csv_files:
        df_dict[file] = data_cleaning(pd.read_csv(file))

create_flight_dfs()
# %%

def remove_columns(flight_df):
    # remove extra columns
    flight_df.drop(['TailNum', 'AirTime', 'TaxiIn', 'TaxiOut'], axis=1, inplace=True)

remove_columns(df_dict['1995.csv'])
remove_columns(df_dict['1996.csv'])
# %%

# integrate all dataframes into one master df
master_df = pd.concat((df_dict), ignore_index=True)
# %%

# export master df to csv
def export_to_csv(df):
    df.to_csv('combined_data.csv')

export_to_csv(master_df)