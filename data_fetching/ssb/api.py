import pandas as pd
import requests
import json
from jsonstat2_handeler import JSONStat2Handler


tables = ["06913","07849","09391"]
df_list = []

for table in tables:
    # Read the file and parse JSON into a dictionary
    payload = json.load(open(f'data_fetching/ssb/gamle fylker/ssbapi_table_{table}.json'))

    url = payload.get("postUrl")
    query_obj = payload.get("queryObj")

    # Send POST-forespørsel
    response = requests.post(url, json=query_obj)

    data = JSONStat2Handler(response.json())

    if table == "07849":
        df = data.process_to_dataframe(
            time_col = "Tid", 
            primary_col = "Region",
            merge_cols = ["ContentsCode", "DrivstoffType", "KjoringensArt"]
        )
    else:
        df = data.process_to_dataframe(
            time_col = "Tid", 
            primary_col = "Region",
            merge_cols = ["ContentsCode"]
        )

    df_list.append(df)


# Stack each DataFrame and assign column names
df_pop_stacked = df_list[0].stack().reset_index()
df_pop_stacked.columns = ['Tid', 'Fylke', 'Befolkning']

df_private_cars_stacked = df_list[1].stack().reset_index()
df_private_cars_stacked.columns = ['Tid', 'Fylke', 'Personbiler']

df_prod_stacked = df_list[2].stack().reset_index()
df_prod_stacked.columns = ['Tid', 'Fylke', 'Bruttoprodukt']

# Merge all stacked DataFrames on 'Tid' and 'Fylke'
panel_df = pd.concat([df_pop_stacked.set_index(['Tid', 'Fylke']),
                      df_private_cars_stacked.set_index(['Tid', 'Fylke']),
                      df_prod_stacked.set_index(['Tid', 'Fylke'])], axis=1).reset_index()


panel_df = panel_df.sort_values(by=['Fylke', 'Tid'], ascending=[True, True])



# Calculate percentage change for each column where applicable
columns_to_calculate = ["Personbiler", "Bruttoprodukt"]
df = pd.DataFrame(panel_df)
# Calculate percentage increase for 'Pop' (from current year to the next year) siden denne verdien er for 1. januar samme år
df['Befolkning_pct_increase'] = (df['Befolkning'].shift(-1) - df['Befolkning']) / df['Befolkning'] * 100

# Calculate percentage increase for 'Private_Cars' and 'Prod' (within the current year) siden disse verdiene er for siste dag i året
for column in columns_to_calculate:
    df[f"{column}_pct_increase"] = df[column].diff() / df[column].shift(1) * 100

df = df[df['Tid'] <= 2017]

df.to_csv('data_fetching/ssb/summary_data.csv', index=False)