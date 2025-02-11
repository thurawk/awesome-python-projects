#Data Analysis and Visualization of Salary Data
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Creating a Sample Dataset
data = {
    'Name': ['Jin', 'Bob', 'Charlie', 'David', 'Jacob'],
    'Age': [23, 35, 45, 22, 26],
    'Salary': [70000, 80000, 72000, 65000, 120000],
    'colors': ['Green', 'yellow', 'red', 'blue', 'gray']
}

# Convert the data dictionary into a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Calculate the average age
average_age = df['Age'].mean()
print(f"Average Age: {average_age}")

# Calculate the average salary
average_salary = df['Salary'].mean()
print(f"Average Salary: {average_salary}")

# Plotting Age vs Salary
plt.figure(figsize=(8, 5))
plt.bar(df['Name'], df['Salary'], color= df['colors'])
plt.xlabel('Name')
plt.ylabel('Salary')
plt.title('Salary of Each Individual')
plt.show()

