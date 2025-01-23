import pandas as pd
import statsmodels.api as sm

# Load the dataset
file_path = "data.csv"  # Replace with your actual file path
data = pd.read_csv(file_path)

# Perform one-hot encoding for the 'Region' variable
data_encoded = pd.get_dummies(data, columns=['Region'], drop_first=True)

# Define predictors (X) and target variable (y)
X = data_encoded[['Population_Percent_Change'] + [col for col in data_encoded.columns if col.startswith('Region_')]]
y = data_encoded['Trafikkarbeid']

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
