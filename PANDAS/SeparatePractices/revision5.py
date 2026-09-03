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

for row in df.groupby("Department"):
  print(row)

# to group by Experience
for row in df.groupby("Experience"):
  print("\n",row)


