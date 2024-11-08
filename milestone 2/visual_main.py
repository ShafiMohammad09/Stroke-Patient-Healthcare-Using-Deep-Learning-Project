# Import necessary libraries
import pandas as pd               # For data manipulation and analysis
import matplotlib.pyplot as plt    # For creating static, interactive, and animated visualizations
import seaborn as sns             # For advanced statistical plotting, built on top of Matplotlib

# Load the dataset from a CSV file into a pandas DataFrame
data = pd.read_csv('D:\\coding stuff\\infosys\\github\\dataset\\data.csv')

# Display the first few rows of the dataset to inspect the data
data.head()


# --- Age Distribution among Patients ---

# Create a figure for the histogram and KDE plot
plt.figure(figsize=(10, 6))

# Plot the age distribution with a histogram and a KDE (Kernel Density Estimate)
sns.histplot(data['age'], kde=True)

# Set the title and axis labels for the plot
plt.title("Age Distribution of Patients")
plt.xlabel("Age")
plt.ylabel("Frequency")

# Save the plot as a PNG file
plt.savefig('age_distribution.png')

# Display the plot
plt.show()

# Observation:
# The age distribution shows a roughly bimodal trend, with peaks around the ages of 40–60 
# and 80. There is a steady increase in patient numbers from younger ages up to middle age,
# after which it drops slightly before peaking again in older age groups.


# --- Average Glucose Level Difference Between Patients with and without a Stroke ---

# Create a figure for the boxplot
plt.figure(figsize=(10, 6))

# Create a boxplot to compare glucose levels between patients with and without a stroke
sns.boxplot(x='stroke', y='avg_glucose_level', data=data)

# Set the title and axis labels for the plot
plt.title("Average Glucose Level by Stroke Status")
plt.xlabel("Stroke")
plt.ylabel("Average Glucose Level")

# Save the plot as a PNG file
plt.savefig('glucose_by_stroke.png')

# Display the plot
plt.show()

# Observation:
# 1. The median glucose level is higher for patients who have experienced a stroke compared to 
#    those who have not.
# 2. There is a wider spread of glucose levels in stroke patients, indicating that high glucose 
#    levels might be more common in this group.


# --- Hypertension vs. Stroke Status ---

# Create a figure for the count plot
plt.figure(figsize=(8, 6))

# Create a count plot to show the distribution of hypertension status
sns.countplot(x='hypertension', data=data)

# Set the title and axis labels for the plot
plt.title("Hypertension vs Stroke Status")
plt.xlabel("Hypertension")
plt.ylabel("Count")

# Add a legend to indicate stroke status (0 = No, 1 = Yes)
plt.legend(title="Stroke")

# Save the plot as a PNG file
plt.savefig('hypertension_vs_stroke.png')

# Display the plot
plt.show()

# Observation:
# Most patients with hypertension do not have a stroke, as indicated by the large bar at the 
# zero mark. This suggests that while hypertension is a known risk factor, the majority of 
# hypertensive patients in this dataset have not experienced a stroke.


# --- Residence Type Distribution Among Stroke Patients ---

# Filter the data to include only stroke patients, then count the number of patients in each residence type (Urban/Rural)
stroke_residence = data[data['stroke'] == 1]['Residence_type'].value_counts()

# Create a pie chart for the residence type distribution among stroke patients
plt.figure(figsize=(6, 6))
stroke_residence.plot(kind='pie', autopct='%1.1f%%', startangle=140)

# Set the title of the plot
plt.title("Residence Type Distribution Among Stroke Patients")

# Remove the y-axis label for a cleaner pie chart
plt.ylabel("")  

# Save the plot as a PNG file
plt.savefig('residence_type_distribution.png')

# Display the plot
plt.show()

# Observation:
# 1. Stroke patients are slightly more likely to be from urban areas (54.2%) than rural areas 
#    (45.8%).
# 2. This distribution suggests that stroke cases are fairly common in both urban and rural 
#    populations, with a minor inclination toward urban residents.


# --- Correlation Between BMI and Average Glucose Level Among Stroke Patients ---

# Create a scatter plot to show the relationship between BMI and average glucose level by stroke status
plt.figure(figsize=(10, 6))
sns.scatterplot(x='bmi', y='avg_glucose_level', hue='stroke', data=data, palette="viridis")

# Set the title and axis labels for the plot
plt.title("BMI vs Average Glucose Level by Stroke Status")
plt.xlabel("BMI")
plt.ylabel("Average Glucose Level")

# Add a legend to indicate stroke status (0 = No, 1 = Yes)
plt.legend(title="Stroke")

# Save the plot as a PNG file
plt.savefig('bmi_vs_glucose.png')

# Display the plot
plt.show()

# Observation:
# 1. Patients with higher glucose levels and a wide range of BMIs (especially in the 20-60 range) 
#    are present among both stroke and non-stroke groups.
# 2. Stroke cases (marked by a different color) tend to cluster more towards higher glucose 
#    levels, suggesting a possible link between elevated glucose levels and stroke occurrence.


# --- Interaction Between Age, Average Glucose Level, and BMI in Relation to Stroke Status ---

# Create a pairplot to show relationships between age, glucose level, and BMI, colored by stroke status
sns.pairplot(data, vars=['age', 'avg_glucose_level', 'bmi'], hue='stroke')

# Set the title of the pairplot
plt.suptitle("Pairplot of Age, Glucose Level, and BMI by Stroke Status", y=1.02)

# Save the pairplot as a PNG file
plt.savefig('pairplot_age_glucose_bmi.png')

# Display the pairplot
plt.show()

# Observation:
# Patients who have experienced a stroke (indicated by orange markers) appear to cluster around 
# higher glucose levels and a wide range of ages, mostly over 40. There are a few outliers, with
# higher BMI values but no clear pattern between BMI and stroke status. This suggests that age 
# and glucose level may have a stronger correlation with stroke than BMI alone.
