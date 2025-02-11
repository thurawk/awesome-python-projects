import pandas as pd
import matplotlib.pyplot as plt

# Updated data
data = {
    'Field': ['AI Engineer', 'ML Engineer', 'Software Engineer', 'Data Science', 'Full-Stack Developer'],
    'Job Opportunity': ['High', 'High', 'High', 'High', 'High'],
    'Median Income (USD)': ['$100,000 - $150,000', '$90,000 - $130,000', '$80,000 - $120,000', '$95,000 - $140,000', '$85,000 - $120,000'],
    'Entry Percentage': ['Moderate to High', 'Moderate to High', 'High', 'High', 'High']
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate job density based on Job Opportunity - Use different mapping for variation
job_density_mapping = {'Low': 1, 'Moderate': 2, 'Moderate to High': 3, 'High': 4}

# Since all job opportunities are 'High', we can incorporate median income or Entry Percentage into our job density calculation
df['Job Density'] = df['Entry Percentage'].map({'Low': 1, 'Moderate': 2, 'Moderate to High': 3, 'High': 4})

# Alternatively, if you want to incorporate Median Income, we can map income ranges to numerical values (e.g., a higher income range -> higher density)
def median_income_to_density(income_range):
    if "$100,000" in income_range or "$120,000" in income_range:
        return 4
    elif "$90,000" in income_range or "$110,000" in income_range:
        return 3
    else:
        return 2

df['Job Density'] = df['Median Income (USD)'].apply(median_income_to_density)

# Plotting bar graph
plt.bar(df['Field'], df['Job Density'], color=['blue', 'green', 'orange', 'red', 'purple'])
plt.xlabel('Field')
plt.ylabel('Job Density')
plt.title('Job Density Comparison of Different Fields')
plt.xticks(rotation=25, ha='right')  # Rotate x-axis labels for better visibility
plt.show()

# Output the DataFrame for checking
print(df)
