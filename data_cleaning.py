import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("raw_data.csv")

print("Original Data")
print(df)

# Remove duplicates
df = df.drop_duplicates()

# Fill missing names
df["Name"] = df["Name"].fillna("Unknown")

# Fill missing salaries with average salary
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

# Department-wise Salary Report
report = df.groupby("Department")["Salary"].mean()

print("\nDepartment Salary Report")
print(report)

# Visualization
plt.figure(figsize=(8,5))
report.plot(kind="bar")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.tight_layout()
plt.savefig("salary_report.png")
plt.show()

print("\nAutomation Completed Successfully!")