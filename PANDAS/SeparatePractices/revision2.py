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



#               df["Column"].fillna()
#         .fillna() <- value to display, EX: 0/"unknown"

# df["Name"] = df["Name"].fillna("missing")
# df["Age"] = df["Age"].fillna(0)
# print(df)

#                          df.dropna()
#  is used to remove rows or columns that contain missing (NaN) values.
#         use dropna(axis = 1) <- to remove columns

print("\tbefore dropna()\n", df)

df = df.dropna()
print("\tafter dropna()\n",df)
