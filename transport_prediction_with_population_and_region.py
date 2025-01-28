import pandas as pd
import statsmodels.api as sm

# Load the dataset
file_path = "data.csv"  # Replace with your actual file path
data = pd.read_csv(file_path)

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

# Remove rows where any specified column exceeds thresholds
for column in columns_to_check:
    if column in data.columns:
        data = data[(data[column] <= upper_threshold) & (data[column] >= lower_threshold)]
# Drop rows where Fylke is "Oslo"
data = data[data['Fylke'] != 'Oslo']

# Perform one-hot encoding for the 'Region' variable
data_encoded = pd.get_dummies(data, columns=['Fylke'], drop_first=True)

# Define predictors (X) and target variable (y)
X = data_encoded[['Befolkning_pct_increase', 'Bruttoprodukt_pct_increase', 'Personbiler_pct_increase'] + [col for col in data_encoded.columns if col.startswith('Fylke_')]]
y = data_encoded['Transportarbeid_pct_increase']

# Ensure all data is numeric and drop problematic rows
X = X.apply(pd.to_numeric, errors='coerce')  # Coerce non-numeric values to NaN
y = pd.to_numeric(y, errors='coerce')       # Coerce non-numeric values to NaN

# Drop rows with NaN values from both X and y
valid_indices = X.dropna().index.intersection(y.dropna().index)
X = X.loc[valid_indices]
y = y.loc[valid_indices]

X = X.astype(float)
y = y.astype(float)

# Add a constant term to the predictors
X = sm.add_constant(X)

# Fit the OLS regression model
model = sm.OLS(y, X).fit()

# Display the summary of the regression
print(model.summary())
