import pandas as pd
df = pd.read_csv(r"D:/students.csv")
# To drop any columns
# print(df.drop(columns=["Age"]))
# print(df.drop(columns=["Age","Marks"]))

# to drop the row with specific index
# print(df.drop(index=2))
# print(df.drop(index=[2,3]))


# print(df)
# Remove rows that contain at least one NaN.
print(df.dropna()) # <- automatically axis=0 for rows

# Remove columns that contain at least one NaN.
print(df.dropna(axis=1))
