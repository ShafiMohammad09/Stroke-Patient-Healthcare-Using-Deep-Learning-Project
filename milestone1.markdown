# Importing required library
import pandas as pd

# Load dataset
df = pd.read_csv('dataset/data.csv')

# Data Exploration

## 1. Basic Exploration
### Basic statistical description of numerical data:
print("Basic statistical description of numerical data:")
print(df.describe())

### Dataset information (columns, types, and non-null counts):
print("\nDataset information (columns, types, and non-null counts):")
print(df.info())

### Shape of the dataset (rows, columns):
print("\nShape of the dataset (rows, columns):")
print(df.shape)

### Basic statistical description of categorical data:
print("\nBasic statistical description of categorical data:")
print(df.describe(include='object'))

## 2. Unique Value and Null Value Analysis

### Unique values in 'gender' column:
print("\nUnique values in 'gender' column:")
gender_unique = df['gender'].unique()
print(gender_unique)

### Unique values in 'smoking_status' column:
print("\nUnique values in 'smoking_status' column:")
smoking_status_unique = df['smoking_status'].unique()
print(smoking_status_unique)

### Check for null values in the dataset:
null_values = df.isnull().sum()
print("\nNull values in each column:")
print(null_values)

### Percentage of null values in each column:
null_percentage = df.isnull().mean() * 100
print("\nPercentage of null values in each column:")
print(null_percentage)

## 3. Observations

### Observation 1: Dataset dimensions
print(f"1. The dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")

### Observation 2: Missing values in 'bmi' column
missing_bmi_count = null_values['bmi']
if missing_bmi_count > 0:
    print(f"2. The 'bmi' column originally contained {missing_bmi_count} missing values.")
else:
    print("2. The 'bmi' column contains no missing values.")

### Observation 3: Unique values in 'gender' column
print(f"3. The 'gender' column contains the following unique values: {gender_unique}")

### Observation 4: Unique values in 'smoking_status' column
print(f"4. The 'smoking_status' column contains the following unique values: {smoking_status_unique}")

### Observation 5: Missing data analysis
print(f"5. The dataset contains missing data in the following columns (with percentages):")
print(null_percentage[null_percentage > 0])

## 4. Handling Missing Values in 'bmi' Column

### Option 1: Dropping rows with missing 'bmi' values
df_dropped = df.dropna(subset=['bmi'])  
print(f"6. After dropping rows with missing 'bmi' values, the dataset contains {df_dropped.shape[0]} rows.")

### Option 2: Imputing missing 'bmi' values with the mean
mean_bmi = df['bmi'].mean()
df['bmi'].fillna(mean_bmi, inplace=True)  
print(f"\nImputing missing 'bmi' values with mean value: {mean_bmi}")

### Check null values after imputation
null_values_after = df.isnull().sum()
print("\nNull values after imputing missing 'bmi' values:")
print(null_values_after)

### Observation 7: No missing values in 'bmi' column after imputation
if null_values_after['bmi'] == 0:
    print("7. After imputing, the 'bmi' column has no missing values.")

## 5. Duplicate Rows Check
### Identify duplicate rows in the dataset:
duplicates = df.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicates}")

## 6. Stroke Rate Analysis

### Stroke rate by gender:
print("\nStroke rate by gender:")
print(df.groupby('gender')['stroke'].mean())

# Observation of stroke rate by gender:
# gender
# Female    0.047094
# Male      0.051064
# Other     0.000000

### Stroke percentage by gender (relative to all stroke cases):
total = df['stroke'].sum()
strokes_gender = df[df['stroke'] == 1].groupby('gender')['stroke'].count()
stroke_per = (strokes_gender / total) * 100
print("\nStroke percentage by gender (relative to all stroke cases):")
print(stroke_per)

# Output of stroke percentage:
# gender
# Female    56.626506
# Male      43.373494
