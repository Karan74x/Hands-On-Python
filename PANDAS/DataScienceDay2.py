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


print(df)
