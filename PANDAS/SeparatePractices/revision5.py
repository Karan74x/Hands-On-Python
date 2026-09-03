import pandas as pd

#           5. Grouping & Aggregation


#              groupby("column name")
#       groups rows that have the same value.

import pandas as pd

df = pd.DataFrame({
    "Name": ["Karan", "Rahul", "Amit", "Anas", "Karan", "Rahul", "Amit", "Anas"],
    "Department": ["IT", "HR", "IT", "HR", "IT", "HR", "IT", "HR"],
    "Salary": [30000, 25000, 40000, 28000, 35000, 32000, 45000, 30000],
    "Experience": [1, 2, 3, 2, 2, 4, 5, 3]
})

# df.groupby("Department") to group by department

# for row in df.groupby("Department"):
#   print(row)


#           to group by Experience

# for row in df.groupby("Experience"):
#   print("\n",row)


#                    1. sum()

# is used to add up numeric values inside each group.
# Because .sum() is applied to all columns:

# Salary → numbers → added
# Experience → numbers → added
# Name → strings → concatenated

print(df.groupby("Department").sum())




#           only on a specific numeric column

# groupby("Department") → make groups
# ["Salary"]             → select Salary
# .sum()                 → add Salary

print(df.groupby("Department")
    ["Salary"]
    .sum())




#                2.mean(numeric_only=True) = average.

# Group employees by Department
# Then calculate the average of the numeric columns in each department
print(df.groupby("Department").mean(numeric_only=True))



#                    median()
#  means the middle value when the numbers are arranged in order.

#          Group employees by Department
# Then find the median (middle value) of the numeric columns

print(df.groupby("Department").median(numeric_only=True))



#         min() -> finds the smallest value in each group.

# Group employees by Department
# Then find the minimum value of each numeric column
print(df.groupby("Department").min(numeric_only=True))



#      max() -> finds the largest value in each group.

# Group employees by Department
# Then find the maximum value of each numeric column
print(df.groupby("Department").max(numeric_only=True))


#                   count()
# tells us how many non-empty values exist in each group.

print(df.groupby("Department").count())
