import pandas as pd
df = pd.read_csv(r"D:/students.csv")

#             FILTERING

# Give me all rows where Marks > 80
print(df[df["Marks"] > 80])

# Give me all rows where city == ahmedabad
print(df[df["City"] == "Ahmedabad"])

# # Give me all rows where age < 22
print(df[df["Age"] < 22])
