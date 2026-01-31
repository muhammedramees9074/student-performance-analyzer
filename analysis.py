import pandas as pd
import matplotlib.pyplot as plt


# Load student data
df = pd.read_csv("students.csv")

print("📊 Student Data:")
print(df)

# Calculate average marks
average_marks = df["Marks"].mean()
print("\n⭐ Average Marks:", average_marks)

# Categorize performance
def categorize(marks):
    if marks >= 80:
        return "Excellent"
    elif marks >= 60:
        return "Good"
    else:
        return "Needs Improvement"

df["Performance"] = df["Marks"].apply(categorize)

print("\n📈 Updated Student Performance:")
print(df)
print("\nSummary Statistics:")
print(df.describe())

# Plot student marks
plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()



