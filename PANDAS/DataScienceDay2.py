import pandas as pd

#This converts the CSV into a DataFrame
# df = pd.read_csv(r"D:/students.csv")

#           specific column as index index_col="column name"

# ID as index.
# df = pd.read_csv(r"D:/students.csv",index_col="ID")

#  Name as index.
# df = pd.read_csv(r"D:/students.csv",index_col="Name")



#                    Read only selected columns. usecols=[]

# df = pd.read_csv(r"D:/students.csv", usecols=["ID", "Name", "Marks"])
# df = pd.read_csv(r"D:/students.csv", usecols=["ID", "Name", "Course"])



#                 only first few rows. nrows=value

# df = pd.read_csv(r"D:/students.csv", nrows=3)
# df = pd.read_csv(r"D:/students.csv", nrows=2)


#            Skip rows (also includes Column name rows) -> skiprows=value
# df = pd.read_csv(r"D:/students.csv", skiprows=4)

#            Give your own column names -> names=["A","B","C"]
# df = pd.read_csv(r"D:/students.csv", names=["A","B","C","D","E","F"])


#           Suppose CSV doesn't have column names.
# df = pd.read_csv(r"D:/students.csv",header=None)




#                     Force a datatype. dtype={"column name":data type}
# df = pd.read_csv(r"D:/students.csv", dtype={"Marks":float})
# df = pd.read_csv(r"D:/students.csv", dtype={"ID":float})


#                     SELECTING COLUMNS
df = pd.read_csv(r"D:/students.csv")

# One column -> Type Series
# print(df["Age"])

# Multiple columns -> Type DataFrame
# print(df[["Name", "City"]])
# print(df)

#              METHODS

#             value_counts()

# print(df["City"].value_counts())
# print(df["Course"].value_counts())


#             unique() -> Returns all unique values.(In an Array)
# print(df["City"].unique())
# print(df["Course"].unique())


#           nunique()-> Returns only the unique values count.
# print(df["City"].nunique())
# print(df["Age"].nunique())


#          shape -> (rows,columns)
# print(df.shape)

#         columns -> return all columns names (Array)
# print(df.columns)

# Shows number of rows, datatype, missing values, memory usage
# print(df.info())

# .describe() calculates summary statistics.
# By default, it runs on numeric columns, but it also works on text columns (using include='all').
# print(df.describe())
# print("\n\n\t\tAfter including all columns\n\n")
# print(df.describe(include='all'))


#              loc[]  → Location by NAME
# Give me the row whose index is 0 .
# print(df.loc[0])

# Give me the row whose index is  3
# print(df.loc[3])
# print(df)

#     Select One Value ->  loc[row index, "column name"]
# print(df.loc[2, "Name"])


# Select Multiple Columns -> loc[ :, ["Name", "Marks"]]
#                               ( : -> means All rows)
# print(df.loc[:, ["Name", "Marks"]])


# Select Multiple Rows -> loc[1:3] (1: 3 (includes 3rd index also))
# print(df.loc[1:3])

# print(df.loc[:4, ["Name", "Marks"]])


