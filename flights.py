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

def update_dtypes(df):
    # change data types
    master_df['DepTime'] = master_df['DepTime'].astype('float')
    master_df['ArrTime'] = master_df['ArrTime'].astype('float')
    master_df['UniqueCarrier'] = master_df['UniqueCarrier'].astype('category')
    master_df['ActualElapsedTime'] = master_df['ActualElapsedTime'].astype('float')
    master_df['CRSElapsedTime'] = master_df['CRSElapsedTime'].astype('float')
    master_df['ArrDelay'] = master_df['ArrDelay'].astype('float')
    master_df['DepDelay'] = master_df['DepDelay'].astype('float')
    master_df['Origin'] = master_df['Origin'].astype('category')
    master_df['Dest'] = master_df['Dest'].astype('category')
    master_df['Distance'] = master_df['Distance'].astype('float')
    master_df['Cancelled'] = master_df['Cancelled'].astype('bool')
    master_df['Diverted'] = master_df['Diverted'].astype('bool')
    return df

update_dtypes(master_df)
# %%

# export master df to csv
def export_to_csv(df):
    df.to_csv('combined_data.csv', index=False)

export_to_csv(master_df)