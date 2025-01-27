import pandas as pd


ssb = pd.read_csv("data_fetching/ssb/summary_data.csv")
svv = pd.read_csv("data_fetching/svv/summary_data.csv")

# Melt the svv DataFrame
svv_melted = svv.melt(id_vars=["Fylke"], var_name="Tid", value_name="Transportarbeid_pct_increase")
svv = svv_melted.sort_values(by=['Fylke', 'Tid'], ascending=[True, True])
# Fjern rader der Fylke er "Heile landet"
svv = svv[svv["Fylke"] != "Heile landet"]

# Endre navnene i 'Fylke'-kolonnen
ssb["Fylke"] = ssb["Fylke"].str.split(r" -|\s\(-").str[0].str.strip()


# Ensure 'Tid' in both DataFrames is of the same type (e.g., int64)
ssb['Tid'] = pd.to_numeric(ssb['Tid'], errors='coerce')  # Convert to numeric
svv['Tid'] = pd.to_numeric(svv['Tid'], errors='coerce')  # Convert to numeric

# Merge df1 with df2 on Tid and Fylke
df = ssb.merge(svv[['Tid', 'Fylke', 'Transportarbeid_pct_increase']], on=['Tid', 'Fylke'], how='left')

df.to_csv('data.csv', index=False)