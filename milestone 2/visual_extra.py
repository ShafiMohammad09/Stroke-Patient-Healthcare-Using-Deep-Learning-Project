# Import necessary libraries
import pandas as pd               # For handling data manipulation and analysis
import matplotlib.pyplot as plt    # For creating static, interactive, and animated visualizations
import seaborn as sns             # For advanced statistical plotting, built on top of Matplotlib
import matplotlib.ticker as mtick  # For managing tick formatting in plots

# Load the dataset from a CSV file into a pandas DataFrame
df = pd.read_csv('D:\\coding stuff\\infosys\\github\\dataset\\data.csv')

# Fill missing values in the 'bmi' column with the column's mean value
df = df.assign(bmi=df['bmi'].fillna(df['bmi'].mean()))

# Set the Seaborn plotting style to 'whitegrid' (grid lines and white background)
sns.set(style="whitegrid")


# --- Plot 1: Stroke Rate by Gender ---
plt.figure(figsize=(8, 6))  # Create a figure of size 8x6 inches
gender_stroke = df.groupby('gender')['stroke'].mean()*100  # Group by gender and calculate mean stroke rate (multiply by 100 to get percentage)

# Create a barplot with gender on the x-axis and stroke rate percentage on the y-axis
sns.barplot(x=gender_stroke.index, y=gender_stroke.values, palette='viridis', hue=gender_stroke.index, dodge=False)

# Set the plot title and axis labels
plt.title('Stroke Rate by Gender')
plt.xlabel('Gender')
plt.ylabel('Stroke Rate (%)')

# Save the plot as a PNG file
plt.savefig('stroke_rate_by_gender_detailed.png')

# Display the plot
plt.show()


# --- Plot 2: Impact of Glucose Levels on Stroke Occurrence ---
plt.figure(figsize=(10, 6))  # Create a figure of size 10x6 inches

# Create a scatter plot with average glucose levels on the x-axis and stroke occurrence on the y-axis (0 or 1)
sns.scatterplot(data=df, x='avg_glucose_level', y='stroke', hue='stroke', palette={0: 'lightblue', 1: 'salmon'})

# Set the plot title and axis labels
plt.title('Impact of Glucose Levels on Stroke Occurrence')
plt.xlabel('Average Glucose Level')
plt.ylabel('Stroke Occurrence (0 = No, 1 = Yes)')

# Save the plot as a PNG file
plt.savefig('impact_of_glucose_on_stroke.png')

# Display the plot
plt.show()


# --- Plot 3: Stroke Rate by Hypertension and Heart Disease ---
plt.figure(figsize=(12, 6))  # Create a figure of size 12x6 inches

# Group by both hypertension and heart disease, then calculate the mean stroke rate for each combination
hypertension_heart_disease = df.groupby(['hypertension', 'heart_disease'])['stroke'].mean().unstack()

# Create a bar plot with a stacked format to visualize stroke rates by hypertension and heart disease
hypertension_heart_disease.plot(kind='bar', stacked=False, color=['skyblue', 'salmon'], ax=plt.gca())

# Set th
