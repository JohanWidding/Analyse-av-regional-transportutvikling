import pandas as pd
from linearmodels.panel import PanelOLS
import statsmodels.api as sm

# Load your dataset
# Assuming the dataset is stored in 'data.csv'
data = pd.read_csv('data.csv')

# Define thresholds for percentage columns
upper_threshold = 10 
lower_threshold = -10  

# Columns to check for extreme values
columns_to_check = [
    'Befolkning_pct_increase',
    'Personbiler_pct_increase',
    'Bruttoprodukt_pct_increase',
    'Transportarbeid_pct_increase'
]
correlation_matrix = data[columns_to_check].corr()
print(correlation_matrix)
# Remove rows where any specified column exceeds thresholds
for column in columns_to_check:
    if column in data.columns:
        data = data[(data[column] <= upper_threshold) & (data[column] >= lower_threshold)]

# Drop rows where Fylke is "Oslo"
data = data[data['Fylke'] != 'Oslo']

# Convert the dataset to a panel data structure
data['Tid'] = pd.to_datetime(data['Tid'], format='%Y')  # Ensure 'Tid' is datetime
data = data.set_index(['Fylke', 'Tid'])  # Set multi-index with region and time

# Remove rows with missing values
data = data.dropna()

# Define independent variables (X) and the dependent variable (y)
X = data[['Befolkning_pct_increase', 'Personbiler_pct_increase', 'Bruttoprodukt_pct_increase']]
X = sm.add_constant(X)  # Add a constant term for the intercept
y = data['Transportarbeid_pct_increase']

# Perform Panel OLS regression
model = PanelOLS(y, X, entity_effects=True, time_effects=True)  # Fixed Effects Model
results = model.fit()

# Print results summary
print(results.summary)
