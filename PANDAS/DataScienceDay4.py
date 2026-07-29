import pandas as pd
df = pd.read_csv(r"D:/students.csv")

#             FILTERING

# Give me all rows where Marks > 80
#print(df[df["Marks"] > 80])

# Give me all rows where city == ahmedabad
#print(df[df["City"] == "Ahmedabad"])

# # Give me all rows where age < 22
#print(df[df["Age"] < 22])


#         Multiple conditions

# Show students whose Marks > 80 AND whose City is Ahmedabad.
# print(df[(df["Marks"] > 80) & (df["City"] == "Ahmedabad")])

#Show students whose Age < 22 and Marks > 80
# print(df[(df["Age"] < 22) & (df["Marks"] > 80)])


# Show students from Rajkot OR students having Marks > 90.
print(df[(df["City"] == "Rajkot") | (df["Marks"] > 90)])

# Show students where age == 20 OR age == 22
print(df[(df["Age"] == 20) | (df["Age"]==22)])
