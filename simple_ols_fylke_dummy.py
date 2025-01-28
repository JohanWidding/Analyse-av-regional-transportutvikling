import pandas as pd
import statsmodels.api as sm
import numpy as np

# Load the dataset
data = pd.read_csv('data.csv')

# Remove extreme values for percentage columns
upper_threshold = 10  # Upper limit (e.g., 100%)
lower_threshold = -10  # Lower limit (e.g., -50%)

columns_to_check = [
    'Befolkning_pct_increase',
    'Personbiler_pct_increase',
    'Bruttoprodukt_pct_increase',
    'Transportarbeid_pct_increase'
]

for column in columns_to_check:
    if column in data.columns:
        data = data[(data[column] <= upper_threshold) & (data[column] >= lower_threshold)]

# Drop rows where Fylke is "Oslo"
data = data[data['Fylke'] != 'Oslo']

# Convert 'Tid' to datetime
data['Tid'] = pd.to_datetime(data['Tid'], format='%Y')

# Create dummy variables for Fylke
fylke_dummies = pd.get_dummies(data['Fylke'], prefix='Fylke', drop_first=True)

# Combine dummy variables with the dataset
data = pd.concat([data, fylke_dummies], axis=1)

# Drop rows with missing values
data = data.dropna()

# Define dependent variable (y) and independent variables (X)
dummy_columns = [col for col in data.columns if col.startswith('Fylke_')]
X = data[['Befolkning_pct_increase', 'Personbiler_pct_increase', 'Bruttoprodukt_pct_increase'] + dummy_columns]
y = data['Transportarbeid_pct_increase']

# Ensure all data is numeric
X = X.apply(pd.to_numeric, errors='coerce')
y = pd.to_numeric(y, errors='coerce')

# Drop any remaining NaN values
X = X.dropna()
y = y.loc[X.index]  # Align y with X

# Add constant to X for the intercept
X = sm.add_constant(X)

# Perform OLS regression
model = sm.OLS(y, X).fit()

# Print regression summary
print(model.summary())
