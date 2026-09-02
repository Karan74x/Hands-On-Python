import pandas as pd

#                 2. Missing Values



df = pd.DataFrame({
  "Name": ["Karan", "Rahul", None, "Anas", None, "Arnold"],
  "Age": [22, 45, None, 56, 16, None ]
})

#                   df["column"].isna()
#        is used to check whether a value is missing (NaN) or not.


#                 True → value is missing
#                False → value is present


print(df["Name"].isna())
print(df["Age"].isna())

