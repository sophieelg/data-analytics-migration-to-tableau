# %%

import pandas as pd
import numpy as np
# %%

csv_files = ['1987.csv', '1989.csv', '1990.csv', '1991.csv', '1992.csv', '1993.csv', '1994.csv', '1995.csv', '1996.csv']
df_dict = {}

def data_cleaning(flight_df):
    flight_df.replace('NULL', np.nan, inplace=True)
    flight_df.dropna(axis=1, how='all', inplace=True)
    flight_df.replace(np.nan, '0', inplace=True)
    return flight_df

def create_flight_dfs():
    for file in csv_files:
        df_dict[file] = data_cleaning(pd.read_csv(file))
# %%

create_flight_dfs()