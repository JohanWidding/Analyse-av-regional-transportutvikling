import pandas as pd
import numpy as np
import statsmodels.api as sm

# Load the dataset
file_path = "data.csv"  # Replace with your actual file path
data = pd.read_csv(file_path)

# Create the interaction term (cross between Region and Population)
data['Region_Population'] = data['Region'].astype(str) + "_" + data['Population'].astype(str)

# Perform one-hot encoding for the interaction term
data_encoded = pd.get_dummies(data, columns=['Region_Population'], drop_first=False)

# Group dummy columns by regions and randomly drop 10% of the dummies
region_dummy_cols = [col for col in data_encoded.columns if col.startswith('Region_Population_')]
regions = {col.split('_')[2] for col in region_dummy_cols}  # Extract unique regions

columns_to_keep = []
for region in regions:
    region_cols = [col for col in region_dummy_cols if f'Region_Population_{region}_' in col]
    num_to_drop = max(1, int(len(region_cols) * 0.10))  # Calculate 10% to drop, minimum 1
    drop_cols = np.random.choice(region_cols, size=num_to_drop, replace=False)
    keep_cols = [col for col in region_cols if col not in drop_cols]
    columns_to_keep.extend(keep_cols)

# Create a reduced dataset with the selected columns
reduced_data_encoded = data_encoded[['Population_Percent_Change', 'BNP_Percent_Change', 'Trafikkarbeid'] + columns_to_keep]

# Define predictors (X) and target variable (y)
X = reduced_data_encoded.drop(columns=['Trafikkarbeid'])
y = reduced_data_encoded['Trafikkarbeid']

# Ensure all data is numeric
X = X.astype(float)
y = y.astype(float)

# Add a constant term
X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(y, X).fit()

# Display the summary
print(model.summary())
