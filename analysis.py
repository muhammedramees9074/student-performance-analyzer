import pandas as pd

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
